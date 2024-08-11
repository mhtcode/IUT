#include <iostream>
#include "linkedlist.h"

int main()
{
     LinkedList<string> ll;

     ll.add("m");
     ll.add("masih");
     ll.add("50");
     ll.add("40");
     ll.add("70");
     ll.add("60");
     ll.add("80");

     ll.addFirst("15");
     ll.add("90");
     ll.add(2, "0");
     ll.add(5, "30");
     ll.addLast("100");

     ll.print();

     cout << endl
          << "LinkedList#remove(60)" << endl;
     ll.remove("60");
     ll.print();

     cout << endl
          << "LinkedList#reverse()" << endl;
     ll.reverse();
     ll.print();

     cout << endl
          << "LinkedList#sort(LinkedList<E>::SORT_Descending )" << endl;
     ll.sort(LinkedList<int>::SORT_DESC);
     ll.print();

     cout << endl
          << "LinkedList#sort(LinkedList<E>::SORT_Ascending)" << endl;
     ll.sort(LinkedList<int>::SORT_ASC);
     ll.print();

     cout << endl
          << "LinkedList#removeFirst()" << endl;
     ll.removeFirst();
     ll.print();

     cout << endl
          << "LinkedList#removeLast()" << endl;
     ll.removeLast();
     ll.print();

     cout << endl
          << "LinkedList#removeFirst()\nLinkedList#removeLast()" << endl;
     ll.removeFirst();
     ll.removeLast();
     ll.print();

     ll.clear();
     return 0;
}