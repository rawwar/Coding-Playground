#include <iostream>

int main(int argc, char const *argv[])
{
    char code;
    std::cin >> code;

    switch (code)
    {
    case 'P':
    case 'p':
        std::cout << "PrepBytes";
        break;
    case 'Z':
    case 'z':
        std::cout << "Zenith";
        break;
    case 'E':
    case 'e':
        std::cout << "Expert Coder";
        break;
    case 'D':
    case 'd':
        std::cout << "Data Structure";
        break;
    default:
        break;
    } 
    return 0;
}
