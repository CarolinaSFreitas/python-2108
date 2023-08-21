from colorama import init, Fore, Back
init(autoreset=True)

# print(Fore.BLUE+"Olá")
# print(Back.GREEN+"Olá 2")
# print(Fore.BLUE+Back.YELLOW+"Olá 3")

# constantes com as configurações do jogo
NUM_LINHAS = 6
NUM_COLUNAS = 7

# declara a matriz (vetor/lista) do jogo
jogo = []

# cria a matriz do jogo, com o número de linhas e colunas
# preenchidos (inicialmente) com vazio " "
def cria_jogo():
    for i in range(NUM_LINHAS):
        jogo.append([])
        for _ in range(NUM_COLUNAS):
            jogo[i].append(" ")        # vazio, indica posição não jogada


# mostra a matriz do jogo (desenha o tabuleiro)
def mostra_tabuleiro():
    print()
    for i, linha in enumerate(jogo, start=1):
        print(f"{i} |", end="")
        for casa in linha:
            if casa == "x":            
                print(Fore.BLUE+Back.YELLOW+" x ", end="")
            elif casa == "o":
                print(Fore.YELLOW+Back.BLUE+" o ", end="")
            else:
                print(f"   ", end="")
        print("|")
    print("  +---------------------+")
    print("    1  2  3  4  5  6  7")


# chama as funções de inicialização
cria_jogo()
mostra_tabuleiro()

print(Fore.BLUE+"\nJogo Connect 4")
print(Fore.YELLOW+"="*40)
print("Informe o número da coluna (1..7) ou 0 para sair")

# contador é usado para saber quem é o próximo jogador
# e também para saber se houve empate 
contador = 1

while True:
    # operador ternário do Python
    jogador = "x" if contador % 2 == 1 else "o"

    coluna = int(input(f"\nJogador {jogador}, informe a coluna: "))

    if coluna == 0:
        break

    linha = 5
    jogo[linha][coluna-1] = jogador
    contador += 1

    mostra_tabuleiro()
