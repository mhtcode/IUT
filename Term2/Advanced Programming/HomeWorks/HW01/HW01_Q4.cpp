#include <iostream>
using namespace std;

template <class T>
struct Node
{
    T data;           // Data Item
    Node<T> *next;    // Pointer to the next item of the List
    Node<T> *preview; // Pointer to the preview item of the list
};

template <class T>
class List
{

private:
    Node<T> *head;
    Node<T> *tail;

public:
    // Default Constructor
    List()
    {
        head = tail = NULL;
    }

    /*------------------- Insertion Functions -------------------*/
    void push_front(T item)
    {
        Node<T> *temp = new Node<T>;
        temp->data = item;

        temp->next = head;
        temp->preview = NULL;

        if (head != NULL)
            temp->next->preview = temp;
        else
            tail = temp;

        head = temp;
    }

    void push_back(T item)
    {
        Node<T> *temp = new Node<T>;
        temp->data = item;

        temp->preview = tail;
        temp->next = NULL;

        if (tail != NULL)
            temp->preview->next = temp;
        else
            head = temp;

        tail = temp;
    }

    /*------------------- Lookup Functions -------------------*/
    Node<T> *getHead()
    {
        return head;
    }

    Node<T> *getTail()
    {
        return tail;
    }

    Node<T> *searchForL(T item)
    {
        if (head == NULL) // If the list is empty
        {
            return NULL;
        }

        else if (item > tail->data)
        {
            return NULL;
        }

        else
        {
            Node<T> *current = head;

            while (current != NULL && current->data <= item)
            {
                if (current->data == item)
                {
                    return current;
                }

                current = current->next;
            }

            return NULL;
        }
    }

    /*------------------- Deletion Functions -------------------*/

    void deleteElement(T &item)
    {
        if (head != NULL) // If the list isn't empty.
        {
            Node<T> *current = head;

            while (current->next != NULL && current->data < item)
            {
                current = current->next;
            }

            // If the element is found.
            if (current->data == item)
            {
                if (current == head)
                {
                    head = head->next;

                    if (head == NULL)
                        tail = NULL;
                    else
                        head->preview = NULL;
                }

                else
                {
                    current->preview->next = current->next;

                    if (current->next != NULL)
                        current->next->preview = current->preview;
                    else
                        tail = current->preview;
                }

                delete current;
            }
        }
    }

    void pop_front()
    {
        if (head != NULL)
        {
            Node<T> *temp = head->next;
            delete head;
            head = temp;

            if (head == NULL)
                tail = NULL;

            else
                head->preview = NULL;
        }
    }

    void pop_back()
    {
        if (head != NULL)
        {
            Node<T> *temp = tail->preview;
            delete tail;
            tail = temp;

            if (tail == NULL)
                head = NULL;

            else
                tail->next = NULL;
        }
    }

    // Deletes a particular node if given the node's address
    void deleteNode(Node<T> *node)
    {
        if (node == head)
        {
            head = head->next;
        }

        else if (node == tail)
        {
            tail = tail->preview;
        }

        else
        {
            node->preview->next = node->next;
            node->next->preview = node->preview;
        }

        if (head != NULL)
        {
            head->preview = NULL;
            tail->next = NULL;
        }

        else
            tail = NULL;

        delete node;
    }

    /*------------------- Utility Functions -------------------*/
    int length()
    {
        int length = 0;
        Node<T> *current = head;

        while (current != NULL)
        {
            length++;
            current = current->next;
        }

        return length;
    }

    void Print()
    {
        if (head != NULL)
        {
            Node<T> *current = head;

            while (current != NULL)
            {
                cout << current->data << endl;
                current = current->next;
            }
        }

        else
            cout << "\nList is empty.";
    }

    // Get element at the desired position, eg 3rd element of list etc
    Node<T> *getDesiredElement(int n)
    {
        Node<T> *current = head;

        if (n <= length())
        {
            while (n != 1)
            {
                current = current->next;
                n--;
            }
        }

        return current;
    }
};
