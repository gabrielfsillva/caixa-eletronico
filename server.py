from socket import *

# Configuração conexao
HOST = 'localhost'
PORTA = 80

# Estabelece a conexação
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)

print ('Servidor Iniciado!')
while True:
    #Aceita conexao do cliente
    conexao, endereco = sockobj.accept()
    

    while True:
        #Recebe informação e decodifica para string
        
        login = conexao.recv(1024).decode()
        senha = conexao.recv(1024).decode()
        if login=='1010' and senha=='123456':
            print ('login confirmado')
            resposta = 'sucesso'
            conexao.send (resposta.encode())
            # break
        else:
            print('Acesso negado')
            resposta = 'falhou'
            conexao.send (resposta.encode())
           
     
   
    print ('Desconectado', endereco)
    
    conexao.close ()