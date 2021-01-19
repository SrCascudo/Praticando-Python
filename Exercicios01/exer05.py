qtd_operadores = int(input('Quantos números deseja somar em sequência? '))
valor = int
while qtd_operadores >= 0:
    valor += int(input('Informe o valor '))
    qtd_operadores -= 1

print('A soma dos valores foi {}'.format(valor))
