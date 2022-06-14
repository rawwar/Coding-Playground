#include <iostream>
#include <chrono>

using namespace std;

int main(){
    typedef ratio<5,4> ratio1;
    typedef ratio<2700> ratio2;
    cout << ratio1::num << endl << ratio1::den << endl;
    cout << ratio2::num << endl << ratio2::den << endl;
}