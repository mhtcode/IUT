#include <iostream>
using namespace std;

int **CreateMatrix(int &row, int &col);
void **FillMatrix(int **ptr, int row, int col);
void PrintMatrix(int **array1, int **array2, int &Q, int &W, int &E);
void **calcmat(int **mult, int **mat1, int **mat2, int &row1, int &col1, int &col2);

int main()
{
    int row1, col1, col2;
    cin >> row1 >> col1 >> col2;
    int **mat1 = CreateMatrix(row1, col1);
    int **mat2 = CreateMatrix(col1, col2);
    FillMatrix(mat1, row1, col1);
    FillMatrix(mat2, col1, col2);

    PrintMatrix(mat1, mat2, row1, col1, col2);

    free(mat1);
    free(mat2);
    return 0;
}

int **CreateMatrix(int &row, int &col)
{
    int **ptr = (int **)malloc(sizeof(int *) * row);
    for (int i = 0; i < row; i++)
        ptr[i] = (int *)malloc(sizeof(int) * col);
    return ptr;
}

void **FillMatrix(int **ptr, int row, int col)
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

void PrintMatrix(int **mat1, int **mat2, int &row1, int &col1, int &col2)
{
    int **mult = CreateMatrix(row1, col2);
    calcmat(mult, mat1, mat2, row1, col1, col2);
    for (int i = 0; i < row1; ++i)
        for (int j = 0; j < col2; ++j)
        {
            cout << mult[i][j] << " ";
            if (j == col2 - 1)
                cout << endl;
        }

    free(mult);
}
void **calcmat(int **mult, int **mat1, int **mat2, int &row1, int &col1, int &col2)
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