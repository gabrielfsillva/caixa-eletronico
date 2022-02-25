from socket import *
import time
import os
import pwinput

HOST = 'localhost'
PORTA = 80

conexao = socket(AF_INET, SOCK_STREAM)
conexao.connect((HOST, PORTA))



while True:
    
    login = str(input ('Login:'))
    
    senha = pwinput.pwinput('Senha: ')
    print (('Senha digitada {senha}'))
    conexao.send(login.encode())
    conexao.send(senha.encode())
    
    
    resposta = conexao.recv(1024).decode()

    if resposta == 'sucesso':
        print ('Login confirmado!')
        os.system('cls')
        
              
        time.sleep(2)
        print('=' * 30)
        print('{:^30}'.format('CAIXA ELETRÔNICO'))    
        
        menu =(['Depositar','Sacar','Visualizar Saldo','Sair'])
        opcao = 0
        saldo = 0
        saque = 0
        valor = 0

        while opcao !=4:
            print('=' * 30)
            print('''    
[ 1 ] Depositar 
[ 2 ] Sacar 
[ 3 ] Visualizar Saldo 
[ 4 ] Sair
            ''')
            print('=' * 30) 

            opcao = int(input('Digite a opção que deseja realizar: '))
            if opcao == 1:
                valor = int(input('Digite valor a ser depositado: '))
                saldo += valor
                time.sleep(2)
                print('-' * 30)
                print (f'O valor depositado foi de:R${valor}')
            if opcao == 2:
                valor = int(input('Digite valor a ser sacado: '))
                time.sleep(2)
                print('-' * 30)
                print('-' * 30)
                print ('CARREGANDO...')
                if saldo >= valor:
                    saldo -= valor
                    print('-' * 30)
                    print (f'O valor saque foi de:R${valor}')
                    time.sleep(3)
                    print (f'O valor do seu saldo após o saque é de: R${saldo}')
                else:
                     time.sleep(3)   
                     print ('Saldo insuficiente')
                     
            if opcao == 3: 
                time.sleep(2)
                print('-' * 30) 
                print(f'Seu saldo é de : R$ {saldo}')
            if opcao == 4: 
                print('Sessão encerrada!')         

    else:
         print('Acesso negado!')
    break   
    
        
    

conexao.close()