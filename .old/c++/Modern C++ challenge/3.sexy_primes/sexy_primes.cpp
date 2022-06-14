#include <iostream>
#include <string>

bool is_prime(int const num);
bool are_sexy_prime(int const a , int const b);

int main(){
    int a,b;
    std::cout << "Please enter number 1: ";
    std::cin >> a;
    std::cout << "Please enter number 2: ";
    std::cin>> b;
    std::string out;
    out = are_sexy_prime(a,b)?"True":"False";
    std::cout <<"are "<< a << " and " << b << " sexy primes? :" << out;
    return 0;
    return 0;
}

bool are_sexy_prime(int const a, int const b){
    return (is_prime(a) && is_prime(b)) ? true:false;
}

bool is_prime(int const num){
        if (num <=1) return false;
        if (num <=3) return true;

        if (num%2==0 || num%3==0) return false;

        for(int i=5;i*i<num; i+=6){
            if(num%i==0 || num%(i+2)==0)
            return false;
        }
        return true;
}

