altura = float(input('Informe a sua altura em Metros(Ex: 1.20): '))
if altura >= 1.20:
    print('Voce pode ir na montanha russa!')
    idade = int(input('Informe a sua idade: '))  #Esta linha so sera executada se a condição for verdadeira
    if idade <= 18:
        print('Valor da taxa a pagar: R$ 7')
    else: 
        print('Valor de taxa a pagar: R$ 12')
else:
    print('Voce nao tem altura o suficiente para ir na motanha russa')