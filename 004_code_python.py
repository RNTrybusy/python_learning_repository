num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
subtrai = num1 - num2
multiplica = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
potencia = num1 ** num2
resto_divisão = num1 % num2
raiz_quadrada1 = num1 ** (1/2)
raiz_quadrada2 = num2 ** (1/2)
print(f'Entre os números {num1} e {num2} esses são os cálculos.')
print(f'Soma: {soma} \nSubtrai: {subtrai} \nMultiplicação: {multiplica} \nDivisão: {divisao:.3f} \nDivisão Inteira: {divisao_inteira} \nPotência: {potencia} \nResto da Divisão: {resto_divisão} \nRaiz Quadrada de {num1}: {raiz_quadrada1:.3f} \nRaiz Quadrada de {num2}: {raiz_quadrada2:.3f}')