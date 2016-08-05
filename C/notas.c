/*
 *  Coded by: Iago Roger
 */

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    float n_max, notas[4];
    printf("Informe a nota da primeira unidade: ");
    scanf("%f", &notas[1]);
    printf("Informe a nota da segunda unidade: ");
    scanf("%f", &notas[2]);
    printf("Informe a nota da terceira unidade: ");
    scanf("%f", &notas[3]);
    printf("Informe a nota da quarta e ultima unidade: ");
    scanf("%f", &notas[4]);
    n_max = notas[1] + notas[2] + notas[3] + notas[4];
    if(n_max >= 24) {
        printf("O aluno passou com %2.f pontos na materia\n", n_max);
    } else {
        printf("O aluno perdeu com %2.f pontos na materia e precisa de %2.f para passar\n", n_max, n_max - 24);
    }
}
