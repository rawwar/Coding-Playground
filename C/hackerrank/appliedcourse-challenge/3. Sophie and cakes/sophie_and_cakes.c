#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {

  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  int n, N;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &N);
    printf("%d\n", (int)(N / 2) + 1);
  }
  return 0;
}