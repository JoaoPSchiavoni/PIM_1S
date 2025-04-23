from utilities import colors
colors.colors()

def get_user_info():
    '''get user name'''
    print()
    name = input(colors.white + "Digite seu nome: ")

    while True:
        try:
            age = int(input('Digite sua idade: '))
            break
            return age
        except ValueError:
            print ('Valor digitado Invalido')
    return name
    
    
def welcome(name):
    '''gives welcome to user'''
    print()
    print(colors.green+ f"Seja bem vindo {name}" + colors.reset_color)

def user_consentiment(name):
    '''ask to user if he agree with terms'''
    global agreement
    print()
    print(f'''TERMO DE CONSENTIMENTO PARA TRATAMENTO DE DADOS PESSOAIS\n
    Nós, Estudantes de Análise e Desenvolvimento de Sistemas da Universidade Paulista de Ribeirão Preto,\n      estamos comprometidos com a proteção dos seus dados pessoais.De acordo com a LGPD, \n   solicitamos sua autorização para tratá-los conforme as condições abaixo.\n
    1. Dados coletados: Nome, e-mail, telefone, etc.
    2. Finalidade: Comunicação, personalização e cumprimento legal.
    3. Segurança: Seus dados são protegidos contra acessos não autorizados.
    4. Direitos do usuário: Você pode acessar, corrigir ou excluir seus dados a qualquer momento.\n
    Caso concorde, digite 'ACEITO'. Para mais detalhes, consulte nossa Política de Privacidade.\n''')
    print()
     #se o Usuario digitar N (não) o Codigo volta a pedir o Nome do usuario
    agreement = input(colors.white +'Se Concorda digite [ACEITO] ou se Discorda digite [NAO]: '+ colors.reset_color).upper().replace(' ', '')
    while agreement not in ['ACEITO', 'NAO']:
        #tratamento de erro:
        print(colors.red +'Opção inválida. Tente novamente.'+ colors.reset_color)
        print()
        agreement = input(colors.white + 'Se Concorda digite [ACEITO] ou se Discorda digite [NAO]: '+ colors.reset_color).upper().replace(' ', '')







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