import art

def func_soma(num1, num2):
    return num1 + num2
def func_subtra(num1, num2):
    return num1 - num2
def func_multi(num1, num2):
    return num1 * num2
def func_divid(num1, num2):
    return num1 / num2

dados_dict = {
    "adição": "+",
    "subtração": "-",
    "multiplicação": "*",
    "divisão": "/"
}
def main():
    print(art.logo)
    continue_calc = True
    number_1 = float(input('Insert a number to calculate:\n'))
    #Save result's value
    result = 0
    while continue_calc:
        #Show options(operations)
        for i in dados_dict:
            print(dados_dict[i] , i.capitalize())
        select_Operation = input("\nSelect an operation:")

        number_2 = float(input('Choose the second number:'))

        if select_Operation == "+":
            print(f"{number_1} + {number_2} = {func_soma(num1=number_1, num2=number_2)}")
            result = func_soma(num1= number_1, num2=number_2)
        elif select_Operation == "-":
            print(f"{number_1} + {number_2} = {func_subtra(num1=number_1, num2=number_2)}")
            result = func_subtra(num1=number_1, num2=number_2)
        elif select_Operation == "*":
            print(f"{number_1} + {number_2} = {func_multi(num1=number_1, num2=number_2)}")
            result = func_multi(num1=number_1, num2=number_2)   
        elif select_Operation == "/":
            print(f"{number_1} + {number_2} = {func_divid(num1=number_1, num2=number_2)}")
            result = func_divid(num1=number_1, num2=number_2)
        else:
            print('Insert a valid option')

        continue_calc = input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation , type 'stop' to finish the process\n: ").lower()
        
        
        if continue_calc == "y":
            continue_calc = True
            number_1 = result
        elif continue_calc == "n":
            main()
        elif continue_calc == "stop":
            print(2 * '\n' , 'Process finished' , 2 * '\n')
            continue_calc = False
            break


if __name__ == '__main__':
    main()
