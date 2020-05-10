#include <iostream>

using namespace std;

int factors(int);
int factor_pairs(int);

int main(){
    int N, n;
    cin >> N;
    
    for (int i = 0; i < N; i++)
    {

        cin >> n;
        int count = 0;
        for (int k = 2; k <= n; k++)
        {
            while(n%k ==0 ){
                count+=k;
                n = n/k;
            }
        }
        cout << count << endl;
        


    }
    

}
