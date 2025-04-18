# condicao = True
#
# base = {}
#
# valores = []
#
# def descobrir_maior(valor):
#     for i in valores:
#         if quantia > i:
#             print(f"Maior valor = {quantia}")
#             #Verifica interando sobre cada elemento e comparando se esse elemento é menor do que a ultima quantia adicionada
# while condicao:
#     nome = input('Nome: ')
#     quantia = int(input('Valor: '))
#     valores += [quantia]
#     base[nome] = quantia
#
#     condicao = input('Continuar?: ').lower()
#
#     if condicao == 'n':
#         condicao = False
#
#         # for j in base:
#         #     print(j, base[j])
#         print(descobrir_maior(valor=base[nome]))


lista = [1, 2, 3, 4, 5, 6, 9]

valorUsuario = 8
lista += [valorUsuario]
def maior_numero(valor):
    for i in valor:
        if valorUsuario  > i:
            return i, valorUsuario
        elif valorUsuario < i:
            return 'Não é o maior valor'
        else:
            continue

print(maior_numero(valor=lista))

