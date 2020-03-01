#include <stdio.h>

long lcm(long, long, long);
long gcd(long, long);

int main(int argc, char const *argv[]) {
  long N, n1, n2;
  scanf("%d", &N);
  for (long i = 0; i < N; i++) {
    scanf("%ld %ld", &n1, &n2);
    long _gcd = gcd(n1, n2);
    printf("%ld %ld\n", _gcd, lcm(n1, n2, _gcd));
  }

  return 0;
}

long gcd(long a, long b) {
  if (b == 0) {
    return a;
  } else {
    return gcd(b, a % b);
  }
}

long lcm(long a, long b, long _gcd) { return (a * b) / _gcd; }