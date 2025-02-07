print('Bem vindo(a) ao Python Delivery')
tamanhoPizza = input('Qual o tamanho da pizza que voce deseja? P , M , G: ')
peperonni = input('Gostaria de adicionar peperonni na sua pizza?: S ou N: ')
queijo_extra = input('Gostaria que adicionar queijo extra?: S ou N: ')

#Pizza pequena
if tamanhoPizza == 'P':
    valor = 15
    if peperonni == "S":
        valor = valor + 2
    if queijo_extra == "S":
        valor = valor + 1

#Pizza Media
elif tamanhoPizza == 'M':
    valor = 20
    if peperonni == "S":
        valor = valor + 3
    if queijo_extra == "S":
        valor = valor + 1

#Pizza Grande
elif tamanhoPizza == 'G':
    valor = 25
    if peperonni == "S":
        valor = valor + 3
    if queijo_extra == "S":
        valor = valor + 1


print(f'O seu pedido custará R$ {valor}')