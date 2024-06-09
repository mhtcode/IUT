#include <iostream>
#include <string>

using namespace std;

// STRING functions
string tabee(string a, string b)
{
    return a + b;
}
string tabee(string a, bool b)
{
    if (1 == b)
        return a + " True";
    else
        return a + " False";
}
template <typename T>
string tabee(string a, T b)
{
    a += to_string(b);
    return a;
}
template <typename T>
string tabee(T a, string b)
{
    b += to_string(a);
    return b;
}
template <typename T>
string tabee(string a, T array[], int len)
{
    for (int i = 0; i < len; i++)
    {
        string num_str(to_string(array[i]));
        a += " " + num_str;
    }
    return a;
}

// ARRAY functions
template <typename T>
T tabee(T a[], T b[], int m, int n)
{
    T arr[m + n];
    for (int i = 0; i < m + n; i++)
    {
        if (i < m)
        {
            arr[i] = a[i];
        }
        else
        {
            arr[i] = b[i - m];
        }
    }

    for (int i = 0; i < m + n; i++)
    {
        cout << arr[i] << ' ';
        a[i] = arr[i];
    }
    cout << endl;
    return *a;
}
template <typename T>
int tabee(T a, T *array, int len)
{
    for (int i = len; i > 0; i--)
        array[i] = array[i - 1];
    array[0] = a;
    for (int j = 0; j < len + 1; j++)
        cout << array[j] << ' ';
    cout << endl;
    return *array;
}
template <typename T>
int tabee(T *array, T a, int len)
{
    array[len] = a;
    len++;
    for (int j = 0; j < len; j++)
        cout << array[j] << ' ';
    cout << endl;
    return *array;
}

// NUMBERS functions
template <typename T>
T tabee(T a, T b)
{
    return a + b;
}

// BOOLEAN functions
bool tabee(bool a, bool b)
{
    return a & b;
}

int main()
{
    float a = 10.25;
    float b = 12.35;
    int array1[] = {1, 2, 3};
    int array2[] = {4, 5, 6};
    float array3[] = {1.23, 2.34, 3.4};
    float array4[] = {4.57, 5.6, 6.75};

    int m = sizeof(array1) / sizeof(array1[0]);
    int n = sizeof(array2) / sizeof(array2[0]);

    string str = "ali";
    string str1 = "mohammadi";
    cout << tabee(str, str1) << endl;
    cout << tabee(10, str1) << endl;
    cout << tabee(str1, 10) << endl;
    cout << tabee(a, str1) << endl;
    cout << tabee(str1, b) << endl;
    cout << tabee(str1, b > a) << endl;
    cout << tabee(str, array1, 3) << endl;
    cout << tabee(1, 3) << endl;
    cout << tabee(a, b) << endl;
    cout << tabee(true, true) << endl;
    tabee(array1, array2, m, n);
    tabee(array3, array4, m, n);
    tabee(69, array1, m);
    cout << tabee(a, b) << endl;
    return 0;
}