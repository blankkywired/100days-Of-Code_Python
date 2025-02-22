import letters




message = input('Digite uma mensagem para codificar: ')
message = message.lower()
# Transforma T0do o conteudo da mensagem em lowercase
print(message)

splitMensage = [i for i in message if i != ' '] #Cria uma lista contendo cada caractere da mensagem do usuario que nao seja esse caractere um
# Espaco em branco
print(splitMensage)

