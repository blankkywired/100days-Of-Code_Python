import random

escolhaUsuario = int(input('Escolha 0 para Pedra, 1 para Papel e 2 para tesoura\n'))

computador = random.randint(0,2)
#usuario
print('Voce')
if escolhaUsuario == 0:
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

elif escolhaUsuario == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)


elif escolhaUsuario == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

#Computador
print('Computador')
if computador == 0:
    print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
elif computador == 1:
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computador == 2:
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if escolhaUsuario == computador:
    print('Empate')

elif escolhaUsuario == 0 and computador == 1: #pedra vs papel
    print('Derrota')

elif escolhaUsuario == 0 and computador == 2:  #pedra vs tesoura
    print('Vitoria')

elif escolhaUsuario == 1 and computador == 0: #Papel vs pedra
    print('Vitoria')

elif escolhaUsuario == 1 and computador == 2: #Papel vs tesoura
    print('Derrota')

elif escolhaUsuario == 2 and computador == 1: #tesoura vs papel
    print('Vitoria')
elif escolhaUsuario == 2 and computador == 0: #tesoura vs pedra
    print('Derrota')



