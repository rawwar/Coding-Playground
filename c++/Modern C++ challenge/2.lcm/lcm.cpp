#include <iostream>


int lcm(int a, int b);
int gcd(int a, int b);

int main(){
    int a,b;
    std::cout << "Please enter number 1: ";
    std::cin >> a;
    std::cout << "Please enter number 2: ";
    std::cin>> b;
    std::cout << "LCM of " << a << " and " << b << " is " << lcm(a,b);
    return 0;
}


int gcd(int a, int b){
    return b==0?a : gcd(b,a%b);
}

int lcm(int a, int b){
    // lcm * gcd = a*b
    // lcm = a*b/gcd(a,b)
    return a*b/gcd(a,b);
}
