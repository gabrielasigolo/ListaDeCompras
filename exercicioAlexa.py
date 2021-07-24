print('\033[1;30;41m=-' * 20, 'LISTA DE COMPRAS', '=-' * 20, '\033[m')
listaCompras = []
item = ''
n = 0
print('\033[36mDigite "Fim" quando finalizar a lista\033[m')
while item != 'Fim':
    n = n + 1
    item = input('Digite o {}º item: '.format(n)).capitalize()
    if item != 'Fim':
        listaCompras.append(item)
print('')

print('\033[0;35;40m-=-\033[m' * 10)
print('Sua lista de compras:')
for i in range(0, len(listaCompras)):
    print('Item {}: {}'.format(i + 1, listaCompras[i]))
print('\033[0;35;40m-=-\033[m' * 10)