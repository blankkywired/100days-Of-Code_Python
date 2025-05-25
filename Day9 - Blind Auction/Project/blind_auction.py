import draw
import os

print(draw.logo)

start_code = True


data_base = {}


def find_highest_bidder(bidding_dictionary):
    winner = ""
    max_value = 0
    for bidder in bidding_dictionary:
        if data_base[bidder] > max_value:
            max_value = data_base[bidder]
            winner = bidder
    
    print(draw.result)
    return f'The highest bid is {winner}: R${max_value}'
    
while start_code:
    name_user = input('What is your name?: ')
    bid_user = int(input('What is your bid?: $'))
    bidders_question = input("Are there any other bidders?: Type 'yes' or 'no'.\n").lower()

    #values_bid += [bid_user]     #Adding the bid for the list
    data_base[name_user] = bid_user    #Adding name and bid in the dicti

    if bidders_question == "no":
        start_code = False
        print(find_highest_bidder(bidding_dictionary=data_base))

    elif bidders_question == "yes":
        os.system('cls' if os.name == 'nt' else 'clear') #-Clean the screen after the user's input
    else:
        print("Please enter a valid bidding_dictionary")
for user in data_base:
    print(f'{user}: ${data_base[user]}')


