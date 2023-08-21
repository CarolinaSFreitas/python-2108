# Connect 4 em Python aula do dia 21/08 | Matrizes

## Terceira aula de Python da disciplina Algoritmos e Estrutura de Dados I - CONNECT 4 - Matrizes e Colorama - 21/08/2023

### Explicaçãozinha do ChatGPT:

"Claro, vou explicar o código para você passo a passo:

1. `from colorama import init, Fore, Back`: Importa o módulo `colorama` para permitir a manipulação de cores no terminal.

2. `init(autoreset=True)`: Inicializa o `colorama` com a configuração `autoreset=True`, que garante que as configurações de cores voltem ao normal após cada uso.

3. Comentários: Vários comentários foram adicionados no código para explicar o que cada parte do código faz.

4. Constantes: `NUM_LINHAS` e `NUM_COLUNAS` são definidas para determinar o tamanho do tabuleiro do Connect 4.

5. Matriz do Jogo: A matriz `jogo` é declarada como uma lista vazia, que será usada para representar o tabuleiro do jogo.

6. Função `cria_jogo()`: Essa função preenche a matriz do jogo com espaços em branco, criando um tabuleiro vazio.

7. Função `mostra_tabuleiro()`: Essa função exibe o estado atual do tabuleiro do jogo, colorindo as peças de acordo com os jogadores (x e o).

8. Função `linha_disponivel(coluna)`: Essa função verifica a primeira linha vazia em uma coluna específica, percorrendo de baixo para cima.

9. Função `verifica_vencedor(simbolo)`: Essa função verifica as quatro direções possíveis para determinar se um jogador ganhou o jogo.

10. Inicialização do Jogo: Chama a função `cria_jogo()` e `mostra_tabuleiro()` para inicializar e exibir o tabuleiro vazio.

11. Loop Principal (`while True`): Aqui, o jogo começa em um loop infinito que permite que os jogadores façam jogadas até que o jogo termine.

12. Operador Ternário: O operador ternário decide qual jogador é o próximo com base no contador, alternando entre "x" e "o".

13. Entrada do Jogador: Solicita ao jogador que insira a coluna onde deseja colocar sua peça.

14. Verificações:
   - Verifica se o jogador escolheu sair (coluna 0) ou uma coluna inexistente (`coluna > NUM_COLUNAS`) para interromper o loop.
   - Usa a função `linha_disponivel(coluna-1)` para encontrar a linha disponível na coluna escolhida.
   - Se a coluna estiver cheia (`linha == -1`), exibe uma mensagem informando ao jogador.
   - Caso contrário, atualiza o tabuleiro com a jogada do jogador e incrementa o contador.

15. Verificação de Vitória ou Empate: Após cada jogada, verifica se o jogador atual venceu ou se houve empate. Se algum jogador vencer ou se todas as posições forem preenchidas, o jogo é encerrado.

Esse código é uma implementação completa e funcional do jogo Connect 4, incluindo verificação de vitória em várias direções e a detecção de empates."



A saída no terminal:
![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/8057d1e7-9e3e-45eb-9949-4c93ab10ed2a)
![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/03b9d750-c12f-41c9-8402-ed1ac37f6dfb)

## Lembretes:

* Instalar o Colorama (https://www.pythonpool.com/python-colorama/):
`` python.exe -m pip install colorama ``

* Exemplo de como usa o Colorama:

* ![image](https://github.com/CarolinaSFreitas/python-2108/assets/99994934/00ba3941-1010-4891-bc43-e61863334b63)

* Pra executar o .py `` python connect4.py ``

