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
    // Destructor
    ~Time(){};
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

    // check equalities of objects
    friend istream &operator>>(istream &in, Time &t)
    {
        in >> t.hours >> t.minute;
        return in;
    }
    friend ostream &operator<<(ostream &out, Time &t)
    {
        out << setw(2) << setfill('0') << t.hours << ":"
            << setw(2) << setfill('0') << t.minute << t.whenDay() << endl;
        ;
        return out;
    }
    friend bool operator<(const Time &t1, const Time &t2)
    {
        bool b;
        if (t1.hours < t2.hours)
            b = true;
        else if (t1.hours == t2.hours && t1.minute < t2.minute)
            b = true;
        else
            b = false;
        return b;
    }
    friend bool operator<=(const Time &t1, const Time &t2)
    {
        bool b;
        if (t1.hours < t2.hours)
            b = true;
        else if (t1.hours == t2.hours && t1.minute < t2.minute)
            b = true;
        else if (t1.hours == t2.hours && t1.minute == t2.minute)
            b = true;
        else
            b = false;
        return b;
    }
    friend bool operator>(const Time &t2, const Time &t1)
    {
        bool b;
        if (t1.hours < t2.hours)
            b = true;
        else if (t1.hours == t2.hours && t1.minute < t2.minute)
            b = true;
        else
            b = false;
        return b;
    }
    friend bool operator>=(const Time &t2, const Time &t1)
    {
        bool b;
        if (t1.hours < t2.hours)
            b = true;
        else if (t1.hours == t2.hours && t1.minute < t2.minute)
            b = true;
        else if (t1.hours == t2.hours && t1.minute == t2.minute)
            b = true;
        else
            b = false;
        return b;
    }
    Time operator+(const Time &t1)
    {
        Time tmp;
        tmp.hours = hours + t1.hours;
        tmp.minute = minute + t1.minute;
        tmp.normalize();
        return tmp;
    }
    Time operator-(const Time &t1)
    {
        Time tmp;
        tmp.hours = hours - t1.hours;
        tmp.minute = minute - t1.minute;
        tmp.normalize();
        return tmp;
    }
    operator string() const
    {
        string a;
        a = to_string(hours) + ":" + to_string(minute);
        return a;
    }
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
    minute = abs(minute);
    hours = abs(hours);
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
    Time t, t1, t2, t3;
    string a;

    while (1)
    {
        cin >> t;
        cin >> t1;
        cout << a << endl;
        t3 = t1 + t;
        t2 = t1 - t;
        cout << t2;
        cout << t3;
        if (t < t1)
            cout << "koochektar" << endl;
        if (t <= t1)
            cout << "koochektar mosavi" << endl;
        if (t >= t1)
            cout << "bozorgtar mosavi" << endl;
        if (t > t1)
            cout << "bozorgtar" << endl;
        string a;
        a = (string)t3;
        cout << a << endl;
    }

    return 0;
}