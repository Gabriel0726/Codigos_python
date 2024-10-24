# Função para verificar se três lados formam um triângulo
def pode_formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Função para determinar o tipo de triângulo
def tipo_triangulo(a, b, c):
    if a == b == c:
        return "EQUILÁTERO"
    elif a == b or b == c or a == c:
        return "ISÓCELES"
    else:
        return "ESCALENO"

# Leitura dos três lados
print("EQUILÁTERO")
lado1 = float(input())
print("ISÓCELES")
lado2 = float(input())
print("ESCALENO")
lado3 = float(input())

# Verificação se pode formar um triângulo
if pode_formar_triangulo(lado1, lado2, lado3):
    tipo = tipo_triangulo(lado1, lado2, lado3)
    print(f"Os números podem formar um triângulo {tipo}.")
else:
    print("Os números não podem formar um triângulo.")
