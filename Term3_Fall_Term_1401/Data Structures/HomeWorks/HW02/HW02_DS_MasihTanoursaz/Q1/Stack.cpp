/*
 * Stack.cpp
 *
 * Description: Implementation of an int sequence with push/pop ...
 * Class Invariant: ... in a LIFO order
 *
 * Author: Masih Tanoursaz and Mohammad Hussein Heydarian
 * Date: 12/22/2022
 */

#include <cstddef> // For NULL
#include "Stack.h"
#include <iostream>

using namespace std;
using namespace std;

Stack::Stack()
{
    head = NULL;
    tail = NULL;
}

Stack::~Stack()
{
    StackNode* p = head;
    while (p != NULL)
    {
        head = head->next;
        delete p;
        p = head;
    }
}

void Stack::push(int _value)
{
    StackNode* temp = new StackNode();
    temp->data = _value;
    if (isEmpty())
    {
        temp->next = tail;
        head = temp;
        tail = temp;
    }
    else
    {
        tail->next = temp;
        tail = temp;
    }
}

int Stack::pop()
{
    if (isEmpty())
    {
        cout << "Stack is empty!!!" << endl;
        exit(1);
    }
    else
    {
        StackNode* temp;
        temp = head;
        int value ;
        if (head == tail)
        {
            value = head->data;
            delete head;
            head = NULL;
            tail = NULL;
            return value;
        }
        while (temp->next != tail )
            temp = temp->next;        
        tail = temp;
        temp = temp->next;
        tail->next = NULL ;
        value= temp->data;
        delete temp;
        return value;
    }
}

int Stack::peek() const
{
    if (isEmpty())
    {
        cout << "Stack is empty!!!" << endl;
        exit(1);
    }
    return tail->data;
}

bool Stack::isEmpty() const
{
    if (this->head == NULL && this->tail == NULL)
        return true;

    return false;
}