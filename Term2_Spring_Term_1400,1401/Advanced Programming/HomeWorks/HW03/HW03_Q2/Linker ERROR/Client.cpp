// Client.cpp
#include "TestTemp.h"

int main()
{
    TestTemp<int> TempObj;
    TempObj.SetValue(2);
    int nValue = TempObj.Getalue();
    return 0;
}