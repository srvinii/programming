#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){

  int a, b, c, resultado, raiz1, raiz2, raizdelta;

	printf("Digite o valor de a: ");
	scanf("%d", &a);

	printf("Digite o valor de b: ");
	scanf("%d", &b);

	printf("Digite o valor de c: ");
	scanf("%d", &c);
	
	printf("\n\n");

  resultado = (b * b) - 4 * a * c;

	printf("############################################\n");
	printf("##        Valor de delta: %d               ##", resultado);
	printf("\n");
	printf("############################################");
	printf("\n\n");
  
  raizdelta = sqrt(resultado);

  raiz1 = -(b) + raizdelta;
  raiz1 = raiz1 / (2 * a);

  raiz2 = -(b) - raizdelta;
  raiz2 = raiz2 / (2 * a);
  
  if (resultado < 0){
	printf("\n\n Nao possui raizes reais");
	printf("\n");
	getchar();
	return 0;
  }
  
  printf("############################################\n");
  printf("##                x' = %i", raiz1);
  printf("                  ##\n");
  printf("############################################\n");
  printf("##                x'' = %i", raiz2);
  printf("                 ##\n");
  printf("############################################\n");
  

  getchar();
  return 0;
}
