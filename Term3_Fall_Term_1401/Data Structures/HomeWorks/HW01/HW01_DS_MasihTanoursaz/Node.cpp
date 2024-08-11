/*
 * Node.cpp
 *
 * Class Description: Need this for List.
 * Class Invariant: Each patient is data of each Node.
 *
 * Author: (Masih Tanoursaz)
 * Date: (12/5/2022)
 */
#include"Node.h"

Node::Node()
{
	this->next = nullptr;
}

Node::Node(const Patient &member)
{
	this->data = member;
	this->next = nullptr;
}

Node::~Node() {}

void Node::setData(const Patient & _patient)
{
	this->data = _patient;
}
Patient Node::getData()
{
	return this->data;
}

void Node::setNext(Node* _next) { this->next = _next; }
Node* Node::getNext() { return this->next; }