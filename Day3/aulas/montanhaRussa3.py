altura = float(input('Digite sua altura em metros(EX: 1.20): '))

if altura >= 1.20:
    print('Voce pode ir na montanha russa!')
    idade = int(input('Informe sua idade: '))

    if idade < 12:
        print(f'Altura: {altura} , idade: {idade}')
        print('Valor a pagar: R$ 5')

    elif idade >= 12 and idade <= 18: #Intervalo da idade entre 12 anos e 18 anos
        print(f'Altura: {altura} , idade: {idade}')
        print('Valor a pagar: R$ 7')

    else : #para idades maiores do que 18 anos
        print(f'Altura: {altura} , idade: {idade}')
        print('Valor a pagar: RS 12')
else:
    print('Altura insuficiente')    