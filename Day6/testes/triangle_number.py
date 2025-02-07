# Write a function to calculate the th triangular triangular_number
# a triangular number is calculated by adding all natural numbers up to n 

# Example: input 5
# output 15
# because the 5th triangular number is calculated as 1+2+3+4+5 = 15



def triangular_number(n):
    acumulador = 0
    for i in range(1, n + 1):
        acumulador = acumulador + i
    return acumulador


print(triangular_number(5))


# for i in range(1, 5 + 1):
#     acumulador = acumulador + i
#     print(acumulador)

