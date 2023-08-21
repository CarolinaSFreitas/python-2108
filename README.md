# Connect 4 em Python aula do dia 21/08 | Matrizes

## Terceira aula de Python da disciplina Algoritmos e Estrutura de Dados I - CONNECT 4 - Matrizes e Colorama - 21/08/2023

### Explicaçãozinha do ChatGPT:

"Claro, vou explicar o código para você passo a passo:

1. `from colorama import init, Fore, Back`: Aqui, estamos importando do módulo `colorama` algumas funcionalidades para permitir a manipulação de cores no terminal.

2. `init(autoreset=True)`: Essa linha inicializa o `colorama` e garante que as configurações de cores voltem ao normal após cada uso.

3. Comentários:
   - `# print(Fore.BLUE+"Olá")`: Isso é um exemplo de como usar a coloração do `colorama`. O texto "Olá" seria impresso com a cor azul.
   - `# print(Back.GREEN+"Olá 2")`: Aqui, o fundo da impressão é colorido em verde.
   - `# print(Fore.BLUE+Back.YELLOW+"Olá 3")`: Aqui, tanto o texto quanto o fundo da impressão têm cores diferentes.

4. `NUM_LINHAS = 6` e `NUM_COLUNAS = 7`: Essas são constantes que definem o tamanho do tabuleiro do jogo Connect 4. O tabuleiro terá 6 linhas e 7 colunas.

5. `jogo = []`: Isso declara uma lista vazia chamada `jogo`, que será usada para representar o tabuleiro do Connect 4.

6. `cria_jogo()`: Essa função é usada para criar a matriz do jogo, preenchida inicialmente com espaços em branco.

7. `mostra_tabuleiro()`: Essa função é usada para imprimir o estado atual do tabuleiro do jogo.
8. Ela itera através da matriz `jogo` e imprime cada célula com a cor apropriada, dependendo se é um "x" (jogador 1), um "o" (jogador 2) ou um espaço em branco.

9. `contador = 1`: Aqui, um contador é definido para acompanhar o turno dos jogadores e verificar se houve um empate.

10. `while True:`: Inicia um loop infinito que permite que o jogo seja jogado indefinidamente, até que o jogador decida sair.

11. O operador ternário `jogador = "x" if contador % 2 == 1 else "o"` determina qual jogador deve jogar com base no valor do contador.
12. Se o contador for ímpar, o jogador será "x", caso contrário, será "o".

13. `coluna = int(input(f"\nJogador {jogador}, informe a coluna: "))`: Solicita ao jogador que insira a coluna onde deseja colocar sua peça.

14. `if coluna == 0: break`: Se o jogador inserir 0, o loop é interrompido e o jogo termina.

15. `linha = 5`: Aqui, a linha é definida como 5 porque as linhas estão indexadas de 0 a 5.

16. `jogo[linha][coluna-1] = jogador`: A posição escolhida pelo jogador é marcada com a peça correspondente.

17. `contador += 1`: O contador é incrementado para alternar os jogadores.

18. `mostra_tabuleiro()`: O tabuleiro atualizado é exibido novamente após cada jogada.

Isso resume o funcionamento do código, onde jogadores alternam, fazem suas jogadas e o tabuleiro é atualizado e exibido. 
É um ótimo exemplo de como você pode usar loops, estruturas condicionais e funções para criar um jogo simples em Python.

Claro, vou explicar as mudanças no código que você forneceu:

1. `def linha_disponivel(coluna)`: Essa é uma nova função que verifica a primeira linha vazia em uma coluna específica. Ela percorre as linhas de baixo para cima até encontrar a primeira linha disponível. Se a coluna estiver cheia, a função retorna -1.

2. `def verifica_vencedor(simbolo)`: Essa função verifica se um jogador venceu, procurando por quatro símbolos consecutivos na horizontal.

3. No início do loop `while True`, após receber a entrada da coluna do jogador, agora o código verifica se a coluna informada está fora dos limites (maior que `NUM_COLUNAS`) ou igual a 0 (indicando saída do jogo). Se sim, o loop é interrompido e o jogo termina.

4. Em seguida, a linha disponível para a jogada é obtida usando a função `linha_disponivel(coluna-1)`, onde `coluna-1` é usado para ajustar para o índice base 0.

5. Se `linha` for -1, isso significa que a coluna está cheia, então uma mensagem é exibida informando ao jogador que a coluna está preenchida.

6. Caso contrário, a posição é atualizada com o símbolo do jogador e o contador é incrementado.

7. Após cada jogada, o tabuleiro é mostrado novamente.

8. Finalmente, o código verifica se o jogador atual venceu usando a função `verifica_vencedor(jogador)`. Se o jogador venceu, uma mensagem é exibida e o loop é interrompido.

Essas mudanças adicionaram a funcionalidade de verificar se um jogador venceu ao conectar quatro de seus símbolos consecutivos na horizontal. Isso adiciona um elemento de vitória ao jogo Connect 4, tornando-o mais interessante e desafiador."



A saída no terminal:
![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/8057d1e7-9e3e-45eb-9949-4c93ab10ed2a)
![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/03b9d750-c12f-41c9-8402-ed1ac37f6dfb)

## Lembretes:

* Instalar o Colorama (https://www.pythonpool.com/python-colorama/):
`` python.exe -m pip install colorama ``

* Exemplo de como usa o Colorama:

* ![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/00ba3941-1010-4891-bc43-e61863334b63)

* Pra executar o .py `` python connect4.py ``

* 
