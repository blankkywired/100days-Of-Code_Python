#Soma
# Crie uma função chamada soma 
# que recebe dois números como parâmetros e retorna a soma deles.
def soma(numero1, numero2):
    print(numero1 + numero2)

# soma(1, 2)



#Par ou impar
# Crie uma função chamada par_ou_impar que recebe 
# um número inteiro como parâmetro e imprime se o número é "par" ou "ímpar".
def checador(numero):
    if numero % 2 == 0:
        print('Par')
    else:
        print('Impar')

# checador(6)




# Crie uma função chamada maior_numero 
# que recebe dois números como parâmetros e retorna o maior deles.

def maiorNum(numero1, numero2):
    if numero1 > numero2:
        print(f'O maior numero é: {numero1}')
    else:
        print(f'O maior numero é {numero2}')

# maiorNum(10, 3)



# Crie uma função chamada eh_primo que recebe um número inteiro 
# como parâmetro e retorna True se o número for primo, caso contrário, retorna False.

def num_primo(numero):
    if numero / 1 == numero and numero / numero == 1:
        print("PRIMO")
    else:
        print("NÂO PRIMO")

# num_primo(6)


def numeroPrimo(numero):
    if numero / 1 == numero and numero / numero == 1:
        return True
    else:
        return False
        
print(numeroPrimo(5))