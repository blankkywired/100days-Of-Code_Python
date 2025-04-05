#Dicionarios são variaveis que funcionam para guardar multiplos valores correlacionados de uma so vez

#Estrutura Basica de um dicionario em python:
#{Key: Value}

dic = {"Bug": "an error in a program thats prevents the programming running as expected."}
print(dic)

colors = {
    "apple": "red",
    "strayberrys": "purple",
    "banana": "yellow"
}

print(colors["apple"]) #Busca pela propriedade do item apple dentro da variavel colors
#Para retornar o valor de uma "Key", basta usar o nome da key entre colchetes

nomes_idades = {
    "Guilherme": 20,
    "Kaua": 17,
    "Katarina": 26,
    "Lux": 19
}
print(nomes_idades["Guilherme"])

for i in nomes_idades:
    print(i , nomes_idades[i] , "Anos") #Itera sobre cada elemento da lista mostrando o nome seguido da propriedade(idade) do nome atribuido


#Adicionando valores a dicionarios
#Estrutura para adicionar valores dentro de dicionarios:

# nome_do_dicionario[Key] = valor da key

nome = {
    "Guilherme": 20,
    "Samira": 30
}

nome["Lux"] = 19 #Adiciona a key lux com o respectivo valor(19)

print(nome)