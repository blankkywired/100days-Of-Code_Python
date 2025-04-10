import draw
import os

print(draw.simbol)

start_code = True

data_base = {

}
while start_code:
    name_user = input('What is your name?: ').lower()
    bid_user = int(input('What is your bid?: $'))
    bidders_question = input("Are there any other bidders?: Type 'yes' or 'no'.\n").lower()

    data_base[name_user] = bid_user

    if bidders_question == "no":
        start_code = False

    #Limpar a tela do usuario no terminal
    elif bidders_question == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') #Rodar codigo no terminal powershell pelo pycharm


for user in data_base:
    print(f'{user}: ${data_base[user]}')
