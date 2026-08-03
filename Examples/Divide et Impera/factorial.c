#include<stdio.h>
int factorial(int *n){
    if(*n == 0){
        return 1;
    }
    else{
        int pre = *n-1;
        return *n  * (factorial(&pre));
    }
}
int main(){

    int x;
    scanf("%d",&x);
    printf("Factorial of %d = %d\n", x, factorial(&x));

    return 0;
}
