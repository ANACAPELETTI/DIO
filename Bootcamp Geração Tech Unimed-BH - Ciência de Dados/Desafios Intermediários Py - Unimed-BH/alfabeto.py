""" 
====================================================
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
====================================================
1/3 - Alfabeto
====================================================
Dada a letra N do alfabeto, nos diga qual a sua posição.
Entrada
Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
Saída
Um único inteiro, que representa a posição da letra no alfabeto.
--------------------------------------------
| Exemplo de Entrada | Exemplo de Saída    |
--------------------------------------------
| C                  | 3                   |
--------------------------------------------
| J                  | 10                  |
--------------------------------------------
| Z                  | 26                  |
--------------------------------------------
| A                  | 1                   |
--------------------------------------------
SOLUÇÃO ABAIXO:
"""
letra = input() 
num = 0
soma = 0
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;
num = ord(letra)
for i in range(65,91):
  soma = soma + 1
  if i == num:
    print(soma)
    break