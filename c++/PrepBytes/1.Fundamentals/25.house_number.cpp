#include <iostream>
using namespace std;

int main(){
    int N,x, digits;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        digits = 0;
        cin >> x;
        for (int i = 1; i <= x; i *= 10) {
        digits += (x - i + 1); 
        }

        cout << digits << endl;
    }

    
}