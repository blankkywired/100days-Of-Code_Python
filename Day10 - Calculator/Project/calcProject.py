import art

def func_soma(num1, num2):
    return num1 + num2
def func_subtra(num1, num2):
    return num1 - num2
def func_multi(num1, num2):
    return num1 * num2
def func_divid(num1, num2):
    return num1 / num2

operationDict = {
    "+": func_soma,
    "-": func_subtra,
    "*": func_multi,
    "/": func_divid
}

listOptions = {
    "+": "Add",
    "-": "Subtraction",
    "*": "Multiply",
    "/": "Divide"
}

#O Dicionario armazena as funções como valores para cada key
def main():
    startAlgorithm = True  

    print(art.logo)
    result = 0
    continueCalc = True

    for  option in listOptions:
    #Show options
        print(listOptions[option], option.capitalize())
    UserNumber_1 = float(input('Insert the first number: '))

    while startAlgorithm:
        choiceOperation = input('Choose a operation:')
        UserNumber_2 = float(input('Insert the second number: '))

        print(operationDict[choiceOperation](UserNumber_1,UserNumber_2)) #Exibe o resultado da operação baseada na escolha do usuario, sem o uso de condicionais 

        result = operationDict[choiceOperation](UserNumber_1, UserNumber_2)
            #Puxando a key e o valor dela, o valor da key é uma função, entao, os argumentos são repassados usando as duas entradas do usuario apos a key ser chamada

        print(f"{UserNumber_1},{choiceOperation} {UserNumber_2} = {result}")

        continueCalc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, type 'stop' to finish the process: ").lower()

        if continueCalc == 'y':
            startAlgorithm = True
            UserNumber_1 = result
        elif continueCalc == 'n':
            main()
        elif continueCalc == 'stop':
            print(2 * '\n', 'Process finished', 2 * '\n')
            startAlgorithm = False
            break

if __name__ == '__main__':
    main()




