#include <iostream>

int main(int argc, char const *argv[])
{
    int x;
    std::cin >> x;
    int sum=0;
    while ( x>0){
        sum += x%10;
        x = x/10;
    }
    std::cout << sum;
    return 0;
}