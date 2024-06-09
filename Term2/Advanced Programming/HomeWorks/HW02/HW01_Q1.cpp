#include <iostream>
#include <string>  // for whenDay Function
#include <iomanip> // for setfill and setw

using namespace std;

class Time
{
private:
    int hours, minute;

public:
    // constructor with default value 0
    Time(int h = 0, int m = 0);
    Time(int h);

    // setter function
    void setHour(int h);
    void setMinute(int m);

    // getter function
    int getHour();
    int getMinute();

    void showTime();
    // normalize the time
    void normalize();

    string whenDay();

    // check equalitys of objects
    bool equals(Time);
};

Time ::Time(int h, int m)
{
    hours = h;
    minute = m;
}
Time ::Time(int h)
{
    hours = h;
    minute = 0;
}
void Time ::setHour(int h)
{
    hours = h;
}
void Time ::setMinute(int m)
{
    minute = m;
}
int Time ::getHour()
{
    return hours;
}
int Time ::getMinute()
{
    return minute;
}
void Time ::showTime()
{
    cout << setw(2) << setfill('0') << hours << ":"
         << setw(2) << setfill('0') << minute << whenDay() << endl;
}
void Time ::normalize()
{
    hours += minute / 60;
    minute %= 60;
    hours %= 24;
}
string Time ::whenDay()
{
    if ((0 <= hours && hours < 12) && (0 <= minute && minute <= 59))
        return " Morning";
    else if (hours == 12 && minute == 0)
        return " Noon";
    else if ((12 <= hours && hours <= 16) && (1 <= minute && minute <= 59))
        return " Afternoon";
    else if ((17 <= hours && hours <= 19) && (0 <= minute && minute <= 59))
        return " Evening";
    else
        return " The night";
}
bool Time ::equals(Time otherTime)
{
    if (hours == otherTime.hours && minute == otherTime.minute)
        return true;
    else
        return false;
}

int main()
{
    while (1)
    {
        int h1, m1, h2, m2;
        cout << endl;
        cout << "Enter the first time hour : ";
        cin >> h1;
        cout << "Enter the first time minute : ";
        cin >> m1;
        cout << "Enter the second time hour : ";
        cin >> h2;
        cout << "Enter the second time minute : ";
        cin >> m2;
        if (h1 > 24 || h2 > 24 || m1 > 60 || m2 > 60)
        {
            string tmp;
            cout << "\nYou have entered incorrect numbers!! Do you want to continue ? (yes or no)\t";
            cin >> tmp;
            cout << endl;
            if (tmp == "yes")
            {
                Time t1(h1, m1);
                t1.normalize();
                t1.showTime();
                Time t2;
                t2.setHour(h2);
                t2.setMinute(m2);
                t2.normalize();
                t2.showTime();
                if (t1.equals(t2))
                    cout << "Two objects are equals\n";
                else
                    cout << "Two objects are not equals\n";
            }
            else
                break;
        }
        else if (h1 < 0 || h2 < 0 || m1 < 0 || m2 < 0)
        {
            cout << "\nYou have entered incorrect numbers!!";
            break;
        }
        else
        {
            Time t1(h1, m1);
            t1.normalize();
            t1.showTime();
            Time t2;
            t2.setHour(h2);
            t2.setMinute(m2);
            t2.normalize();
            t2.showTime();
            if (t1.equals(t2))
                cout << "Two objects are equals\n";
            else
                cout << "Two objects are not equals\n";
            cout << endl;
        }
    }
    return 0;
}