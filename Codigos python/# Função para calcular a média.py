# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Leitura dos dados do aluno
nome = input("Gabriel Teixeira Ramos")
nota1 = float(input("9"))
nota2 = float(input("6"))
nota3 = float(input("10"))
faltas = int(input("3 "))

# Cálculo da média
notas = [9, 6, 10]
media = calcular_media(notas)

# Verificação da situação do aluno
if faltas > 10:
    situacao = "REPROVADO POR FALTA"
elif media < 7.0:
    situacao = "REPROVADO POR MÉDIA"
else:
    situacao = "APROVADO"

# Impressão da situação do aluno
print(f"{nome}, sua situação é: {situacao}")
