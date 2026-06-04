#define MAX 4
int main() {
Fila f; int id = 0;
inicializar(&f);
// Insere 4 pecas (fila fica cheia)
Peca pecas[4] = {{'I',0},{'O',1},{'T',2},{'L',3}};
int i;
for (i = 0; i < 4; i++)
inserir(&f, pecas[i]);
// Remove 2 pecas
retirar(&f);
retirar(&f);
// Insere mais 2
Peca n1={'S',4}; inserir(&f,n1);
Peca n2={'Z',5}; inserir(&f,n2);
printf("inicio=%d fim=%d total=%d\n",
f.inicio, f.fim, f.total);
return 0;
}
