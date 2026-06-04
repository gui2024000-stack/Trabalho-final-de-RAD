#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

typedef struct{
    char nome[30];
    char cor[10];
    int tropas;
} Torio;

// BATALHA (apenas 1 rodada)
void atacar(Torio* atacante, Torio* defensor){
    int ataque = rand() % 6 + 1;
    int defesa = rand() % 6 + 1;

    printf("\n%s ataca %s!\n", atacante->nome, defensor->nome);
    printf("Dado do atacante: %d\n", ataque);
    printf("Dado do defensor: %d\n", defesa);

    if(ataque > defesa){
        printf("%s conquistou %s!\n", atacante->nome, defensor->nome);

        // Transfere tropas
        atacante->tropas += defensor->tropas;

        // Muda cor (domínio)
        strcpy(defensor->cor, atacante->cor);

        // Zera tropas do defensor
        defensor->tropas = 0;

    } else {
        printf("%s perdeu a batalha!\n", atacante->nome);

        atacante->tropas -= 1;
        if(atacante->tropas < 0)
            atacante->tropas = 0;
    }

    printf("Tropas: %s=%d | %s=%d\n",
           atacante->nome, atacante->tropas,
           defensor->nome, defensor->tropas);
}

// Cadastro
void cadastro(Torio* p, int n){
    int i;
    for(i = 0; i < n; i++){
        printf("Informe o nome do Territorio: ");
        scanf("%s", p[i].nome);

        printf("Informe a cor do Territorio: ");
        scanf("%s", p[i].cor);

        printf("Informe a quantidade de tropas: ");
        scanf("%d", &p[i].tropas);

        system("cls"); 
    }
}

// Loop do jogo
void war(Torio* p, int n, Torio* jogador){
    int atacante, defensor;

    while(1){
        printf("\n--- ESTADO ATUAL ---\n");

        int i;
        for(i = 0; i < n; i++){
            printf("%d - %s | Cor: %s | Tropas: %d\n",
                   i+1, p[i].nome, p[i].cor, p[i].tropas);
        }

        // Se jogador perdeu seu território
        if(jogador->tropas == 0){
            printf("\nVocê perdeu seu território!\n");
            break;
        }

        // Contar territórios vivos
        int vivos = 0;
        int ultimo = -1;

        for(i = 0; i < n; i++){
            if(p[i].tropas > 0){
                vivos++;
                ultimo = i;
            }
        }

        // Vitória final
        if(vivos == 1){
            if(&p[ultimo] == jogador)
                printf("\nVocê venceu o jogo!\n");
            else
                printf("\nVocê perdeu o jogo!\n");
            break;
        }

        printf("\nEscolha o territorio ATACANTE: ");
        scanf("%d", &atacante);

        printf("Escolha o territorio DEFENSOR: ");
        scanf("%d", &defensor);

        // Validação
        if(atacante < 1 || atacante > n ||
           defensor < 1 || defensor > n ||
           atacante == defensor ||
           p[atacante-1].tropas == 0 ||
           p[defensor-1].tropas == 0){

            printf("Escolha inválida!\n");
            continue;
        }

        atacar(&p[atacante - 1], &p[defensor - 1]);
    }
}

int main(){
    srand(time(NULL));

    int n, escolha;

    printf("Informe a quantidade de territorios: ");
    scanf("%d", &n);

    Torio* p = (Torio*) malloc(n * sizeof(Torio));

    cadastro(p, n);

    // Mostrar territórios
    int i;
    for(i = 0; i < n; i++){
        printf("\nTerritorio %d:\n", i+1);
        printf("Nome: %s\n", p[i].nome);
        printf("Cor: %s\n", p[i].cor);
        printf("Tropas: %d\n", p[i].tropas);
    }

    printf("\nEscolha seu Territorio (1 a %d): ", n);
    scanf("%d", &escolha);

    if(escolha < 1 || escolha > n){
        printf("Escolha inválida!\n");
        free(p);
        return 1;
    }

    Torio* jogador = &p[escolha - 1];

    printf("\nVoce escolheu:\n");
    printf("Nome: %s\n", jogador->nome);
    printf("Cor: %s\n", jogador->cor);
    printf("Tropas: %d\n", jogador->tropas);

    system("cls"); // ou "clear"

    war(p, n, jogador);

    free(p);
    return 0;
}