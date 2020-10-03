import hibpwned
import pandas
import os
from time import sleep
from colorama import init, Fore
import smtplib
#from cademails import cadpessoa

def indi(dados):  #opcao individual

    api = '' # KEY DO HAVEIBEENPWNED

    emailvzd = input(Fore.LIGHTYELLOW_EX+'[+] Digite o email para consultar: ') # variavel do email pra consultar
    data_list = []

    check = hibpwned.Pwned(emailvzd, 'HIBP_Email_Check', api) # variavel check == pra comparar o email na api
    myBreaches = check.searchAllBreaches(truncate=False, unverified=True)

    if not '404' in str(myBreaches): # condicional caso o email tenha sido vazado
        print (Fore.LIGHTRED_EX+'\n[!] ' + emailvzd + ' foi vazado!')
        print('[Email]  [Local]  [Type]  [Data]')

        for x in myBreaches:  # salva cada dado da variável na lista PAWNED[], separando por colunas.
            for y in x ['DataClasses']:
                pawned = [emailvzd,x['Name'],y,x['BreachDate']]
                print(pawned)
                data_list.append(pawned)

    elif '404' in str(myBreaches): # condicional caso o email n tenha sido vazado
        print (Fore.LIGHTBLUE_EX+'\n[!] ' + emailvzd + ' nao foi vazado!')

def wordlistkk(dados):  #opcao de wordlist

    api = '26274f6c776746909f7afee0f44e60b8' 

    pergunta = input('Ja possui uma wordlist ? ou quer criar uma ?(Y ou N)').upper()

    if pergunta == 'Y':
        sleep(1.5)
        #cadpessoa(dados)

    elif pergunta == 'N':

        file = input('[!] Insira o arquivo com os emails a serem pesquisados (.txt) (wordlist default: emails.txt): ')

        sleep(1.5)

        print('[!] A lista deve estar na mesma pasta que os codigos [!]')


        if not os.path.isfile(file):
            print (Fore.LIGHTRED_EX+'[X] O arquivo nao existe no diretorio.')
            quit()

        elif not file.endswith('.txt'):
            print ('[!] Apenas ha suporte para .txt files.')
            quit()

        elif file == '':
            print (Fore.LIGHTRED_EX+'[X] Nome de arquivo invalido.')
            quit()

        else: # abre o arquivo e cria as 2 listas
            data_list = []
            f = open(file, 'r')
            emails = []

            for z in f: # pesquisa na API e salva na variavel usando append, cada dado abaixo do outro
                z = z.strip()
                emails.append(z)
                myApp = hibpwned.Pwned(z, 'HIBP_Email_Check', api)
                myBreaches = myApp.searchAllBreaches(truncate=False, unverified=True)

                if not '404' in str(myBreaches):  # caso o email não esteja em uma lista de vazado, printa "(EMAIL) não vazado"
                    print (Fore.LIGHTRED_EX+'\n [!] ' + z + ' foi vazado!')

                    for x in myBreaches:  # salva cada dado da variável na lista PAWNED[], separando por colunas.
                        for y in x['DataClasses']:
                            pawned = [z,x['Name'],y,x['BreachDate']]
                            data_list.append(pawned)

                else:  # se n tiver salvo ele salva todas as colunas da ultima linha como null
                    not_pawned = ['','','','']
                    data_list.append(not_pawned) 
                    sleep(1.5)   

                data = pandas.DataFrame(data_list ,columns= ['Email','Incidente','Dado Vazado','Data do Vazamento'])  # define o titulo de cada coluna

                with pandas.io.excel.ExcelWriter('filename.xlsx') as writer: #por data e hora  no resultado # salva tudo isso em um arquivo
                    data.to_excel(writer, sheet_name='Status', index=False)

        print ('\n [+] Tarefa finalizada, salva no arquivo consulta.xlsx') #definir o mesmo nome de arquivo para essa string filename.xlsx

def passwdvzd(dados):
    api = '26274f6c776746909f7afee0f44e60b8'

    senhavzd = input(Fore.LIGHTYELLOW_EX+'[+] Digite a senha para consultar: ') # variavel de senha pra consultar
    data_list = []

    check = hibpwned.Pwned(senhavzd, 'HIBP_Pwd_Check', api) # variavel check == pra comparar o senhas na api
    myBreaches = check.searchAllBreaches(truncate=False, unverified=True)

    if not '404' in str(myBreaches): # condicional caso o senhas tenha sido vazado
        print (Fore.LIGHTRED_EX+'\n[!] ' + senhavzd + ' foi vazado!')

    elif '404' in str(myBreaches): # condicional caso a senha n tenha sido vazado
        print (Fore.LIGHTBLUE_EX+'\n[!] ' + senhavzd + ' nao foi vazado!')

def wordlistpass(dados):
    api = '26274f6c776746909f7afee0f44e60b8' 

    #if pergunta == 'Y':
    #    sleep(1.5)
    #    cadpessoa(dados)

    #elif pergunta == 'N':

    file = input('[!] Insira o arquivo com as senhas a serem pesquisadas (.txt) (wordlist default: senhas.txt): ')
    sleep(1.5)

    print('[!] A lista deve estar na mesma pasta que os codigos [!]')


    if not os.path.isfile(file):
        print (Fore.LIGHTRED_EX+'[X] O arquivo nao existe no diretorio.')
        quit()

    elif not file.endswith('.txt'):
        print ('[!] Apenas ha suporte para .txt files.')
        quit()

    elif file == '':
        print (Fore.LIGHTRED_EX+'[X] Nome de arquivo invalido.')
        quit()

    else: # abre o arquivo e cria as 2 listas
        data_list = []
        f = open(file, 'r')
        senhas = []

        for z in f: # pesquisa na API e salva na variavel usando append, cada dado abaixo do outro
            z = z.strip()
            senhas.append(z)
            myApp = hibpwned.Pwned(z, 'HIBP_Pwd_Check', api)
            myBreaches = myApp.searchAllBreaches(truncate=False, unverified=True)

            if not '404' in str(myBreaches):  # caso a senha não esteja em uma lista de vazado, printa "(SENHA) vazada"
                print (Fore.LIGHTRED_EX+'[!] ' + z + ' foi vazado!')

            else:
                print(Fore.LIGHTBLUE_EX+'[!] Essa senha não foi vazada!')

def send_email():   
    api = '26274f6c776746909f7afee0f44e60b8' # KEY DO HAVEIBEENPWNED
    
    emailvzd = input(Fore.LIGHTYELLOW_EX+'[+] coloque seu email para receber o aviso: ') # variavel do email pra consultar
    data_list = []

    myApp = hibpwned.Pwned(emailvzd, 'HIBP_Email_Check', api)
    myBreaches = myApp.searchAllBreaches(truncate=False, unverified=True)

    if not '404' in str(myBreaches):  # caso o email não esteja em uma lista de vazado, printa "(EMAIL) não vazado"
        print (Fore.LIGHTRED_EX+'\n [!] ' + emailvzd + ' foi vazado!')

        for x in myBreaches:  # salva cada dado da variável na lista PAWNED[], separando por colunas.
            for y in x['DataClasses']:
                pawned = [emailvzd,x['Name'],y,x['BreachDate']]
                data_list.append(pawned)

    else:  # se n tiver salvo ele salva todas as colunas da ultima linha como null
        not_pawned = ['','','','']
        data_list.append(not_pawned) 
        sleep(1.5)   

    data = pandas.DataFrame(data_list ,columns= ['Email','Incidente','Dado Vazado','Data do Vazamento'])  # define o titulo de cada coluna

    print ('\n [+] Tarefa finalizada, email enviado!')    

    assunto = "Dados Vazados"
    remetente = "" # email do bot
    Senha = "" # senha do bot 
    emailaddr = [emailvzd] # email que desejar
    
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(remetente, Senha)
        for e in emailaddr:
            message = 'assunto: {}\n\n{}'.format( assunto, data_list)
            server.sendmail(remetente, e, message)
        server.quit()
    except:
        print("deu erro")

def about(dados):  #opcao de sobre
    print('')
    print('''
    [?] Sobre a ferramenta [?]
        |
        |-> [•] VAL.DIR é uma ferramenta de pesquisa de dados vazados na 
                internet, que usa como base a api do Haveibeenpwned para
                verificar se o email ou algo relacionado a ele foi vazado
                na internet.
                na ferramenta é possivel fazer consultas por meio individual
                e por wordlist (arquivo com varios emails, capaz de consultar
                varios emails por vez e mandar para uma planilia xlsx )

        ''')
