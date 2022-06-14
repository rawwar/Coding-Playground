
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int N, power, good_number;
    long long int n;
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> n;
        vector<int> value;
        int pos2 = -1;
        while (n>0){
            value.push_back(n%3);
            if(value.back() == 2){
                pos2 = int(value.size()) -1;
                
            }
            n /= 3;
        }
        value.push_back(0);

        if(pos2 != -1){
            int pos0 = find(value.begin()+pos2, value.end(), 0) - value.begin();
            value[pos0] = 1;
            for(int i = pos0-1; i>=0; --i){
                value[i] = 0;
            }
        }
        long long ans = 0;
        long long pw = 1;
        for (int i = 0; i < int(value.size()); i++)
        {
            ans += pw*value[i];
            pw *= 3;
        }
        if(value.back() ==1){
            ans = pw/3;
        }

        cout << ans << endl;
        

    }
    return 0;
}
