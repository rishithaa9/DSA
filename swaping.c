#include <stdio.h>
int x,y;
int a,b;

void swapByValue(int a,int b) {
   int temp=a;
   a=b;
   b=temp;
   }

   int main() {
      int x=5;y=10;
      printf("Before swap; x=%d\n",x,y);
      swapByReference(&x,&y);
      printf("Afterswap(call by reference);x=%d;y=%d\n",x,y);
      return 0;
}