#include <stdio.h>

int main(int argc, char const *argv[]) {
  int N, sh, sm, eh, em;
  scanf("%d", &N);
  for (int i = 0; i < N; i++) {
    scanf("%d %d %d %d", &sh, &sm, &eh, &em);
    int total_time = eh * 60 + em - sh * 60 - sm;

    printf("%d %d", (int)total_time / 60, total_time % 60);
  }
  return 0;
}
