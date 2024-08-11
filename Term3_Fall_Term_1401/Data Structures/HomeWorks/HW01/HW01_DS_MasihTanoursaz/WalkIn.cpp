/*
 * WalkIn.cpp
 *
 * Author: (Masih Tanoursaz)
 * Date: (12/5/2022)
 */

// Includes
#include <iostream>
#include "List.h"
#include "Node.h"
#include "Patient.h"

int main()
{
    Patient p1("1927364938");
    Patient p2("1111111111");
    Patient p3("3333333333");
    Patient p4("2222222222");
    Patient p5("1234532678", "Mohsen", "09132345743", "email@email.com", "Isfahan");

    List list;
    List list1(4);
    list.insert(p1);
    list.insert(p2);
    list.insert(p3);
    list.insert(p4);

    cout << *(list.search(p2)) << endl;

    list.printList();

    list.remove(p4);
    list.printList();
    list.removeAll();
    list.printList();
    cout << "..............." << endl;
    cout << list.remove(p1) << endl;
    cout << "..............." << endl;
    list1.insert(p5);
    list1.insert(p3);
    list1.insert(p2);
    list1.insert(p1);
    list1.insert(p4);

    Patient *helper = list1.search(p5);
    cout << (*helper) << endl;
    delete helper;
    list1.edit("Hamed", "09139999999", "email@helper.com", "1234532678", "Isfahancity");
    cout << "#####################################################" << endl;
    list1.printList();
}
