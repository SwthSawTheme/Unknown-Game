import time

class Users:
    def __init__(self):
        self.usuarios = {}
    
    def Register(self):
        print('Registre um novo usuário\n')
        login = input('Login:')
        password = input('Password:')
        
        if login in self.usuarios:
            print('Usuário ja cadastrado!')
        else:
             self.usuarios[login] = password
             print('\nCadastrado com Sucesso!')
    
    def Login(self):
        print('Rede Inc')
        
        login = input('\nLogin:')
        
        if login in self.usuarios:
            password = input('Password:')
            if password == self.usuarios[login]:
                print('Senha invalida!')
        else:
            print('Usuario não cadastrado!')
            
        
            
users = Users()

users.Register()
