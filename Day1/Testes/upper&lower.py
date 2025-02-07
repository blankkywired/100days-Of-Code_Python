
contador = 0

while contador < 5:
    nomes = input('Digite um nome:\n')
    contador = contador + 1

    if nomes.islower():   # Se nomes.islower() for verdadeiro
        print('Minusculas')
    else: # Se nome.islower() for falso
        print('Maiuscula')

