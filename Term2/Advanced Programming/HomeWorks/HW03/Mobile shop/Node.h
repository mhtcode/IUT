#ifndef NODE_H
#define NODE_H

template <class T>
class Node
{
public:
    T value;
    Node<T> *next;

    Node();

    explicit Node(T val); // using explicit for not implicitly convert types
};
template <class T>
Node<T>::Node()
{
    next = nullptr;
}

template <class T>
Node<T>::Node(T val)
{
    value = val;
    next = nullptr;
}

#endif