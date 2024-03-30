
def Jog(): #JOGO DO PAR OU IMPAR
    from random import randint
    v = 0 
    while True:
        pc = randint(1,10)
        jogador = int(input('Digite um valor de 0 a 9: '))
        total = pc + jogador
        tipo = " "
        while tipo not in 'PpIm':
            tipo = str(input('Deseja jogar Par ou impar? [P/I] ')).upper()[0]

        print('Vc Jogou {} e o Pc {}. Somando dá {}'.format(jogador,pc,(jogador + pc)))
        print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
        if tipo in "pP":
            if total % 2 == 0:
                print('Você venceu! ')
            else:
                print('você perdeu!')
                break
        elif tipo in 'Ii':
            if total % 2 == 0:
                print('Você perdeu! ')
                break
            else:
                print('Você venceu!')
                v += 1
        print('Vamos jogar novamente... ')
    print('GAME OVER! Você venceu {} de vezes'.format(v))



def cadastro():
    from time import sleep
    cont = 0
    H = M = M20  = 0
    soma = 0
    while True:
        cont += 1
        print('-='*20)
        print('     CADASTRO DE PESSOAS')
        print('=-'*20)
        print('')
        idade = int(input('Inssira a idade da {}° pessoa: '.format(cont)))
        sexo = ' '
        while sexo not in 'FM':
            sexo = str(input('Informe o sexo [M/F]: ')).upper().strip()[0]
        resp = ' '
        soma += idade 
        if idade < 20 and sexo == 'F':
            M20 += 1
        if sexo == 'M':
            H += 1
        if sexo == "M":
            M += 1
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp == 'N':
            break
    print('Cadastro Finalizado.') 
    sleep(1)
    print('Gerando resultados... ')
    medida = soma  / cont
    sleep(1)
    print(f'A media das idades cadastradas é {medida}, a quantidade de Homens é {H}, Mulheres é {M}\n{M20}Mulheres com menos de 20 anos de idade ')






def carrinho(): #Exibe estatisticas de um carrinho de supermercado
    soma = cont = 0
    pm = 0
    pb = 0
    nb = ' '
    while True:
        
        print('-='*20)
        print('     CARRINHO DE SUPERMERCADO  [value negative for stop]')
        print('=-'*20)
        print('')
        print(' -ITEM {}'.format(cont + 1))
        print('')
        nome = str(input('Qual é o nome do produto? '))
        valor = float(input('Qual é o valor do produto? '))
        if valor < 0:
            break
        soma += valor
        if cont == 1 or valor < pb:
            nb = nome  
            pb = valor
    
        if valor > 1000:
            pm += 1
    
        cont += 1
    print(f'Em uma lista de {cont} produtos, seu preço a pagar é de R${soma:40.2f}\nO produto mais barato da lista foi (a) {nb}custando apenas R${pb} Reais\nE {pm} dos itens passaam da faxa dos Mil reais.')



def caixa(): #CAIXA ELETRONICO Com bug no saque!
    from time import sleep
    while True:

        user = str(input('Digite o seu nome de usuario: ')).strip()
        if user == '':
            print('Nome de usuario Invalido!')
            user = str(input('Digite o seu noome de usuario: '))
        senha = str(input('Digite a sua senha: ')).strip()
        if senha == '':
            print('Senha Invalida!')
            senha = str(input('Digite a sua senha: ')).strip()
        cont = 0

        saldo = 232
        while True:
            print('-='*20)
            print('     BANCO DO GUSTAVO')
            print('=-'*20)
            print(f'Olá, {user}\nSeu saldo é de R${saldo} Reais') 
            print('--'*20)
            print('')
            print('Oque deseja fazer?\n[ 0 ] Sair\n[ 1 ] Fazer Depósito\n[ 2 ] Fazer um saque ')
            opc = int(input('Digite a opção: '))
            if opc > 2 or opc < 0:
                opc = int(input('Opção Invalida! Digite novamente: '))
            elif opc == 0:
                break
            elif opc == 1:
                dep = float(input('Qual o valor do depósito? R$'))
                if dep < 0:
                    dep = float(input('Qual o valor do depósito? R$'))
                cont += 1
                saldo += dep
            elif opc == 2:
                cont += 1
                sc = float(input('De quanto deseja fazer o saque? R$'))
                print('Processando...')
                sleep(1)
                duzentos = cem = cinquenta = vinte = dez = cinco = dois = cent = 0
                if sc > saldo:
                    print('Saldo incuficiente!')
                else:
                    if sc // 200 != 0:
                        duzentos = sc // 200
                        sc -= duzentos * 200
                    if sc // 100 != 0:
                        cem = sc // 100
                        sc -= cem * 100
                    if sc // 50 != 0:
                        cinquenta = sc // 50
                        sc -= cinquenta * 50
                    if sc // 20 != 0:
                        vinte = sc // 20
                        sc -= vinte * 20
                    if sc // 10 != 0:
                        dez = sc // 10
                        sc -= dez * 10
                    if sc // 5 != 0:
                        cinco = sc // 5
                        sc -= cinco * 5
                    if sc // 2 != 0 :
                        dois = sc // 2
                        sc -= dois * 2
                    soma = (duzentos * 20) + (cem * 100) + (cinquenta * 50) + (vinte * 20) + (dez * 10) + (cinco * 5) + (dois * 2) 
                    saldo -= soma

                    print('Serão imprimidas as seguintes quantidades de notas:\n {:.0f} de R$200\n {:.0f} de R$100\n {:.0f} de R$50n\ {:.0f} de R$20\n {:.0f} de R$10\n {:.0f} de R$5\n {:.0f} de R$2'.format(duzentos,cem,cinquenta,vinte,dez,cinco,dois))
                    if sc != 0 :
                        print(f"Não exite notas suficientes para sacar R${sc} do valor desejado, por isso irá ficar na sua conta ")
                    c = str(input('Deseja continuar? ')).upper().strip()[0]
                    if c != 'S':
                        break


        break
    print('Fechando sistema...')
    sleep(1)
    print(f'OBS: Foi feito {cont} operações na seção anterior do caixa')


caixa()