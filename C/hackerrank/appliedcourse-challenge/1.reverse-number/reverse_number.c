#include <stdio.h>

#define ll long long

ll int reverse_number(ll int);

int main(int argc, char const *argv[]) {
  ll int n, n1, n2;
  scanf("%lld", &n);
  for (long i = 0; i < n; i++) {
    scanf("%lld %lld", &n1, &n2);
    printf("%lld\n", reverse_number(reverse_number(n1) + reverse_number(n2)));
  }
  return 0;
}

ll int reverse_number(ll int num) {
  ll int rem, result = 0;
  while (num != 0) {
    rem = num % 10;
    result = result * 10 + rem;
    num = num / 10;
  }
  return result;
}