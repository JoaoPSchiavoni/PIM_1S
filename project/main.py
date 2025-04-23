import os
from utilities import colors, users, info, menu
colors.colors()

while True:
    name = users.get_user_info()
    #precisa criar uma funcao para pegar a idade do usuario
    users.welcome(name)
    users.user_consentiment(name)
    
    print()
    if users.agreement == 'ACEITO':
        from time import sleep
        print()
        info.text_TI()
        print()
        sleep(1)
        print(colors.white +'\nPseudocódigo : 1\nFluxograma : 2'+ colors.reset_color)
        print()
        try:
            option = int(input(colors.white +'Escolha uma opção: '+ colors.reset_color)) 
        except TypeError:
            print(colors.red +'valor digitado invalido!'+ colors.reset_color)
        print()
        menu.option_menu(option)
        menu.request_confirmation()
        sleep(1.5)
        os.system('clear')


        
       