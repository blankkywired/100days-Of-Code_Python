nomes = ['Jack', 'Louis', 'Mary', 'Afrodite']

n = input('Digite o nome que deseja buscar na lista: ')

if n in nomes:
# Se o nome que o usuario busca estiver na lista de nomes entao ira retornar a mensagem
    print(f'O nome {n} esta na lista de nomes')

else:
    print(f"O nome {n} não se encontra na lista de nomes")

