#include <stdio.h>

int main(int argc, char const *argv[]) {
  long n;
  scanf("%ld", &n);
  for (long i = 1;; i++) {
    n -= i;
    if (n <= 0) {
      printf("Ramesh");
      break;
    }
    n -= 2 * i;
    if (n <= 0) {
      printf("Suresh");
      break;
    }
  }

  return 0;
}
