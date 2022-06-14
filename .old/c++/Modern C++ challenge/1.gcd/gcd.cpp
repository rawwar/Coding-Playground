#include<iostream>

using namespace std;

int gcd(int int1, int int2);

int main(){
    int a,b;
    cout << "Please enter number 1: ";
    cin >> a;
    cout << "Please enter number 2: ";
    cin>> b;
    cout << "GCD of " << a << " and " << b << " is " << gcd(a,b);
    return 0;
}


int gcd(int int1, int int2){
    return int2 ==0?int1 : gcd(int2, int1%int2);
}

