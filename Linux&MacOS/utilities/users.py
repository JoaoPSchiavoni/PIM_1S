from utilities import colors
import os
colors.colors()

def header():
    '''header of the program'''
    
    print()
    os.system('clear')
    text = colors.white + 'PLATAFORMA DE EDUCAÇÃO DIGITAL' + colors.reset_color
    print(colors.white + "==" * 25 + colors.reset_color)
    print(text)
    print(colors.white + "==" * 25 + colors.reset_color)

def get_user_info():
    '''get user name, age'''
    print()
    header()
    while True:
        name = input(colors.white + 'Digite seu nome: ' + colors.reset_color).strip().upper()
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
    print(colors.white + '==' * 40 + colors.reset_color)
    print( colors.green + f'BEM-VINDO {name} À PLATAFORMA DE EDUCAÇÃO DIGITAL DA NOSSA ONG!' + colors.reset_color)
    print(colors.white + "==" * 40 + colors.reset_color)
   

def user_consentiment(name):
    '''ask to user if he agree with terms'''
    global agreement
    law = colors.white+'Lei nº 13.709/2018'+colors.reset_color
    print()
    print(f'TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAIS')
    print('Nós, Estudantes de Análise e Desenvolvimento de Sistemas da Universidade Paulista de Ribeirão Preto,')

    print(f'estamos comprometidos com a proteção dos seus dados pessoais. Consoante, a {law} (Lei Geral de Proteção de Dados),')
    print('solicitamos sua autorização para tratá-los conforme as condições abaixo.')
    print('1. Dados coletados: Nome, idade e tempo de uso.')
    print('2. Finalidade: Uso para estatísticas e armazenamento.')
    print('3. Segurança: Seus dados são protegidos contra acessos não autorizados.')
    print('4. Direitos do usuário: Você pode acessar, corrigir ou excluir seus dados a qualquer momento.')
    print('5. Compartilhamento: Seus dados não serão compartilhados com terceiros sem sua autorização.')
    print('6. Prazo de armazenamento: Seus dados serão mantidos enquanto forem necessários para a finalidade.')
    print('7. Consentimento: Você pode revogar seu consentimento a qualquer momento.')
    print()
    print('Caso concorde, digite "ACEITO". Para mais detalhes, consulte nossa Política de Privacidade.')
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
            from time import sleep
            print()
            info.text_TI()
            print()
            
            os.system('clear')
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

