import draw
import os

print(draw.simbol)

start_code = True

data_base = {}
values_bid = []
def most_expensive(value):
    max_value = 0
    for j in value:
        if j > max_value:
            max_value = j
    return (f'The highest value is R${max_value}')
    
while start_code:
    name_user = input('What is your name?: ')
    bid_user = int(input('What is your bid?: $'))
    bidders_question = input("Are there any other bidders?: Type 'yes' or 'no'.\n").lower()

    #Adding the bid for the list
    values_bid += [bid_user]
    #Adding name and bid in the dict
    data_base[name_user] = bid_user

    if bidders_question == "no":
        start_code = False
        print(most_expensive(value=values_bid))


    elif bidders_question == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') #-Clean the screen after the user's input
         


print("-" * 15 , "RESULT" , "-" * 20)
for user in data_base:
    print(f'{user}: ${data_base[user]}')


