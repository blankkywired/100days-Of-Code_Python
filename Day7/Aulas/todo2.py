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
print(f"Word chosen: {chose_word}")




placeholder = ""
for i in chose_word:
    placeholder += "_ "
print(placeholder)


correct_letters = []
lifes = 4
game_over = False

while not game_over: #Inverte a condicional par aexecutar o loop
    display = ""
    guess = input('Advinhe uma letra: ')
    print('\n')

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
        game_over = True
        print('You got it!')
        print(f'Congratulations", the chosen word was {chose_word}')




