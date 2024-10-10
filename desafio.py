
valor_bonus = 1000
nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salario: "))
bonus = float(1.5)

valor_final = valor_bonus + salario * bonus

print(f"O usuario: {nome} possui o bonus de {valor_final}")