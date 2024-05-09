# EXERCICIO 1 - Usando um loop for e a função range() para gerar os números pares de 2 a 20
for num in range(2, 21, 2):
    print(num)


# EXERCICIO 2 - Usando um loop for e a função range() para gerar os múltiplos de 5 em 5 até 50
for num in range(5, 51, 5):
    print(num)



# EXERCICIO 3 - Definindo uma variável
x = 10

# Verificando o tipo da variável usando a função type()
tipo_de_x = type(x)

# Imprimindo o tipo da variável
print("O tipo de x é:", tipo_de_x)


# EXERCICIO 4 - Solicita ao usuário que insira seu nome
nome_usuario = input("Digite o seu nome: ")

# Imprime uma mensagem de saudação personalizada
print("Olá,", nome_usuario + "! Bem-vindo!")


# EXERCICIO 5 - Inicializa a soma e a contagem de números ímpares
soma = 0
contagem = 0

# Itera sobre os números ímpares de 1 a 10 usando a função range()
for num in range(1, 11, 2):
    soma += num  # Adiciona o número à soma
    contagem += 1  # Incrementa a contagem

# Calcula a média
media = soma / contagem

# Imprime a média
print("A média dos números ímpares de 1 a 10 é:", media)


# EXERCICIO 6 - Gerar números ímpares de 1 a 10
numeros_impares = [i for i in range(1, 11, 2)]

# Calcular a média dos números ímpares
soma = sum(numeros_impares)
media = soma / len(numeros_impares)

# Encontrar o máximo e o mínimo
maximo = max(numeros_impares)
minimo = min(numeros_impares)

# Imprimir a média, máximo e mínimo
print("A média dos números ímpares de 1 a 10 é:", media)
print("O máximo dos números ímpares é:", maximo)
print("O mínimo dos números ímpares é:", minimo)


# EXERCICIO 7
lista = [10, 56, 40, 5, 4, 9, 7, 1, 0, 56]
lista_ordenada = sorted(lista)
print("Lista ordenada:", lista_ordenada)



# EXERCICIO 8
lista = [10, 56, 40, 5, 4, 9, 7, 1, 0, 56]
lista_ordenada = sorted(lista)

soma = sum(lista_ordenada)
print("A soma de todos os valores da lista ordenada é:", soma)

