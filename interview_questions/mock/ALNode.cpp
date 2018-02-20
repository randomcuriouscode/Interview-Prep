class ALNode {
    public:
      int value;
      ALNode *next;
      ALNode *arbitrary;
};

#include <vector>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

ALNode *deepCopy(ALNode *head){
  vector<ALNode*> nodes;
  vector<ALNode*> newNodes;
  ALNode* newHead = new ALNode();

  auto tmp = newHead;
  for (ALNode* node = head; node != NULL; node = node->next)
  {
    nodes.push_back(node);
    newNodes.push_back(tmp);
    tmp->value = node->value;
    tmp->next = new ALNode();
    tmp = tmp->next;
  }

  int nodeIndex = 0;
  for (ALNode* node = head; node != NULL; node = node->next)
  {
    if (node->arbitrary){
      auto it = find(nodes.begin(), nodes.end(), node->arbitrary);
      int arbIndex = distance(nodes.begin(), it);
      cout << nodeIndex << "->" << arbIndex << endl;
      newNodes[nodeIndex]->arbitrary = newNodes[arbIndex];
    }
    nodeIndex ++;
  }

  return newHead;
}

int main(){
  ALNode* head = new ALNode();
  head->value = 10;
  head->next = new ALNode();
  head->arbitrary = head->next;
  head->next->value = 9;
  head->next->arbitrary = head;

  cout << head->value << "->" << head->next->value << endl;
  cout << head->arbitrary->value << "->" << head->next->arbitrary->value << endl;
  cout << "old ^^^^^^^^^ ____ new vvvvvvvvvvvv" << endl;
  
  ALNode* newhead = deepCopy(head);
  cout << newhead->value << "->" << newhead->next->value << endl;
  cout << newhead->arbitrary->value << "->" << newhead->next->arbitrary->value << endl;
}