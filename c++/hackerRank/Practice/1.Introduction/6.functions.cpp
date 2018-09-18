#include <iostream>
#include <cstdio>
#include <limits>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/

int max_of_four(int a, int b, int c, int d){
  int max_int = numeric_limits<int>::min();
  if (a > max_int){
        max_int = a;
  }
  if (b > max_int){
      max_int = b;
  }
  if (c > max_int){
      max_int = c;
  }
  if (d > max_int){
      max_int = d;
  }
  return max_int;
}

int main() {
    int a, b, c, d;
    
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
