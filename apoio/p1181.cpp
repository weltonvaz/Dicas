#include <iostream>
#include <stdio.h>

int main(){
    int l;
    char t;
    double N[4][4];
    double soma = 0.0;
    
    std::cin >> l;
    std::cin >> t;    
    
    for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                   std::cin >> N[i][j];
                   if(i == l){
                        soma += N[i][j];
                   }
            }
   }
   
   if(t == 'S')
         printf("%.1f\n", soma);
    else
         printf("%.1f\n", soma/4.0);
    return 0;
}
