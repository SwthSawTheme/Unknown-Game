
import time
import os


def Main():
    
    user1 = Users()
    
    while True:
        Unknown()
        menu = ['\n1.Entrar','2.Registrar','3.Sair']
        for item in menu:
            print(item)
            time.sleep(0.5)
        escolha = input('\nC:/> ')
        
        if escolha == '1':
            time.sleep(0.5)
            os.system('clear')
            user1.Login()
            
        elif escolha == '2':
            time.sleep(0.5)
            os.system('clear')
            user1.Register()
            
        else:
            
            break
            quit()