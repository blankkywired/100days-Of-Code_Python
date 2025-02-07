peso = float(input('Informe o peso em Kilogramas(EX: 56.7): '))
altura = float(input('Informe sua altura em Metros(EX: 1.56): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(round(imc, 2))
    print('Abaixo do peso!')

elif imc <= 24.9:
    print(round(imc, 2))
    print('Peso ideal')
    
else:
    print(round(imc, 2))
    print('Acima do Peso')