#include <iostream>
using namespace std;
void swap(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
    cout <<"a"<< a <<endl;
};


int main(){

    int a=1;
    int b=2;
    int c =a;
    swap(a,b);
    cout << "a : " << a << " b: " << b << "c:"<<c<<endl;

}