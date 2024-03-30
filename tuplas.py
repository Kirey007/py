def a01():
    colocados = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo','Corinthians','Criciúma', 'Cruzeiro','Cuiabá','Flamengo','Fluminense','Fortaleza','Grêmio','Internacional','Juventude', 'Palmeiras','Red Bull Bragantino','São Paulo','Vasco da Gama','Vitória')
    from time import sleep
    while True:
        opc = str(input('C para continuar, E para sair')).upper().strip()[0]
        if opc in 'eE':
            break
        print('Carregando informações no banco de dados..')
        sleep(1)
        print('     RESULTADO DO BRISILEIRÃO')
        print('=-'*20)
        print('')
        print(f'Os 5 primeiros colocados são:{colocados[:5]}')
        print(f'Os 4 ultimos colocados são:{colocados[-4:]}')
        clr = sorted(colocados)

        print('     LISTA DOS TIMES NO BANCO DE DADOS')
        for c in clr:
            print(f'- {c}')

    
def a02():
    while True:
        nuns = ('Zero','Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catose','Quinze',
                'Deseseis','Desesete','Desoito','Desenove','Vinte')

        ps = int(input('Digite um número entre 0 e 20: '))
        if ps == 88:
            break
        if ps > 20 or ps < 0:
            ps = int(input('Opção Invalida! Tente novamente de 0 a 20 '))

        r = nuns[ps]
        print(f'Você digitou o número {r}')





def a03():
    from random import randint

    while True:
        opc = str(input('N for play :')).strip().upper()[0]
        if opc == 'N':
            nuns = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
            print(f'Os números sorteados foram {nuns}')
            maior = m = nuns[0]
            while True: #verifica qual é o maior
                if nuns[1] > maior :
                    maior = nuns[1]

                if nuns[2] > maior:
                    maior = nuns[2]
                if nuns[3] > maior:
                    maior = nuns[3]

                if nuns[4] > maior:
                    maior = nuns[4]

                break

            while True:
                if nuns[1] < m :
                    m = nuns[1] 

                if nuns[2] < m:
                    m = nuns[2]
                if nuns[3] < m:
                    m = nuns[3]

                if nuns[4] < m:
                    m = nuns[4]
                break
            print(f'O maior foi o {maior} e o menor foi {m}')
        else:
            break





def a03v2():
    from random import randint

    while True:
        opc = str(input('N for play :')).strip().upper()[0]
        if opc == 'N':
            nuns = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
            print(f'Os números sorteados foram {nuns}')
            maior = m = nuns[0]
            print(f'O maior é {max(nuns)} \nE o menor é {min(nuns)}')


        else:
            break




def a004():
    num =   (int(input('Digite um número: ')),
            int(input('Digite outro: ')),
            int(input('Mais um: ')),
            int(input('O ultimo : ')))
    print(num)
    print(f'O valor 9 apareceu {num.count(9)} vezes')
    if 3 in num:
        print(f'O valor 3 apareceu no indice {num.index(3)}')
    par = imp = 0
    for n in num:
        if n % 2 == 0:
            par += 1
        else:
            imp += 1

    print(f'Dos valores {par} são PAR e {imp} são IMPARES ')





def a0012():
    lista = ('Casaco', 66.43,'Camisa', 44 ,'sort', 32)

    for c in range(1,len(lista)):
        if c % 2 == 0 :
            print(f'{lista[c]:.<15}',end='')
        else: 
            print(f'R${lista[c]:>}')


palavras = ('Casaco','box','Treiler','carro','dinheiro')


for p in range(1,len(palavras)):
    l = ''
    for l in palavras[p]:
        if l.lower() in 'aeiou':
            nl += l


    print(f'As letras miniscula da palavra {palavras[p]} são: {l}')