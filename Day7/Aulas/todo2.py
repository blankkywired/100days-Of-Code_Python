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
    if i == " ":  #verifica se a palavra contem espaços
        placeholder += "   "
    else:
        placeholder += "_ "
print(placeholder)


display = ""
letters_guessed = []
lifes = 4

display = ""
while lifes > 0:
    guess = input("Advinhe uma letra: ").lower()

    if guess in letters_guessed:
        print('Letra ja advinhada anteriormente')
        continue    
    
    letters_guessed.append(guess)

    for letter in chose_word:
        if letter == guess:
            display += letter
        else:
            display += "_ "




    if not guess in chose_word:
        lifes -= 1

        







