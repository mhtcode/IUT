#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int **CreateMatrix(int row, int col)
{
    int **ptr = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < row; i++)
        ptr[i] = (int *)malloc(sizeof(int) * col);
    return ptr;
}

template <typename T>
void **FillMatrix(T **ptr, int row, int col)
{
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            cin >> ptr[i][j];
        }
    }
    return 0;
}
template <typename T>
void **operation(T **mult, T **mat1, T **mat2, int row1, int col1, int col2)
{
    for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col2; ++j)
        {
            mult[i][j] = 0;
        }
    for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col2; ++j)
            for (int k = 0; k < col1; ++k)
            {
                mult[i][j] += mat1[i][k] * mat2[k][j];
            }
    return 0;
}
template <typename T>
void PrintMatrix(T **mat1, T **mat2, int row1, int col1, int col2)
{
    int **mult = CreateMatrix(row1, col2);
    operation(mult, mat1, mat2, row1, col1, col2);
    for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col2; ++j)
        {
            cout << mult[i][j] << " ";
            if (j == col2 - 1)
                cout << endl;
        }

    free(mult);
}

int main()
{
    int row1, col1, col2, d;
    cin >> row1 >> col1 >> col2 >> d;

    int **mat1 = CreateMatrix(row1, col1);
    int **mat2 = CreateMatrix(col1, col2);

    switch (d)
    {
    case 2:

        break;
    case 1:

        break;
    case 0:
        FillMatrix(mat1, row1, col1);
        FillMatrix(mat2, col1, col2);

        PrintMatrix(mat1, mat2, row1, col1, col2);

        free(mat1);
        free(mat2);
        break;
    case -1:
        break;
    default:
        break;
    }

    return 0;
}