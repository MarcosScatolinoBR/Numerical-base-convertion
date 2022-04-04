binario = []
def entra():
    entrou = input('Entre com um número de, no máximo, 3 dígitos, em forma binária: ')
    if (len(entrou) > 3):
        print('Entre com um número de no máximo de 3 dígitos')
        entra()
    for i in entrou:
        if (entrou != 0 or entrou != 1):
        print(i)
        print('Digite apenas números 0 ou 1')
        entra()
    else:
        entrada = int(entrou)
        binario = bin(entrada)

entra()
print(binario)
