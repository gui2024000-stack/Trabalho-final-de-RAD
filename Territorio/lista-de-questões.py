'''Abaixo vai a lista de questões, eu decidi separar por comentários para facilitar na hora dos testes'''


''' Q1
nome = "Gui"
idade = 19
altura = 1.82
print(f"seu nome é:{nome}, sua idade é:{idade} e sua altura é:{altura}")
'''


'''Q2
n1 = int(input("informe um número: "))
n2= int(input("informe outro número: "))
soma = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
print(f"A soma dos números é: {soma}, a subtração dos números é: {sub}, a multiplicação dos números é: {mult}, a divisão dos números é: {div}")
'''


'''Q3
idade = int(input("informe sua idade: "))
if(idade>=18):
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")
'''


'''Q4
for i in range(1,11):
    print(i)
'''


'''Q5
frutas = ['uva','banana','maçã','pera']
for fruta in frutas:
    print(fruta)
'''


'''Q6
n1 = int(input("informe um número: "))
n2= int(input("informe outro número: "))
soma = n1+n2
print(f"A soma destes números é: {soma}")
'''


'''Q7
pessoa = {
    "nome": "Guilherme",
    "idade": "19",
    "cidade": "Olhoa D'água"
}
print(pessoa)
'''


'''Q8
frase = input("Digite uma frase: ")
print(frase.upper())
print(frase.lower())
print(frase.title())
'''


'''Q9
texto = input("Informe o que quer escrever: ")
with open("texto.txt","w") as arquivo:
    arquivo.write(texto)
with open("texto.txt","r") as arquivo:
    conteudo = arquivo.read()
palavras = conteudo.split()
quantidade = len(palavras)
print("o arquivo tem",quantidade,"palavras")
'''


'''Q10
for x in range(1,11):
    print(x**2)
'''


'''Q11
n1 = int(input("informe um número: "))
n2= int(input("informe outro número: "))
if(n2 == 0):
    while(n2 == 0):
        print("Escolha um número válido")
        n2= int(input("informe outro número: "))
div = n1/n2
print("O resultado da divisão é:",div)
'''


'''Q12
escolha = int(input("escolha 1 para Celsius ou 2 para Fahreinheit para ver a conversão: "))
graus= int(input("informe a quantidade de graus: "))
C = (graus*9/5)+32
F = (graus - 32)*5/9
if(escolha == 1):
    print(graus,"Graus Celsius Convertido para Fahreinheit é: ",C)
else:
    print(graus,"Graus Fahreinheit covertido para Celsius é: ",F)
'''


'''Q13
num = int(input("Informe qual o termo da sequência fibonnaci quer saber: "))
if(num == 1):
    print(0)
elif(num == 2):
    print(1)
else:
    n1 = 0
    n2 = 1
    for _ in range(3,num+1):
        n3 = n1+n2
        n1 = n2
        n2 = n3
    print(n3)
'''


'''Q14
def eh_palindromo(texto):
    texto = texto.lower()
    texto = ''.join(c for c in texto if c.isalnum())

    return texto == texto[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
'''


'''Q15
frase = input("Informe o que quer escrever: ")
with open("palavras.txt","w") as arquivo:
    arquivo.write(frase)
with open("palavras.txt","r") as arquivo:
    conteudo = arquivo.read()
palavras = conteudo.split()
quantidade = len(palavras)
print("o arquivo tem",quantidade,"palavras")
'''


'''Q16
lista_num = [1,10,24,65,789,987,1234]
for i in range(len(lista_num)):
    for k in range(0,len(lista_num)- i -1):
        if lista_num[k]> lista_num[k+1]:
            corr = lista_num[k]
            lista_num[k] = lista_num[k+1]
            lista_num[k + 1] = corr
print(lista_num)
'''