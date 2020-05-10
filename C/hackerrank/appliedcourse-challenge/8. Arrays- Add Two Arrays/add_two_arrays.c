#include <stdio.h>

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    int len;
    scanf("%d", &len);
    int arr1[len], arr2[len];
    for (int j = 0; j < len; j++) {
      scanf("%d", &arr1[j]);
    }
    for (int j = 0; j < len; j++) {
      scanf("%d", &arr2[j]);
    }
    for (int j = 0; j < len; j++) {
      printf("%d ", arr1[j] + arr2[j]);
    }
    printf("\n");
  }

  return 0;
}
