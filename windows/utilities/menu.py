from utilities import colors
import os
colors.colors()
def option_menu():
    '''Option Menus, ask to user which option he wants'''
    print(colors.white +'\nPseudocódigo : 1\nFluxograma : 2'+ colors.reset_color)
    print()
    try:
        option = int(input(colors.white +'Escolha uma opção: '+ colors.reset_color)) 
    except TypeError:
        print(colors.red +'valor digitado invalido!'+ colors.reset_color)
    print()
    if option == 1:
        print()
        print(colors.green + "\n--- Pseudocódigo ---")
        print("Pseudocódigo (ou Português Estruturado) é uma forma de descrever um algoritmo")
        print("usando uma linguagem simples, que se assemelha à linguagem natural (como o português),")
        print("mas com uma estrutura organizada que facilita a conversão para uma linguagem de programação real.")
        print("Ele não possui uma sintaxe rígida e formal como as linguagens de programação,")
        print("focando na clareza da lógica e dos passos a serem seguidos.")
        print("Exemplo simples de pseudocódigo para somar dois números:")
        print("  INÍCIO")
        print("    LER numero1")
        print("    LER numero2")
        print("    soma = numero1 + numero2")
        print("    ESCREVER soma")
        print("  FIM"+colors.reset_color)
        print()

    elif option == 2:
        print()
        print(colors.green+"\n--- Fluxograma ---"+colors.reset_color)
        print(colors.white+"Fluxograma é uma representação gráfica de um algoritmo. Ele utiliza símbolos")
        print("geométricos padronizados para representar as diferentes instruções (ações, decisões,")
        print("entradas/saídas de dados, início/fim) e setas para indicar o fluxo de controle")
        print("e a sequência das operações.")
        print("É uma ferramenta visual poderosa para entender a lógica de processos complexos.")
        print("Principais símbolos:")
        print("  - Oval: Início ou Fim do algoritmo.")
        print("  - Retângulo: Processo ou instrução.")
        print("  - Losango: Decisão (condição com saídas Sim/Não).")
        print("  - Paralelogramo: Entrada ou Saída de dados.")
        print("  - Setas: Direção do fluxo."+ colors.reset_color)
        print()



def request_confirmation():
    """Solicita confirmação ao usuário para continuar ou não."""
    global continue_option
    while True:
        continue_option = input("Deseja continuar? [SIM/NÃO]: ").strip().upper()
        # Remove espaços e substitui "NÃO" por "NAO"
        continue_option = continue_option.replace(" ", "").replace("NÃO", "NAO")

        if continue_option in ["SIM", "NAO"]:
            break
        else:
            print("Opção inválida. Tente novamente.")

    if continue_option == "SIM":
        os.system("cls")  
        option_menu()
    