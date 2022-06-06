"""
Loop for

Loop -> Estrutura de repetição 
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop



Ultilizamos loop para iterar sobre sequéncias ou sobre valores iteráveis

Exemplo de iteráveis:
- String
   nome = 'Marcio Costa'
- Lista 
   lista = [1, 3, 5, 7, 9]
- Range
   numeros = tange(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)


# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: o valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10- Não

for numero in range(1, 10):
    print(numero)



Enumerate:
((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'u')...)

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

nome = 'Marcio Costa'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que tranformar em lista


for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe 0 (n)/(qtd) valor: '))
    soma = soma + num
print(f'A soma é (soma)')

nome = 'Marcio Costa'
for letra in nome:
    print(letra, end='')
"""



