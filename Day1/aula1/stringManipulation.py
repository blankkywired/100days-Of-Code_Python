# Manipulação de Strings

#Concatenação
nome = "Guilherme"
sobrenome = "Abreu"

print(nome + sobrenome) #Juntou as duas strings das variaveis nome e sobrenome sem separar por espaços

print(nome + " " + sobrenome) # Uniu duas strings e separou com espaço entre elas

# F - Strings
# Une o valor de multiplas variaveis dentro de uma string sem precisar concatenar

print(f' O nome do usuario é : {nome} e o seu sobrenome é: {sobrenome}')

print(f' O nome do usuario é :\n{nome}\n e o seu sobrenome é:\n{sobrenome}') #\n para quebrar uma linha

#Upper & Lower

usuario1 = 'Edgar'
usuario2 = 'Roberta'
print(usuario1.lower()) #Minusculo
print(usuario2.upper())  #Maiusculo

#Repetição de simbolos e caracteres
print(5 * 'X') # Repete a letra X 5 vezes
print(2 * ' Hello World!') # Repete a frase Hello world 3 vezes

