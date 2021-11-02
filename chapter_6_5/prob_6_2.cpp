using namespace std;

constexpr double pi() { return std::atan(1.0) * 4.0; }

class Shape {
    public:
        Shape();
        virtual double area() = 0;
        virtual double circ() = 0;
}

class Circle: public Shape {
    public:
        Circle (double radius); 
    private:
        double _radius;
}
Circle::Circle(double radius) {
    _radius = radius;
}
Circle::area(){
    return pi * _radius * _radius;
}
Circle::circ(){
    return pi * _radius * 2.0;
}

class Rectangle: public Shape {
    public:
        Rectangle (double, double);
    private:
        double _width, _height;
}
Rectangle::Rectangle(double width, double height) {
    _width = width;
    _height = height;
}
Rectangle::area(){
    return _width * _height;
}
Rectangle::circ(){
    return 2.0 * _width * _height;
}

class Square: public Rectangle {
    public:
        Square (double);
}

Square::Square(double size){
    _width = size;
    _height = size;
}

/* ## haskell implementation of Square: */
/* data Shape = Circle Float | Rect Float Float | Square Float */
/* area (Square s) = s * s */
/* circ (Square s) = s * 4.0 */
