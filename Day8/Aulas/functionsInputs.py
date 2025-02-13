def greet():
    print('Hello')
    print('World')
    print('Encoders')

greet()


#Name é o paramentro atribuido na função helloUser()
#E "Amanda" é o argumento(usado para atribuir um valor durante o uso dessa função)
def helloUser(name):
    print('Hello', name)
    print('How do you do?', name)

helloUser("Amanda")


#Inputs em funções

def myInput():
    age = int(input('What is your age?: '))
    print('Your age is', age)
myInput()


#O argumento de uma função pode ser entendido como 
# o valor guardado dentro de uma variavel, chamada de parametro
# Por exemplo: na função helloUser() name é o parametro e "Amanda" é um argumento
#
#Para a função, o parametro  é uma variavel entre parenteses apos a definiçaõ de seu name
