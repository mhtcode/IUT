/*
 * Node.h
 *
 * Class Description: Nodes of List.
 * Class Invariant: Each patient is like a Node.
 *                  The List(List class) is contains some Nodes and each Node is just a Patient(Patient class)
 *
 * Author: (Masih Tanoursaz)
 * Date: (12/5/2022)
 */
#pragma once
#include"Patient.h"
	class Node
{
private:
	Patient  data;
	Node* next;
public:
	// Default Constructor
	// Description: Create a Node and sets "next" attribute to nullptr.
	Node();
	// Parameterized Constructor
	// Description: Create a Node and sets ("data", "next")  attributes to (given Patient, nullptr).
	Node(const Patient &);
	// Destructor
	~Node();
	// Setter
	void setData(const Patient & );
	void setNext(Node*);
	// Getter
	Node* getNext();
	Patient getData();
};

