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






