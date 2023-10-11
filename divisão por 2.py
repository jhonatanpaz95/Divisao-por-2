#programa de divisão (versão-1)

nome_usuario = input('digite seu nome: ')
idade_usuario = input('digite sua idade: ')

print(f'O nome do usuário(a) é {nome_usuario} e sua idade é {str(idade_usuario)} anos.')

print(f'{nome_usuario }vamos verificar se um numero é par?!')

digite_um_numero = int(input((f'digite um numero {nome_usuario}: ')))

if  digite_um_numero % 2 == 0:
    print('O numero que você digitou é par (ou seja, a divisão desse número por 2 tem resto igual a 0)')
else:
    print('o numero que você digitou é impar')