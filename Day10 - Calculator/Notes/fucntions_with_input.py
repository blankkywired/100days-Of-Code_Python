def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
format_name('guilherme', 'AMANDA')


def format_name(f_name, l_name):
    format_f_name = f_name.title()
    format_l_name = l_name.title()

    return format_f_name , format_l_name

name1 = input('Digite o primeiro nome: ')
name2 = input('Digite o segundo nome: ')

print(format_name(f_name=name1, l_name=name2))