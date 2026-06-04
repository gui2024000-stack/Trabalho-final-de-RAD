#include<stdio.h>
int main(){
	int i,a,b,c;
	a = 0;
	b = 1;
	for(i=1;i<=30;i++){
		printf("%d ",a);
		c = a + b;         
        a = b;             
        b = c;

	}
	return 0;
}