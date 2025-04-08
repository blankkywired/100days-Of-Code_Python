#Nesting

#Usando valores aninhados dentro de dicionarios:

capitais_pais = {
    'França': 'Paris',
    'Alemanha': 'Berlim',
    'Russia': 'Moscou',
    'Portugal': 'Lisboa'
}



#Usando listas em dicionarios:
cidades_visitados_por_paises = {
    'França': ['Paris', 'Strasbourg', 'Bordeaux'],

}

cidades_alemanha = {
    'Alemanha': 'Berlim',

}
cidades_visitados_por_paises2 = {
    'França': ['Paris', 'Strasbourg', 'Bordeaux'],
}

print(cidades_visitados_por_paises2['França'][1]) # --- > Mostrando um elemento da lista da Key(frança) dentro do dicionario,  Output = Strasbourg

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1]) # ----> Exibindo um elemento de uma lista aninhada Output: "D"


#Dicionarios aninnhados

#Lista aninhada de paises visitados organizados por cidades visitadas por pais junto com a quantidade de vezes visitadas
travel_log = {
    "France": {
        "num_visited": 8,
        "cities_visited": ["Paris", "Little", "Dijo"]
    }
}