#include <iostream>

using namespace std;

int main(){
    int N, i,m, count=0;
    cin >> N;
    for (int j = 0; j < N; j++)
    {
        cin >> i >> m;
        if ((m-i) >=2){
            count++;
        }
    }
    cout << count;
    
}