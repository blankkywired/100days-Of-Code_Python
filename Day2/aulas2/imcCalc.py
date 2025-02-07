#entrada de dados do usuario 
altura = float(input('Informe o valor da sua altura em metros:\n'))
peso = float(input('Informe o valor do seu peso em kilograma:\n'))

imc = peso / (altura ** 2)
print(f'Seu imc é: {imc:.2f}')  #Imc formatado para apenas duas casas decimais


