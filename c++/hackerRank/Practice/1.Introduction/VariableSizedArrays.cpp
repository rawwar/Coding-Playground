#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,q;
    vector<vector<int>> vec;
    cin >> n >> q;
    for (int i=0; i<n; i++){
        int k;
        cin >>k;
        vector<int> temp1 {};
        vec.push_back(temp1);
        for(int ii=0;ii<k;ii++){
            int temp;
            cin >> temp;
            vec.at(i).push_back(temp);
        }
    }
    for (int i=0;i<q;i++){
        int y,yy;
        cin >> y >> yy;
        cout << vec[y][yy] << "\n";
    }
    return 0;
}
