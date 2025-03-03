letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# message = input('Insira sua mensagem: ')
def encrypt(message, shift):
    message = message.lower()
    print(f'Sua mensagem:' , message)

    placeholder = ""
    messageCrypted = ""

    # shift = int(input('Shift amount:'))

    for char in message:
        if char != " ":
            indexLetra = letters.index(char) + shift  #Gera um indice usando a busca pelo caractere da mensagem na lista de letras,
            # exibindo a posicao, depois soma essa posicao com o numero de casas para mover a direita

            placeholder = char.replace(char ,letters[indexLetra]) #Substitui o caractere pelo indice correspondente do elemento da lista de letras,
            #o indice é dado pela variavel indexLetra

            messageCrypted += placeholder #Adiciona cada caractere um por um formando uma nova mensagem
            
        elif char == " ":
            placeholder = " "
            messageCrypted += placeholder
        
            
            
        # print(letters.index(letter), letter,  indexLetra , placeholder)
    return messageCrypted


print(encrypt('Katarina', 2))


def decrypt(message, shift):
    placeholder = ""
    messageDecrypted = ""
    message = message.lower()
    print(f'Sua mensagem:' ,  message)

    for char in message:
        if char != " ":
            indexLetra = letters.index(char) - shift

            placeholder = char.replace(char, letters[indexLetra])
            messageDecrypted += placeholder
        
        elif char == " ":
            placeholder = " "
            messageDecrypted += placeholder
    
    return messageDecrypted

    
print(decrypt('k nqxg w ', 2))

