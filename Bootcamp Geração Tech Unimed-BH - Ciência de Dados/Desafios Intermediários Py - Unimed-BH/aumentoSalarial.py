""" 
====================================================
Bootcamp Geração Tech Unimed-BH - Ciência de Dados
====================================================
3/3 - Papagaio Poliglota
====================================================
A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:

--------------------------------------------------
| Salário            | Percentual de Reajuste    |
--------------------------------------------------
| 0 - 600.00         | 17%                       |
--------------------------------------------------
| 600.01 - 900.00    | 13%                       |
--------------------------------------------------
| 900.01 - 1500.00   | 12%                       |
--------------------------------------------------
| 1500.01 - 2000.00  | 10%                       |
--------------------------------------------------
| Acima de 2000.00   | 5%                        |
--------------------------------------------------

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

Exemplo 1
-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 1000               | Novo salario: 1120,00 Reajuste ganho: 120,00 Em percentual: 12 % |
-----------------------------------------------------------------------------------------

Exemplo 2
-----------------------------------------------------------------------------------------
| Exemplo de Entrada |                              Saída                               |
-----------------------------------------------------------------------------------------
| 2000               | Novo salario: 2200,00 Reajuste ganho: 200,00 Em percentual: 10 % |
-----------------------------------------------------------------------------------------

SOLUÇÃO ABAIXO:
"""

salario = int(input()) 
if salario <= 600.00:
  s = salario * 1.17
  r = s - salario
  p = 17
elif salario >= 600.01 and salario <= 900.00:
  s = salario * 1.13
  r = s - salario
  p = 13
elif salario >= 900.01 and salario <= 1500.00:
  s = salario * 1.12
  r = s - salario
  p = 12
elif salario >= 1500.01 and salario <= 2000.00:
  s = salario * 1.10
  r = s - salario
  p = 10
elif salario > 2000.01:
  s = salario * 1.05
  r = s - salario
  p = 5

salString = str(s)
novoSal = salString.split('.')
reString = str(r)
novoRe = reString.split('.')
print(f"Novo salario: {novoSal[0]},00 Reajuste ganho: {novoRe[0]},00 Em percentual: {p} %")