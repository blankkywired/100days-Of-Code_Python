#A linha abaixo ira retornar um erro pois a função len não aceita numeros inteiros
# lenght = len(12345)
# print(lenght)


#A linha abaixo ira retornar a quantidade de caracteres como o esperado
lenght = len("12345")
print(lenght)


#Challenger
# A linha abaixo retornara um erro
# Pois não é possivel cocatenar string com numeros usando "+" , somente ","
# print('Numeros de letras em sua string: ' + len(input('Digite sua string: ')))

#Retornara o valor esperado
print('Numeros de letras em sua string: ' , len(input('Digite sua string: ')))

#Usand =o conversão do tipo de dado de len, que é um valor inteiro e covertendo para string
print('Numeros de letras em sua string: ' + str(len(input('Digite sua string: '))))


