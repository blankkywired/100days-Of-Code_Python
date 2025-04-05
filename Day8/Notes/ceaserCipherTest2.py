alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n ").lower()
text = input("Type your message:\n").lower()
shift = int(input('Type shift number:\n'))


def ceaser(encode_decode, original_text, shift_amount):
    cipher_text = ""
    
    if direction == "encode":
        for char in original_text:
            if char != " ":
                shifted_position = alphabet.index(char) + shift_amount
                shifted_position %= len(alphabet)#Verifica o resto de elementos na lista de letras, se shifted position for menor do que o total de elementos da lista
                #Sera gerado um novo indice do começo da lista
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += " " #Adiciona espaços na mensagem


        

    print(f"Message: {cipher_text}")

ceaser(encode_decode=direction, original_text=text, shift_amount=shift) #Cada argumento ira receber uma variavel com um input, para que nao
#seja necessario passar os argumentos na função, e sim, durante a execução do codigo, automatizando o processo.enc