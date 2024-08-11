class point
{
private:
    int x, y;

public:
    point()
    {
        x = 0;
        y = 0;
    }
    point(int tool, int arz)
    {
        x = tool;
        y = arz;
    }
    void setX(int tool);
    void setY(int arz);
    void setAll(int tool, int arz);
    int getX();
    int getY();
    int lengh();
    void showPoint();
};