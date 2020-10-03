# Esse codigo foi desenvolvido pelo grupo F13!
import hibpwned
import pandas
import os
from time import sleep
from colorama import init, Fore
from supferramenta import * #indi, wordlistkk, about
#from cademails import cadpessoa

init()
api = '' # KEY DO HAVEIBEENPWNED
dados = {}

#vazado = pawned
#ass = assunto

print (Fore.LIGHTGREEN_EX+'''
  ▌ ▐· ▄▄▄· ▄▄▌       ·▄▄▄▄  ▪  ▄▄▄   
 ▪█·█▌▐█ ▀█ ██•       ██▪ ██ ██ ▀▄ █· 
 ▐█▐█•▄█▀▀█ ██▪       ▐█· ▐█▌▐█·▐▀▀▄  
  ███ ▐█ ▪▐▌▐█▌▐▌  •  ██. ██ ▐█▌▐█•█▌ 
 . ▀   ▀  ▀ .▀▀▀   ▀  ▀▀▀▀▀• ▀▀▀.▀  ▀  1.0.0

[©] Todos os direitos reservados pela F13 [©]
''')

while True:

    print (Fore.LIGHTGREEN_EX+'''
[•] Escolha a forma de consulta [•]
    |
    |-> [1] Consultar Email
    |
    |-> [2] Consultar Senhas 
    |
    |-> [3] Definir um aviso
    |
    |-> [4] Sobre a ferramenta
    |
    |-> [5] Sair
    ''')

    escolha = int(input(Fore.LIGHTGREEN_EX+'[:] Digite a opcao a ser executada: '))

    if escolha == 1:
        sleep(1.5)
        print(Fore.LIGHTBLUE_EX+''' 
Emails    
    |
    |-> [1] Consulta individual
    | 
    |-> [2] Consulta por wordlist (wordlist default: emails.txt)
    |
    |-> [3] Sair

             ''')
        escolha = int(input(Fore.LIGHTBLUE_EX+'[:] Digite a opcao a ser executada: '))

        if escolha == 1:  #opcao individual
            sleep(1.5)
            indi(dados)
            print('')

        elif escolha == 2: # opcao de wordlist
            sleep(1.5)
            wordlistkk(dados)
            print('')

        elif escolha == 3: # SAIR
                exit()


    elif escolha == 2:
        sleep(1.5)
        print(Fore.LIGHTYELLOW_EX+''' 
Senhas   
    |
    |-> [1] Consulta individual
    | 
    |-> [2] Consulta por wordlist (wordlist default: senhas.txt)
    |
    |-> [3] Sair

            ''')
        escolha = int(input(Fore.LIGHTYELLOW_EX+'[:] Digite a opcao a ser executada: '))

        if escolha == 1: #opcao individual
            sleep(1.5)
            passwdvzd(dados)
            print('')

        elif escolha == 2: # opcao de wordlist
            sleep(1.5)
            wordlistpass(dados)
            print('')

        elif escolha == 3: # Sair
            exit()

    elif escolha == 3:
        sleep(1.5)
        send_email()
        print('')

    elif escolha == 4: # about
        sleep(1.5)
        about(dados)
        print('')

    elif escolha == 5: # sair
        exit()

    else:
        print('Opcao invalida, por favor tente novamente')
