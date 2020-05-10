#include <stdio.h>

int main(int argc, char const *argv[]) {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    long len, key;
    scanf("%ld %ld", &len, &key);
    long arr[len];
    long lowest, temp;
    scanf("%ld", &lowest);
    for (int j = 0; j < len - 1; j++) {
      scanf("%ld", &temp);
      if (temp < lowest) {
        lowest = temp;
      }
    }
    printf("%ld\n", key - lowest);
  }

  return 0;
}
