#include <stdio.h>

int main(){
    int N[1000], i, t, n;
    scanf("%d", &t);
    n=0;
    if(t>=2 && t<=50){
    for(i=0;i<1001;i++){
          if(n==t){
            n=0;
        }
          N[i]=n;
          n++;
        }

    for(i=0;i<1000;i++){
        printf("N[%d] = %d\n", i, N[i]);
    }
    }
    return 0;
}
