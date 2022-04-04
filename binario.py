binario = []
entrou = ''
def entra():
    global entrou
    entrou = input('Entre com um número de, no máximo, 3 dígitos, em forma binária: ')
    testa = len(entrou)
    if (testa > 3):
        print('Entre com um número de no máximo 3 dígitos')
        return entra()
    for i in entrou:
        if (i == 0):
            print(i)
        elif (i == 1):
            print(i)
entra()
