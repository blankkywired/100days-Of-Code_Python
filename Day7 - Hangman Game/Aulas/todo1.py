import random
word_list = ["lapis", "mochila", "Caderno"]

choosen_word = random.choice(word_list)
print("Palavra escolhida: " , choosen_word)


guess = input('Advinhe uma letra da palavra: ').lower() #Atribuir uma letra qualquer advinhada pelo usuario
 #Transformar a  letra advinhada pelo usuario em letra minuscula


print(guess)



#Para cada letra da palavra escolhida, ira verificar se essa letra no loop é igual a letra
# adivinhada pelo o usuario
for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    