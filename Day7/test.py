# n = 0

# display = ""
# guesses = []    
# chosen_word = "lapis"
# while n < 5:
#     guess = input('Digite uma letra: ')

#     guesses += guess

#     print(guesses)
#     n += 1
    

#     for letter in chosen_word:
#         for i in guesses:
#             if i == letter:
#                 display += letter
#             else:
#                 display += "_ "
#     print(display)


palavra = "banana"

guess = input('Letra: ')


if not guess in palavra:
    print('Nao existe essa letra na palavra')
else:
    print('Essa letra esta na palavra')


    