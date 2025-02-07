"""
Estrutura:
while <condicao for verdadeira>:
    faça algo

"""
# x = 1
# while x <= 3:  # Enquanto a condição for verdadeira, faça algo
#     x += 1
#     print('Hello')
#Vai mostrar hello enquanto x for menor ou igual a 3
#para cada vez que mostrar hello ira adicionar + 1 para x




# valorUser = int(input('Digite um valor numerico: '))

# while valorUser < 10:
#     valorUser = int(input('Digite um valor numerico: '))



#AUTENTICADOR DE SENHAS
password = str(57482)

user_pass = input('Digite sua senha: ')

lives = 4
while lives > 0:
    
    if user_pass.isnumeric():
        if user_pass == password:
            print('Login efetuado com sucesso')
            break
        else:
            user_pass = input('Digite sua senha novamente: ')
            lives -= 1
    else:
        print('A senha deve conter somente valores numericos')
        lives -= 1



