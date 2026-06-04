#include<stdio.h>
int main(){
	char escolha;
	int n1,n2;
	printf("ola!,por favor escolha a sua operacao");
	scanf("%c",&escolha);
	if(escolha == '+'){
		printf("escolha dois numeros para somar");
		scanf("%d %d",&n1,&n2);
		printf("a soma eh : %d",n1+n2);
	}
	else if(escolha == '-'){
		printf("escolha dois numeros para subtrair");
		scanf("%d %d",&n1,&n2);
		printf("a soma eh : %d",n1-n2);
	}
	else if(escolha == '*'){
		printf("escolha dois numeros para multiplicar");
		scanf("%d %d",&n1,&n2);
		printf("a soma eh : %d",n1*n2);
	}
	else if(escolha == '/'){
		printf("escolha dois numeros para dividir");
		scanf("%d %d",&n1,&n2);
		printf("a soma eh : %d",n1/n2);
	}
	if (escolha != '+' && escolha!='-' && escolha !='*' && escolha != '/'){
		printf("escolha outro numero");
	}
	printf("o numero correspondente a : %d ",'+');
	return 0;
}