#include <iostream>
using namespace std;

/*
I did not have enough knowledge to solve this question so I used the site "geekforgeeks" resources with a relative understanding,
 I hope it will be acceptable
 */

typedef struct Node
{
    int data;
    Node *next;
};

Node *head = NULL;
void push(Node **head, int node_data)
{
    /* 1. create and allocate node */
    Node *newNode = new Node;

    /* 2. assign data to node */
    newNode->data = node_data;

    /* 3. set next of new node as head */
    newNode->next = (*head);

    /* 4. move the head to point to the new node */
    (*head) = newNode;
}

void insertAfter(Node *prev_node, int node_data)
{

    if (prev_node == NULL)
    {
        cout << "the given previous node is required,cannot be NULL";
        return;
    }

    Node *newNode = new Node;

    newNode->data = node_data;

    newNode->next = prev_node->next;

    prev_node->next = newNode;
}

void append(Node **head, int node_data)
{

    Node *newNode = new Node;

    Node *last = *head;

    newNode->data = node_data;

    newNode->next = NULL;

    if (*head == NULL)
    {
        *head = newNode;
        return;
    }

    while (last->next != NULL)
        last = last->next;

    last->next = newNode;
    return;
}

void print(Node *node)
{

    while (node != NULL)
    {
        cout << node->data << "-->";
        node = node->next;
    }

    if (node == NULL)
        cout << "null";
}
void swapNodes(Node **head_ref, int x, int y)
{
    if (x == y)
        return;

    Node *prevX = NULL, *currX = *head_ref;
    while (currX && currX->data != x)
    {
        prevX = currX;
        currX = currX->next;
    }

    Node *prevY = NULL, *currY = *head_ref;
    while (currY && currY->data != y)
    {
        prevY = currY;
        currY = currY->next;
    }

    if (currX == NULL || currY == NULL)
        return;

    if (prevX != NULL)
        prevX->next = currY;
    else
        *head_ref = currY;

    if (prevY != NULL)
        prevY->next = currX;
    else
        *head_ref = currX;

    Node *temp = currY->next;
    currY->next = currX->next;
    currX->next = temp;
}

float avgOfNodes(struct Node *head)
{
    // if head = NULL
    if (!head)
        return -1;

    int count = 0; // Initialize count
    int sum = 0;
    float avg = 0.0;

    struct Node *current = head; // Initialize current
    while (current != NULL)
    {
        count++;
        sum += current->data;
        current = current->next;
    }

    // calculate average
    avg = (double)sum / count;

    return avg;
}
void deleteNode(Node **head_ref, int position)
{

    // If linked list is empty
    if (*head_ref == NULL)
        return;

    // Store head node
    Node *temp = *head_ref;

    // If head needs to be removed
    if (position == 0)
    {

        // Change head
        *head_ref = temp->next;

        // Free old head
        free(temp);
        return;
    }

    // Find previous node of the node to be deleted
    for (int i = 0; temp != NULL && i < position - 1; i++)
        temp = temp->next;

    // If position is more than number of nodes
    if (temp == NULL || temp->next == NULL)
    {
        cout << "invalid input size!" << endl;
        return;
    }

    // Node temp->next is the node to be deleted
    // Store pointer to the next of node to be deleted
    Node *next = temp->next->next;

    // Unlink the node from linked list
    free(temp->next); // Free memory

    // Unlink the deleted node from list
    temp->next = next;
}
int search(Node *head, int x)
{
    Node *current = head; // Initialize current
    int index = 0;
    while (current != NULL)
    {
        if (current->data == x)
            return index;
        current = current->next;
        index++;
    }
    return -1;
}
Node *max()
{
    int max = -2147483647;
    Node *mx;

    while (head != NULL)
    {
        if (max < head->data)
        {
            mx = head->next;
            max = head->data;
        }
        head = head->next;
    }
    return mx;
}

/* main program for linked list*/
int main()
{

    Node *head = NULL;

    append(&head, 10);

    push(&head, 20);

    push(&head, 30);

    append(&head, 40); //

    insertAfter(head->next, 50);

    // swapNodes(&head, 20, 10);
    // cout << avgOfNodes(head) << endl;
    // deleteNode(&head, 6);
    // cout <<search(head, 10);

    // print(max());  ???!
    print(head);

    return 0;
}