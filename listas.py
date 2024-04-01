def a001():
    lista = []
    tamanho = int(input('Quantos elementos irá colocar na sua lista? '))
    for ob in range(1,tamanho + 1):
        nun = int(input('Digite o valor que ficará na {}° posição da lista:> '.format(ob)))
        if nun == 666:
            print('Você decidiu interronper o programa! ')
            break
        lista.append(nun)
        print(f'{nun} foi adicionado na lista! ')
    print(f'Sua lista => {lista}')
    print(f'O maior valor é {max(lista)} e foi encontrado nas posições => ',end='')
    for i,v in enumerate(lista):
        if v == max(lista):
            print(f'   {i},', end='')
    print(f'\nO menor valor é o {min(lista)} e foi encontrado nas posições => ',end='')
    for i,v in enumerate(lista):
        if v == min(lista):
            print(f'  {i},',end='')


def a002():
    lista = []
    while True:
        ob = int(input('Digite um valor para adicionar na lista: '))
        for i, v in enumerate(lista):
            if ob == v:
                cnt = str(input(f'{ob} já existe na sua lista! Deseja adicionar mesmo assim? [S/N] ')).strip()[0]
                if cnt in 'Nn':
                    ob = int(input('Digite outro valor: '))
        lista.append(ob)
        opc = str(input('Quer continuar? [S/N] ')).split()[0]
        if opc not in 'Ss':
            break



    print(f'Sua lista => {lista}')




def a003():
    lis = []
    n = int(input('Sua lista terá quantos elementos? '))
    for c in range(0,n):
        nun = int(input('Digite um valor para adicionar a lista: '))
    
        if c == 0 or nun > lis[-1]:
            lis.append(nun)
            print('Valor adicionado na lista!')

        else:
            pos = 0
            while pos <= len(lis):
                if nun <= lis[pos]:
                    lis.insert(pos,nun)
                    print(f'Valor adicionado no indice {pos} da lista ')
                    break
                pos += 1

    print(f'Sua lista => {lis}')




def a005():
    lis = []
    s = 0 
    while True:
    
        if s > 0:
            opc = str(input('Quer continuar? ')).strip()[0]
            if opc not in 'Ss':
                break
        nun = int(input('Digite um valor para ser adicionado na lista: '))
        if nun in lis:
            print(f'O número {nun} ja estar na lista! ')
        else:
            lis.append(nun)
            print('Valor adicionado com sucesso! ')
        s += 1    
    print(f'Sua lista => {lis}')
    lisord = lis.sort(reverse=True)
    print(f'Sua lista ordenada => {lis.sort()}')
    print(f'Sua lista de forma decresente => {lisord}')




def a006():
    lista = []
    while True:
        nun = int(input('Digite um número a ser adicionado na lista: '))
        lista.append(nun)
        print(f'{nun} foi adicionado a sua lista com sucesso! ')
    
        if nun == -66:
            break
    pares = impares = []
    2
    for i, v in enumerate(lista):
        print(i)
        if v % 2 == 0:
            pares.append(v)
        else:
            impares.append(v)
    print(f'A sua lista gereada é => {lista}')
    print(f'Lista somente com os pares => {pares}')
    print(f'Somente impares {impares}')


print('\033[32mWrite stop for break\033[m')
while True:
    exp = str(input('Digite sua expreção para verificar a validação: '))
    if exp == 'stop':
        break
    pilha = []
    for el in exp:
        if el == '(':
            pilha.append("()")
        elif el == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(")")
                break
    if len(pilha) == 0 :
        print('Sua expresão está valida! ')
    else:
        print('Invalido!')