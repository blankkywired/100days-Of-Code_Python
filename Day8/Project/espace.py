alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
text = input('Type your message: \n')
shift = int(input('Type the shift number: \n'))



def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter != " ":
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += " "
    print(f"Message encrypted: {cipher_text}")

encrypt(original_text=text, shift_amount=shift)