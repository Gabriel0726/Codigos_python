# Função para verificar se três lados formam um triângulo
def pode_formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Leitura dos três lados
print("3")
lado1 = float(input())
print("4")
lado2 = float(input())
print("5")
lado3 = float(input())

# Verificação e impressão do resultado
if pode_formar_triangulo(lado1, lado2, lado3):
    print("Os números podem formar um triângulo.")
else:
    print("Os números não podem formar um triângulo.")
