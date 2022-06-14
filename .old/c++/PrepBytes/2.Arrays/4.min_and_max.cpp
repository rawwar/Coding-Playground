#include <iostream>

using namespace std;

int main(){
    int N;
    int size;
    int lowest;
    int highest;
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> size;
        int arr[size];
        for (int j = 0; j < size; j++)
        {
            cin >> arr[j];
        }
        lowest = highest = arr[0];
        
        for (int j = 0; j < size; j++)
        {
            if(arr[j] < lowest){
                lowest = arr[j];
            }
            if(arr[j]> highest){
                highest = arr[j];
            }
        }
        
        cout << lowest << " " << highest << endl;
        
    }
    
}