# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Mundo!! Me Ajuda por favor!!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# 1 Funções
''' 
1. Crie uma função potencia que receba dois números a e b (base e expoente,
respectivamente) e retorne a elevado a b!
'''


def potencia(base, expoente):
    resposta = base ** expoente
    return resposta


print('Resposta do Exercício 1: ', potencia(3, 3))

'''
2. Crie uma função que permita a conversão de graus Celsius para Fahrenheit.
'''


def celsius2fahrenheit(graus):
    return 9 / 5.0 * graus + 32


print('Resposta do Exercício 2: ', celsius2fahrenheit(1))

'''
3. Crie uma função numero_par que permita verificar um dado número, x,
passado como parâmetro é um número par.
'''


def numero_par(x):
    if x % 2 == 0:
        return print('Número Par!')
    else:
        return print('Número Impar!')

print('Resposta do Exercício 3:')
numero_par(5.5)


'''
4. Dadas as seguintes funções:
'''
def equacao1(p, q)

