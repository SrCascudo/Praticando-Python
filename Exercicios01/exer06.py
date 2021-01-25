somatorio = 0
media = 0.0

qtd_fator = int(input("Deseja tirar a média de quantos valores? "))
for i in range(0, qtd_fator):
    somatorio += int(input("Digite um valor para adicionar a Média: "))

media = (somatorio / qtd_fator)
print("A média dos valores informados foi de: {}".format(media))
