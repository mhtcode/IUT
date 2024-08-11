/*
 * List.h
 *
 * Class Description: List data collection ADT.
 * Class Invariant: Data collection with the following characteristics:
 *                   - Each element is unique (no duplicates).
 *                   - If capacity was not specified, is equal to MAX_ELEMENTS
 *
 * Author: (Masih Tanoursaz)
 * Date: (12/5/2022)
 */

#include <iostream>
#include "List.h"
#include "Patient.h"

List::List()
{
	this->header = new Node();
	this->elementCount = 0;
	this->capacity = MAX_ELEMENTS;
}

List::List(int _capacity)
{
	this->header = new Node();
	this->elementCount = 0;
	this->capacity = _capacity;
}
List::~List()
{
	delete this->header;
}

int List::getElementCount() const { return this->elementCount; }

bool List::insert(const Patient &newElement)
{
	Node *helper = new Node(newElement);
	if (elementCount < capacity)
	{
		elementCount++;
		if (elementCount == 1)
		{
			this->header = helper;
			return true;
		}
		Node *temp = this->header;
		if (helper->getData() > temp->getData())
		{
			helper->setNext(this->header);
			this->header = helper;
			return true;
		}
		else if (temp->getData() == helper->getData())
			return false;
		Node *temp2 = temp->getNext();
		while (temp2 != nullptr)
		{
			if (temp2->getData() < helper->getData())
				break;
			if (temp2->getData() == helper->getData())
				return false;
			temp = temp2;
			temp2 = temp->getNext();
		}
		temp->setNext(helper);
		helper->setNext(temp2);
	}
	else
	{
		cout << "Sorry we can not insert more patients.(There is not more capacity)" << endl;
		return false;
	}
}
bool List::remove(const Patient &toBeRemoved)
{
	if (!elementCount)
		return false;
	Node *temp = this->header;
	if (this->header->getData() == toBeRemoved)
	{
		this->header = temp->getNext();
		delete temp;
		temp = nullptr;
		if (--this->elementCount != 0)
			return true;
		this->header = new Node();
		return true;
	}
	Node *temp2 = this->header->getNext();
	while (temp2 != nullptr)
	{
		if (temp2->getData() == toBeRemoved)
		{
			temp->setNext(temp2->getNext());
			delete temp2;
			this->elementCount--;
			return true;
		}
		temp = temp->getNext();
		temp2 = temp2->getNext();
		if (temp2->getData() < toBeRemoved)
			return false;
	}
	return false;
}

void List::removeAll()
{
	Node *temp = this->header;
	Node *temp2 = this->header->getNext();
	while (temp2 != nullptr)
	{
		delete temp;
		temp = temp2;
		temp2 = temp2->getNext();
	}
	if (temp != this->header)
		delete temp;
	this->elementCount = 0;
}

Patient *List::search(const Patient &target)
{
	Node *temp = this->header;
	while (temp != nullptr)
	{
		if (temp->getData() == target)
		{
			Patient *helper = new Patient(temp->getData());
			return (helper);
		}
		temp = temp->getNext();
		if (temp->getData() < target)
			break;
	}
	Patient *nall = new Patient("", "", "", "", "");
	cout << "Patient not found." << endl;
	return nall;
}

void List::printList()
{
	Node *temp = this->header;
	if (elementCount == 0)
		return;
	while (temp)
	{
		cout << temp->getData() << endl;
		temp = temp->getNext();
	}
}

Node *List::edit(string _careCard)
{
	Node *temp = this->header;
	while (temp)
	{
		if (temp->getData().getCareCard() == _careCard)
		{
			return temp;
		}
		temp = temp->getNext();
	}
	Patient pa("");
	Node *helper = new Node(pa);
	return helper;
}

void List::edit(string _name, string _phone, string _email, string _carecard, string _address)
{
	Node *temp = this->header;
	while (temp)
	{
		if (temp->getData().getCareCard() != _carecard)
		{
			temp = temp->getNext();
		}
		else
		{
			Patient helper(_carecard, _name, _phone, _email, _address);
			temp->setData(helper);
			return;
		}
	}
	return;
}