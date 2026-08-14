# Desafio 1
telefone = input("Digite o telefone: ")

ddd = telefone[1:3]
numero = telefone[4:]

print("DDD:", ddd)
print("Número:", numero)


# Desafio 2
data = input("Digite sua data de nascimento: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)


# Desafio 3
email = input("Digite seu e-mail: ")

primeiro_nome = email[0:email.index(".")]
dominio = email[email.index("@") + 1:]

print("Primeiro nome:", primeiro_nome)
print("Domínio:", dominio)
