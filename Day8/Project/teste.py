letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


message = "ABC"
message = message.lower()
print(message)


# splitMessage = [letter for letter in message if letter != ' ']
# print(splitMessage)



# for i in splitMessage:
#     letterCode = i.replace(i, )

newMessage = message.replace(message, "BCD")
print(newMessage)

for i in message:
    
    newValue = i.replace(i, letters[i])
    print(i, newValue)