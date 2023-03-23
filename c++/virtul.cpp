#include <iostream>
using namespace std;
int main(int argc, char const *argv[])
{
    class base{
        public:
            virtual void vir_func(){cout<<"virtual function, class base"<<endl;}
            void func(){cout<<"normal function, class base"<<endl;}


    };
    class A:public base{
        public:
            virtual void vir_func(){
                cout <<"virtual function, class A"<<endl;
            }
            void func(){cout <<"normal function, class A"<<endl;}

    };
    class B: public base{
        public:
            virtual void vir_func(){
                cout <<"virtual function, class B"<<endl;
            }
            void func(){cout <<"normal function, class B"<<endl;}
    };

    base *Base = new(base);
    A * a = new(A);
    B * b = new(B);
    Base->vir_func();
    a->vir_func();
    b->vir_func();
    Base->func();
    a->func();
    b->func();
}