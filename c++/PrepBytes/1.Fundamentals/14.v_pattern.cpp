#include <iostream>

using namespace std;

int main(){

    char n;
    cin >> n;

    for (int i = 1; i <=5; i++)
    {
        for (int j = 1;j <=5; j++){
            if (j<=i){
                cout << j;
            }else{
                cout << " ";
            }
        }
        for (int j = 5;j>0; j--){
            if( j <=i){
                cout << j;
            }else{
                cout << " ";
            }
        }
        cout << endl;
    }
    
}