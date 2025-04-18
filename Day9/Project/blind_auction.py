import draw
import os

print(draw.simbol)

start_code = True

data_base = {

}

def most_expensive():

while start_code:
    name_user = input('What is your name?: ')
    bid_user = int(input('What is your bid?: $'))
    bidders_question = input("Are there any other bidders?: Type 'yes' or 'no'.\n").lower()

    #Adding name and bid in the dict
    data_base[name_user] = bid_user

    if bidders_question == "no":
        start_code = False


    elif bidders_question == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') #-Clean the screen after the user's input
         

#Mostrar os respectivos valores -- nome e quantia 
for user in data_base:
    print(f'{user}: ${data_base[user]}')


