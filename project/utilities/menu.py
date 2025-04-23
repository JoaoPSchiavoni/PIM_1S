from utilities import colors
colors.colors()
def option_menu(option):
    '''Option Menus, ask to user which option he wants'''

    if option == 1:
        print()
        print(colors.green +'Você escolheu Pseudocódigo'+ colors.reset_color)
        print(colors.white +'Pseudocódigo é uma forma de descrever algoritmos, funções ou processos usando uma linguagem natural. É uma ferramenta de aprendizagem e raciocínio que ajuda a compreender os passos lógicos de um algoritmo'+ colors.reset_color)
        print()

    elif option == 2:
        print()
        print(colors.green +'Você escolheu Fluxograma'+ colors.reset_color)
        print(colors.white+ 'Fluxograma é uma representação gráfica de um processo ou algoritmo. Ele usa formas geométricas e setas para mostrar a sequência de passos e decisões necessárias para alcançar um resultado.'+ colors.reset_color)
        print()

def request_confirmation():
    option = input('Deseja continuar? [S/N]: ').upper()
    while option not in ['S', 'N']:
        option = input('Deseja continuar? [S/N]: ').upper()
        if option == 'N':
            break
