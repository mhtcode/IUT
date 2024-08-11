
#include "Scanner.h"
#include "Stack.h" // GENERIC STACK

#include <iostream>
using namespace std;

int compute(const int val1, const int val2, const string op) // Computing the result of operation (val1 op val2)
{
    if (op == "+")
    {
        return val1 + val2;
    }
    else if (op == "-")
    {
        return val1 - val2;
    }
    else if (op == "*")
    {
        return val1 * val2;
    }
    else if (op == "/")
    {
        if (val2 == 0) // We can not divide by zero
        {
            cout << "ERROR: Zero devision\n";
            exit(1);
        }
        return val1 / val2;
    }
}

int main()
{
    Scanner S(cin);
    Token t;

    Stack<Token> numstack, opstack; // 2x Stacks of type Token

    t = S.getnext();

    while (t.tt != eof || !opstack.isEmpty())
    {
        if (t.tt == lptok)
        {
            opstack.push(t);
            t = S.getnext();
        }
        else if (t.tt == integer)
        {
            numstack.push(t);
            t = S.getnext();
        }
        else if (t.tt == rptok)
        {
            if (opstack.peek().tt == lptok)
            {
                opstack.pop();
                t = S.getnext();
            }
            else
            {
                int val2 = numstack.pop().val;
                int val1 = numstack.pop().val;
                string op = opstack.pop().text;
                int res = compute(val1, val2, op);
                Token temp;
                temp.tt = integer;
                temp.text = to_string(res);
                temp.val = res;
                numstack.push(temp);
            }
        }
        else if (t.tt == pltok || t.tt == mitok || t.tt == eof)
        {
            if (!opstack.isEmpty() && (opstack.peek().tt == pltok || opstack.peek().tt == mitok || opstack.peek().tt == asttok || opstack.peek().tt == slashtok))
            {
                int val2 = numstack.pop().val;
                int val1 = numstack.pop().val;
                string op = opstack.pop().text;
                int res = compute(val1, val2, op);
                Token temp;
                temp.tt = integer;
                temp.text = to_string(res);
                temp.val = res;
                numstack.push(temp);
            }
            else
            {
                opstack.push(t);
                t = S.getnext();
            }
        }
        else if (t.tt == asttok || t.tt == slashtok)
        {
            if (!opstack.isEmpty() && (opstack.peek().tt == asttok || opstack.peek().tt == slashtok))
            {
                int val2 = numstack.pop().val;
                int val1 = numstack.pop().val;
                string op = opstack.pop().text;
                int res = compute(val1, val2, op);
                Token temp;
                temp.tt = integer;
                temp.text = to_string(res);
                temp.val = res;
                numstack.push(temp);
            }
            else
            {
                opstack.push(t);
                t = S.getnext();
            }
        }
    } // end of while
    Token tp = numstack.peek();
    cout << tp; // Print the result of operations in terminal

    return 0;
}
