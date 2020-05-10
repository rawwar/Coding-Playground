#include <stdio.h>

int power(int, int);

int main(int argc, char const *argv[]) {
  int n, a;
  long long int b;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d %lld", &a, &b);
    if (b == 0 || b % 4 != 0) {
      b = b % 4;
    } else {
      b = 4;
    }
    printf("%d\n", power((a % 10), b) % 10);
  }
  return 0;
}

int power(int base, int index) {
  int result = 1;
  if (index == 0) {
    return 1;
  }
  for (int i = 0; i < index; i++) {
    result = base * result;
  }
  return result;
}
