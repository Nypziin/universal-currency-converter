from Conversor import Conversor

while True:
    valor = 0
    while True:
        try:
            valor = int(input('Digite o valor: '))
        except (TypeError, ValueError):
            print('Valor inválido, digite novamente!')
            continue
        break

    while True:
        valor_inicial = input('Digite a moeda primária: ')
        valor_final = input('Digite a moeda final: ')

        conversor = Conversor(valor, valor_inicial, valor_final)
        status_moedas = conversor.verificar_moeda()

        if not status_moedas[0]:
            print(f'A moeda {valor_inicial} não existe.')
            continue

        elif not status_moedas[1]:
            print(f'A moeda {valor_final} não existe.')
            continue

        print(conversor.converter())
        print('------------------------------------------------------')
        break

