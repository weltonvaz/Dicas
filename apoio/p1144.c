#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,i,a=0;
    scanf("%d",&n);
    for(i=1;i<=n;i++){
                     printf("%d ",i);
                     a=i*i;
                     printf("%d ",a);
                     a=0;
                     b=i*i*i;
                     printf("%d \n",a);
                     a=0;                     
                     printf("%d ",i);
                     c=i*i+1;
                     printf("%d ",a);
                     a=0;
                     d=i*i*i+1;
                     printf("%d \n",a);
                     a=0;
                     }         
  
  system("PAUSE");   
  return 0;
}
