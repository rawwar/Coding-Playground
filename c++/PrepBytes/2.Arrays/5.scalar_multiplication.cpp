#include <iostream>

using namespace std;

int main(){
    int M,N,K;
    cin >> M >> N >> K;
    int arr[M][N];
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr[i][j];
            arr[i][j] *=K;
        }
        
    }

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout <<  arr[i][j] << " ";
        }
        cout << endl;
        
    }

    
    
}