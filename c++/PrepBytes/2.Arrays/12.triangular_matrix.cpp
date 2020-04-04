#include <iostream>

using namespace std;

int main(){
    int M, N;
    cin >> M >> N;

    int arr[M][N];
    
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> arr[i][j];
        }
        
    }

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(i<j){
                cout << 0 << " ";
            }else{
                cout << arr[i][j] << " ";
            }
        }
        cout << endl;
        
    }
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if(i>j){
                cout << 0 << " ";
            }else{
                cout << arr[i][j] << " ";
            }
        }
        cout << endl;
        
    }
    
    
}