lista_numero = [5,12,3,8,20,15]
nova_lista = []

for numero in lista_numero:
    if numero % 2 == 0:
        nova_lista.append(numero*2)
    else:
        nova_lista.append(numero//2)
        
print(nova_lista)