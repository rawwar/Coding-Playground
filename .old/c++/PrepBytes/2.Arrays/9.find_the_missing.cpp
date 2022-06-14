#include <iostream>

using namespace std;

int main(){
    int N;
    long long size;
    long long temp;

    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> size;
        long long sum = 0;
        for (long long j = 0; j < size-1; j++)
        {
            cin >> temp;
            sum += temp;
        }
        cout << (size*(size+1)/2) - sum << endl;
        
    }
    
}