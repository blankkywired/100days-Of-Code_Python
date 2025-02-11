import random

word_list = [
    "lapis",
    "caneta",
    "borracha",
    "caderno",
    "estojo",
    "mochila",
    "regua",
    "tesoura",
    "cola",
    "apontador",
    "livro",
    "marcador",
    "papelsulfite"
]

chose_word = random.choice(word_list)
# print(f"Word chosen: {chose_word}")



placeholder = ""
for i in chose_word:
    placeholder += "_ "
print(placeholder)


correct_letters = []   # Onde Todas as letras/palpites certos do usuario serao colocadas 
lifes = 4
game_over = False

while lifes > 0: #Inverte a condicional para executar o loop
    display = ""    #Display dentro do loop para nao acumular os respectivos valores que o usuario atribuir
    guess = input('Guess a letter: ')
    if guess in chose_word:
        continue
    else:
        lifes -= 1
    for letter in chose_word:
        if letter == guess:
            correct_letters.append(guess)
            display += letter + ""

        elif letter in correct_letters:
            display += letter + ""
            
        else:
            display +=  " _ "

    print(display)
    print('\n')




#Verifica se ainda contem letras ocultar/ nao advinhada pelo usuario na palavra escolhida
    if not "_" in display:
        print('You got it!')
        print(f'Congratulations", the chosen word was {chose_word}')

    elif lifes == 0:
        print('You lose!')




