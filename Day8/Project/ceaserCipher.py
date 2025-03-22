import art

print(art.title)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser(original_text, shift_amount, encode_decode):
    output_text = ""
    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        
        else:
            shifted_letter = alphabet.index(letter) + shift_amount
            shifted_letter %= len(alphabet)
            output_text += alphabet[shifted_letter]
    print(f'The result of the {encode_decode} is: {output_text}')


continueCode = True

while continueCode:

    direction = input("Type 'encode' to encrypt or 'decode' to decrypt the text: \n").lower()

    text = input('Type your text here:\n').lower()
    shift = int(input('Type the shift amount here: \n'))

    ceaser(original_text=text, shift_amount=shift, encode_decode=direction)

    restart = input("Type 'yes' if you want to run the code again or 'no' to finish the process: ").lower()

    if restart == 'no':
        continueCode = False
        print('Process finished')