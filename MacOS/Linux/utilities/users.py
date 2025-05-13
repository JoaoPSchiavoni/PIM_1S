from utilities import colors
colors.colors()

def get_user_info():
    '''get user name, age'''
    from os import system
    print()
    system('clear')
    print("===" * 20)
    print("BEM-VINDO À PLATAFORMA DE EDUCAÇÃO DIGITAL DA NOSSA ONG!")
    print("===" * 20)
    while True:
        name = input(colors.white + 'Digite seu nome: ' + colors.reset_color).strip()
        if name:
            break
        else:
            print(colors.red + 'Nome inválido. Tente novamente.' + colors.reset_color)
    while True:
        try:
            age = int(input(colors.white +'Digite sua idade: '+ colors.reset_color))
            break
            
        except ValueError:
            print (colors.red+'Valor digitado Invalido'+colors.reset_color)
    return name
    
    
def welcome(name):
    '''gives welcome to user'''
    print()
    print(colors.green+ f"Seja bem vindo {name}" + colors.reset_color)

def user_consentiment(name):
    '''ask to user if he agree with terms'''
    global agreement
    law = colors.white+'Lei nº 13.709/2018'+colors.reset_color
    print()
    print(f'''TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAIS\n
    Nós, Estudantes de Análise e Desenvolvimento de Sistemas da Universidade Paulista de Ribeirão Preto,\n      estamos comprometidos com a proteção dos seus dados pessoais.De acordo com a LGPD {law}, \n   solicitamos sua autorização para tratá-los conforme as condições abaixo.\n
    1. Dados coletados: Nome, e-mail, telefone, endereço e idade.
    2. Finalidade: Comunicação, personalização e cumprimento legal.
    3. Segurança: Seus dados são protegidos contra acessos não autorizados.
    4. Direitos do usuário: Você pode acessar, corrigir ou excluir seus dados a qualquer momento.\n
    Caso concorde, digite 'ACEITO'. Para mais detalhes, consulte nossa Política de Privacidade.\n''')
    print()
     #if the user agrees with the terms, he can continue
    agreement = ''
    while agreement not in ['ACEITO', 'NAO']:
        #error message:
        agreement = input(colors.white +'Se Concorda digite [ACEITO] ou se Discorda digite [NAO]: '+ colors.reset_color).upper().replace(' ', '')

        if agreement != 'ACEITO' and agreement != 'NAO':
            print(colors.red +'Opção inválida. Tente novamente.'+ colors.reset_color)
        
        print()
        if agreement == 'ACEITO':
            from utilities import info, menu
            import os
            from time import sleep
            print()
            info.text_TI()
            print()
            sleep(1)
            menu.option_menu()
            while True:
                menu.request_confirmation()
                if menu.continue_option == 'NAO':
                    print("\nEntendido. Seus dados não serão utilizados para análise estatística.")
                    print("Você será redirecionado(a) para o início.")
                    break
            sleep(1.5)
            os.system('clear')







'''class Usuario:
    def __init__(self):
        self.nome = self.get_nome()
        self.idade = self.get_idade()
        self.consentimento = self.get_consentimento()

    def get_nome(self):
        return input("Digite seu nome: ")

    def get_idade(self):
        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if idade >= 0:
                    return idade
                else:
                    print("Por favor, insira uma idade válida.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    def get_consentimento(self):
        opcao = input(f"{self.nome}, deseja continuar? [S/N]: ").upper()
        while opcao not in ['S', 'N']:
            opcao = input("Entrada inválida. Digite 'S' para Sim ou 'N' para Não: ").upper()
        return opcao'''

