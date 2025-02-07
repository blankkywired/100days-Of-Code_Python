letter = 'x'
base = int(input('Insira o tamanho da base:\n'))

for i in range(1, base + 1):
    triangulo = letter * i
    print(f'\t{triangulo}')

