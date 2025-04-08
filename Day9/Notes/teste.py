nomes = {

}

condicao = True

while condicao:
    question = input('Do you want to add more items?: ').lower()
    if question == "yes":
        name = input('Insert the name:')
        age = int(input('Insert the age:'))
        nomes[name] = age

    else:
        condicao = False

for i in nomes:
    print(i, nomes[i] , "Anos")

