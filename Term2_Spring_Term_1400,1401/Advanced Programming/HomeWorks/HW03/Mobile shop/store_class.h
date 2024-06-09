#ifndef STORE_CLASS_H
#define STORE_CLASS_H
#include <string>
#include "mobile_class.h"
#include "linkedlist.h"
#include <iostream>
using namespace std;

class store
{
private:
    static mobile *a;
    LinkedList<mobile> ll;
    static int count;

public:
    store();
    ~store();
    void printAllProducts();
};

int store::count{0};
mobile *store::a{new mobile};

store::store()
{
    a[count];
    a[count].setBrand("samsung");
    ll.addFirst(a[count]);
    // ll.findIndex(a[count]);
    cout << a[count].getBrand();
    count++;
}
store::~store() { delete a; }

void store::printAllProducts()
{
    for (int i = 0; i < count; i++)
    {
        cout << "The ( brand is " << a[count].getBrand() << " )\t"
             << " ( model is " << a[count].getModel() << " )\t"
             << " ( price is " << a[count].getPrice() << " )\t"
             << " ( resolution is " << a[count].getResolution() << " )\t"
             << " ( color is " << a[count].getColor() << " )\t " << endl;
    }
}

#endif