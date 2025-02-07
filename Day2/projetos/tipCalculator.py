
print(''' _____ _         _____       _            _       _             
|_   _(_)       /  __ \     | |          | |     | |            
  | |  _ _ __   | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | | | | '_ \  | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | | | | |_) | | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
  \_/ |_| .__/   \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
        | |                                                     
        |_|                                                     

''')
print("Bem vindo(a) ao Tip Calculator")

orcamentoTotal = float(input('Qual é o orçamento total ?:\n'))

porcentagem_gorjeta = int(input('Qual a porcentagem bonus de gorjeta voce gostaria de oferecer? Informe: 10% , 12% , 15%:\n'))

qtd_Pessoas = int(input('Quantas pessoas vao dividir a gorjeta?:\n'))



gorjeta = (porcentagem_gorjeta / 100) * orcamentoTotal + orcamentoTotal
resultado = gorjeta / qtd_Pessoas
print(f'Cada pessoa devera pagar R$ {resultado:.2f}')


#A gorjeta é um valor adicional como forma de reconhecimento do serviço do empregado
#Logo, a  gorjeta é um bonus adicional de n% do valor do orçamento, um acrescimo



