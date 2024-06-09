#ifndef MOBILE_H
#define MOBILE_H
#include <string>

using namespace std;

class mobile
{
private:
    string model;
    string brand;
    string price;
    string resolution;
    string color;

public:
    mobile(string _brand = "Apple", string _model = "iphone 13 pro max", string _price = "1199", string _resolution = "64", string _color = "gold") : brand{_brand}, model{_model}, price{_price}, resolution{_resolution}, color{_color}
    {

    }            // constructor
    ~mobile(){}; // destructor
    // set & get model
    void setModel(string input);
    string getModel() const;
    // set & get brand
    void setBrand(string input);
    string getBrand() const;
    // set & get price
    void setPrice(string input);
    string getPrice() const;
    // set & get resolutoin
    void setResolution(string input);
    string getResolution() const;
    // set & get color
    void setColor(string input);
    string getColor() const;
};

void mobile::setModel(string input)
{
    model = input;
}
string mobile::getModel() const
{
    return model;
}
void mobile::setBrand(string input)
{
    brand = input;
}
string mobile::getBrand() const
{
    return brand;
}
void mobile::setPrice(string input)
{
    price = input;
}
string mobile::getPrice() const
{
    return price;
}
void mobile::setResolution(string input)
{
    resolution = input;
}
string mobile::getResolution() const
{
    return resolution;
}
void mobile::setColor(string input)
{
    color = input;
}
string mobile::getColor() const
{
    return color;
}

#endif