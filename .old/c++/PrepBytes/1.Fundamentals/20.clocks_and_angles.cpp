#include <iostream>

using namespace std;

int main(){
    int N, h,m;
    float ha, ma,total;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> h >> m;
        ha =  ((float)h + (float)m/60) *30;
        ma = m*6;
        // cout << ha << "   : " << ma << endl;
        if (ha > ma){
            total = ha - ma;
        }else{
            total = ma - ha;
        }
        if(total >180){
            total = 360 - total;
        }
        cout << total << endl;
    }
    
}