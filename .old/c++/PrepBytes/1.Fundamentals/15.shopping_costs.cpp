#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    int N;
    float  c, q;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> q >> c;
        std::cout << std::fixed;
        cout << std::setprecision(1);
        if (q >100){
            cout << q * c * 0.8 << endl;
        }else{
            cout << q * c << endl;
        }
    }
    
}