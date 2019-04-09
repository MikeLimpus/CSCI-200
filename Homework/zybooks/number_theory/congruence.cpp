#include <stdio.h> 

int main(void) {
    int a = 11;
    int b = 4;
    int m = 3;

    if(a == b % m) { 
        printf("True\n");
    }
    else {
        printf("False\n"); 
    }
}