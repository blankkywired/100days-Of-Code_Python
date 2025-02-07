# Write a function to check if an intenger is divisible by five

# return True if the number is divisible by 5
# Othewise, return False


def is_divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False

print(is_divisible_by_five(5))