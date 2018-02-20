#include <pthread.h>
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/syscall.h>

#define KEYLEN 1

static struct option long_options[] = {
	{"threads", optional_argument, 0, 't'},
	{"iterations", optional_argument, 0, 'i'},
	{"yield", required_argument, 0, 'y'},
	{"sync", required_argument, 0, 's'},
	{0, 0, 0, 0}
};

struct SortedListElement {
	struct SortedListElement *prev;
	struct SortedListElement *next;
	const char *key;
};
typedef struct SortedListElement SortedList_t;
typedef struct SortedListElement SortedListElement_t;

#define	INSERT_YIELD	0x01	// yield in insert critical section
#define	DELETE_YIELD	0x02	// yield in delete critical section
#define	LOOKUP_YIELD	0x04	// yield in lookup/length critical esction


int threads = 1;
int iterations = 1;
int opt_yield = 0;
int syncset = 0;
int mult;
char* keys;
SortedList_t* list;
char* yieldopt = "none";
char* syncopt = "none";
char status[15] = "list";
char delimit[2] = "-";
pthread_mutex_t mlock;


void SortedList_insert(SortedList_t *list, SortedListElement_t *element){
	SortedListElement_t *cur = element;;
	for (cur; cur; cur = cur->next)
	{}
	
	cur->next = element;

	if(opt_yield & INSERT_YIELD){
		sched_yield();
	}
	return;
}

int SortedList_delete( SortedListElement_t *element){
	if(element == NULL || element != element->next->prev || element != element->prev->next)
		return 1;
	if(opt_yield & DELETE_YIELD)
		sched_yield();
	element->prev = element->next;
	free(element);
	
	return 0;
}

SortedListElement_t *SortedList_lookup(SortedList_t *list, const char *key){
	SortedList_t* temp = list->next;
	while(temp != list){
		if(temp->key == key)
			return temp;
		if(opt_yield & LOOKUP_YIELD)
			sched_yield();
		temp = temp->next;
	}
	return NULL;
}

int SortedList_length(SortedList_t *list){
	int counter = 0;
	SortedList_t* temp = list->next;
	do{

		if(temp->next == list && temp->prev == list){
			return counter;
		}
		if(temp->prev->next != temp || temp->next->prev != temp)
			return -1;
		counter++;
		if(opt_yield & LOOKUP_YIELD)
			sched_yield();
		temp = temp->next;
	}while(temp != list);
	return counter;
}

void failedSysCall(char* function){
	fprintf(stderr, "System call %s failed with error number %d: %s\n",function, errno, strerror(errno));
	exit(1);
}

void failedFuncCall(char* function, int errnum){
	fprintf(stderr, "Function %s failed with error number %d: %s\n",function, errnum, strerror(errnum));
	exit(2);
}

void getArg(int argc, char* argv[]){
	char option;
	while(1){
		int option_index;
		option = getopt_long(argc, argv, "t::i::y:", long_options, &option_index);
		if(option == -1)
			break;
		if(option == 't' && optarg != NULL)
			threads = atoi(optarg);
		else if(option == 'i' && optarg != NULL)
			iterations = atoi(optarg);
		else if(option == 'y'){
			yieldopt = optarg;
			if(strchr(optarg, 'i') != NULL)
				opt_yield = opt_yield | INSERT_YIELD;
			if(strchr(optarg, 'd') != NULL)
				opt_yield = opt_yield | DELETE_YIELD;
			if(strchr(optarg, 'l') != NULL)
				opt_yield = opt_yield | LOOKUP_YIELD;
		}
		else if(option == 's'){
			syncopt = optarg;
			syncset = 1;
			if(optarg[0] == 'm'){
				pthread_mutex_init(&mlock, NULL);
			}
		}
		else if(option == '?'){
			fprintf(stderr, "Unrecognized option\nOnly supported arguments are --threads, --iterations, and --yield\n");
			exit(1);
		}
	}
}

void generateChar(char* keys, int mult){
	for(int i = 0; i < mult; i++){
		keys[i] = 'A' + rand() % 26;
	}
}

void *exec_threads(void* arg){
	int *counter = (int*)arg;
	printf("exec threads tid = %d\n", syscall(SYS_thread_selfid));
	int index = mult/threads * (*counter);
	printf("index: %d\n", index);
	for(int i = 0; i < iterations; i++){
		SortedListElement_t* element = (SortedList_t*)malloc(sizeof(SortedList_t));
		element->key = &keys[index + i];
		SortedList_insert(list, element);
	}
	for(int i = 0; i < iterations; i++){

		SortedList_t* element = SortedList_lookup(list, &keys[index + i]);
		if(element == NULL){
			fprintf(stderr, "Could not find element %c in the list\n", keys[index+i]);
			exit(2);
		}
		if(SortedList_delete(element)){
			fprintf(stderr, "Corrupted list\n");
			exit(2);
		}
	}
	return NULL;
}

int main(int argc, char* argv[]){
	long long elapse_time;
	int check;
	pthread_t tid[threads];
	getArg(argc, argv);
	srand(time(NULL));
	list = (SortedList_t*)malloc(sizeof(SortedList_t));
	list->next = list;
	list->prev = list;
	mult = threads * iterations;
	keys = (char*)malloc(mult*sizeof(char));
	generateChar(keys, mult);
	struct timespec start_time;
	clock_gettime(CLOCK_MONOTONIC, &start_time);
	for(int i = 0; i < threads; i++){
		int* id = (int*)malloc(sizeof(int));
		*id = i;
		check = pthread_create(&tid[i], NULL, exec_threads, (void*)id);
		if(check != 0)
			failedFuncCall("pthread_create", check);
	}
	for(int i = 0; i < threads; i++){
		printf("%d\n", i);

		check = pthread_join(tid[i], NULL);
		if(check != 0)
			failedFuncCall("pthread_join", check);
	}
	if(SortedList_length(list)){
		fprintf(stderr, "Finished list length is not 0\n");
		exit(2);
	}
	struct timespec end_time;
	clock_gettime(CLOCK_MONOTONIC, &end_time);
	elapse_time = (end_time.tv_sec - start_time.tv_sec) * 1000000000;
	elapse_time += end_time.tv_nsec;
	elapse_time -= start_time.tv_nsec;
	strcat(status, delimit);
	strcat(status, yieldopt);
	strcat(status, delimit);
	strcat(status, syncopt);
	printf("%s,%d,%d,%d,%d,%lld,%lld\n", status, threads, iterations, 1, threads*iterations*3, elapse_time, elapse_time/(threads*iterations*3));
}