/*
 * Queue.cpp
 *
 * Description: Implementation of an int sequence with enqueue/dequeue ...
 * Class Invariant: ... in FIFO order
 *
 * Author: Masih Tanoursaz & Mohammad Hossein Heydarian
 * Date: 12/26/2022
 */

#include "Queue.h"

// Description:  Constructor, initalize elements and dynamic allocation space for elements array.
Queue::Queue() : elementCount(0), capacity(INITIAL_CAPACITY), frontindex(0), backindex(0)
{
    elements = new int[INITIAL_CAPACITY];
}

// Description:  Inserts element x at the back (O(1), If it was full O(n))
void Queue::enqueue(int x)
{
    if (elementCount == capacity) // Check array is full or not, if it was full we should resize it 2x
    {
        int *newElementsArr = new int[capacity * 2]; // Create a new array 2x bigger than last one

        // Copy all elements from this->elements to new (newElementsArr) Array
        int i = 0;
        for (; frontindex < capacity; i++, frontindex++)
        {
            newElementsArr[i] = this->elements[frontindex];
        }
        frontindex = frontindex % capacity;
        for (; frontindex <= backindex; i++, frontindex++)
        {
            newElementsArr[i] = this->elements[frontindex];
        }

        frontindex = 0;
        backindex = elementCount;
        delete[] elements;
        elements = newElementsArr;
        capacity *= 2;
    }
    elementCount++;
    elements[backindex] = x;
    backindex = (backindex + 1) % capacity;
}

// Description:  Removes the frontmost element (O(1), if (elementCount < capacity / 4) O(n))
// Precondition:  Queue not empty
void Queue::dequeue()
{
    if (elementCount < (capacity / 4) && INITIAL_CAPACITY <= (capacity / 2)) // If there are less element than forth of the capacity we have to resize queue to half
    {
        int *newElementsArr = new int[capacity / 2]; // Create a new array with half the size

        // Copy all elements from this->elements to new (newElementsArr) Array
        for (int index = 0; frontindex < backindex; frontindex++, index++)
        {
            newElementsArr[index] = this->elements[frontindex];
        }

        frontindex = 0;
        backindex = elementCount;
        delete[] elements;
        elements = newElementsArr;
        capacity /= 2;
    }
    elementCount--;
    frontindex = (frontindex + 1) % capacity;
}

// Description:  Returns a copy of the frontmost element (O(1))
// Precondition:  Queue not empty
int Queue::peek() const
{
    return elements[frontindex];
}

// Description:  Returns true if and only if queue empty (O(1))
bool Queue::isEmpty() const
{
    return elementCount == 0;
}