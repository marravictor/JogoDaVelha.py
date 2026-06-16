def validaPosicao(entrada):
    entradaValida = False
    if len(entrada) != 3:
        return False
    
    opcoes_validas = ["0", "1", "2"]
    primeiro_valido = entrada[0] in opcoes_validas
    terceiro_valido = entrada[2] in opcoes_validas

    if primeiro_valido and terceiro_valido:
        return True
    else:
        return False

havencedor  = False
tabuleiro = [0, 0, 0, 
             0, 0, 0, 
             0, 0, 0]
jogadorDaVez = 1  

rodada = 1

jogada = ""

linha = 0
coluna = 0

while True:
    print("\n--- JOGO DA VELHA ---")
    print(f"[ {tabuleiro[0]} ] [ {tabuleiro[1]} ] [ {tabuleiro[2]} ]")
    print(f"[ {tabuleiro[3]} ] [ {tabuleiro[4]} ] [ {tabuleiro[5]} ]")
    print(f"[ {tabuleiro[6]} ] [ {tabuleiro[7]} ] [ {tabuleiro[8]} ]")
    print("-----------------\n")

    print(f"Jogador {jogadorDaVez}, digite a sua jogada (Ex: 0,1): ")
    jogada = input()
    
    if validaPosicao(jogada):
        linha = int(jogada[0])
        coluna = int(jogada[2])

        posicao_tabuleiro = 3 * linha + coluna

        if tabuleiro[posicao_tabuleiro] == 0:
            tabuleiro[posicao_tabuleiro] = jogadorDaVez

            j = jogadorDaVez

            ganhou_linha = (tabuleiro[0]==j and tabuleiro[1]==j and tabuleiro[2]==j) or \
                           (tabuleiro[3]==j and tabuleiro[4]==j and tabuleiro[5]==j) or \
                           (tabuleiro[6]==j and tabuleiro[7]==j and tabuleiro[8]==j)
            ganhou_coluna = (tabuleiro[0]==j and tabuleiro[3]==j and tabuleiro[6]==j) or \
                            (tabuleiro[1]==j and tabuleiro[4]==j and tabuleiro[7]==j) or \
                            (tabuleiro[2]==j and tabuleiro[5]==j and tabuleiro[8]==j)
            ganhou_diagonal = (tabuleiro[0]==j and tabuleiro[4]==j and tabuleiro[8]==j) or \
                              (tabuleiro[2]==j and tabuleiro[4]==j and tabuleiro[6]==j)

            if ganhou_linha or ganhou_coluna or ganhou_diagonal:
                havencedor = True
            else:
                if jogadorDaVez == 1:
                    jogadorDaVez = 2
                else:
                    jogadorDaVez = 1

            rodada = rodada + 1
        else:
            print("Essa posição já está ocupada! Tente novamente.")
    else:
        print("Sua jogada foi inválida! Use o padrão (Linha,Virgula,Coluna), ex: 1,2")

    if havencedor or rodada > 9:
        break

print("\n=== FIM DE JOGO ===")
if havencedor:
    print(f"Parabéns pela vitória, Jogador {jogadorDaVez}!")
else:
    print("Deu Velha!") 

print(f"[ {tabuleiro[0]} ] [ {tabuleiro[1]} ] [ {tabuleiro[2]} ]")
print(f"[ {tabuleiro[3]} ] [ {tabuleiro[4]} ] [ {tabuleiro[5]} ]")
print(f"[ {tabuleiro[6]} ] [ {tabuleiro[7]} ] [ {tabuleiro[8]} ]")