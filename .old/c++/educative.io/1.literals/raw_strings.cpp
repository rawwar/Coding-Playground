#include <iostream> 
using namespace std; 
  
int main() 
{ 
    // A Normal string 
    string string1 = "First. \n Second \t Third\n" ;  
  
    // A Raw string 
    string string2 = R"(First. \n Second \t Third\n)";  
  
    cout << string1 << endl; 
  
    cout << string2 << endl; 
      
    return 0; 
} 