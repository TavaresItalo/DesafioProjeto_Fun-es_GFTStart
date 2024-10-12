
def calculaSaldo() :
    vitorias = int(input("Digite o número de vitórias: "))
    derrotas = int(input("Digite o número de derrotas: "))
    return vitorias - derrotas

def defineRanking(nomePlayer) :
    saldo = calculaSaldo()
    ranking = ""

    if(saldo <= 10) :
        ranking = "Ferro"
    elif (saldo >= 11 and saldo <= 20) :
        ranking = "Bronze"
    elif (saldo >= 21 and saldo <= 50) :
        ranking = "Prata"
    elif (saldo >= 51 and saldo <= 80) :
        ranking = "Ouro"
    elif (saldo >= 81 and saldo <= 90) :
        ranking = "Diamante"
    elif (saldo >= 91 and saldo <= 100) :
        ranking = "Lendário"
    else :
        ranking = "Imortal"

    exibeMensagem(saldo, ranking, nomePlayer)
    

def exibeMensagem(saldo, ranking, nomePlayer) :
    print(f"O jogador {nomePlayer} obteve um saldo de {saldo} e por isso foi rankeado como {ranking}")

nomePlayer = input("Digite o nome do player: ")
defineRanking(nomePlayer)
