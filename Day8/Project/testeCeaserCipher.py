import letters


message = ""

message = input('Digite uma mensagem para codificar: ')
message = message.lower() #Transforma todo o conteudo da mensagem em lowercase
print(message)

splitMensage = [i for i in message if i != ' '] #Cria uma lista contendo cada caractere da mensagem do usuario que nao seja esse caractere um
# Espaco em branco
print(splitMensage)

