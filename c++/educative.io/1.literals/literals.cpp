#include <iostream>

int main(int argc, char const *argv[])
{
    int unsigned_int = u'U';
    int hex = 0x2a;
    std::string raw = R"(Raw String)";
    int octalBase = 0123;

    std::cout << unsigned_int << "," << hex << "," << raw << std::endl << octalBase <<  std::endl;
    return 0;
}
