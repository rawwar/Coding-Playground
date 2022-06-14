#include <stdio.h>

int main() {
    float n1,n2,n3,max;
    printf("Enter first number : ");
    scanf("%f", &n1);
    printf("\nEnter second number : ");
    scanf("%f", &n2);
    printf("\nEnter third number : ");
    scanf("%f", &n3);
    max = (n1 > n2) ? (n1 > n3 ? n1 : n3) : (n2 > n3 ? n2 : n3);
    printf("Max number is %.2f",max);
    return 0;
}