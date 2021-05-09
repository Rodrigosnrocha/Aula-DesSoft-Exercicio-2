import random
#'J♠', 'A♥', '4♣', '7♦'


def cria_baralho(): 
    #Cria um baralho aleatório sem repetições
    cards = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']
    random.shuffle(cards)
    return cards
def display_baralho(deck): 
    #Essa função 
    card_num = 1
    for i in deck:
        print(f"{card_num:2}. {i:3}")
        card_num += 1
def extrai_naipe(carta):
    naipe = carta[-1]
    return naipe
def extrai_valor(carta):
    valor = carta[0:-1]
    return valor
def lista_movimentos_possiveis(baralho,index):
    carta = baralho[index]
    possiveis = []
    if index == 0: 
        #Se uma carta não tiver antecessores, sabemos que não haverá movimentos possíveis. portanto retornamos a lista ainda vazia
        return possiveis
    elif index < 3: 
        #Se o índice for menor que 3, sabemos que não terá terceira carta anterior, portanto comparamos somente à vizinha
        if (extrai_valor(carta) in baralho[index-1]) or (extrai_naipe(carta) in baralho[index-1]):#Comparamos o valor e o naipe da carta escolhida com os equivalentes na carta vizinha, se um dos dois for igual, retornamos que é um movimento possível
            possiveis.append(1)
            return possiveis
        else: 
            #Se não tiver valor ou naipe igual à carta antecedente, retornamos a lista vazia
            return possiveis
    else: 
        #Se tiver índice maior que 3, podemos comparar com a carta vizinha e a terceira anterior
        if (extrai_valor(carta) in baralho[index-1]) or (extrai_naipe(carta) in baralho[index-1]):#Comparamos o valor e o naipe da carta escolhida com os equivalentes na carta vizinha, se um dos dois for igual, retornamos que é um movimento possível
            possiveis.append(1)
        if (extrai_valor(carta) in baralho[index-3]) or (extrai_naipe(carta) in baralho[index-3]):#O mesmo procedimento é feito com a terceira carta anterior
            possiveis.append(3)
        return possiveis
def empilha(baralho,origem,destino):
    carta = baralho[origem]
    baralho.remove(baralho[origem])   
    baralho[destino] = carta
    return baralho

baralho = cria_baralho()
while len(baralho) > 0:
    display_baralho(baralho)
    entrada = input(f"Entre um valor entre 1 e {len(baralho)}: ")
    carta = int(entrada) - 1
    movimentos = lista_movimentos_possiveis(baralho, carta)
    if len(movimentos) == 0:
        print("Não há movimentos possíveis para essa carta, por favor escolha outra")
    elif len(movimentos) == 2:
        print(f"1. {baralho[carta-1]}")
        print(f"3. {baralho[carta-3]}")
        escolha = int(input("Por favor escolha a carta em que quer empilhar(1 ou 3): "))
        destino = carta - escolha
        baralho = empilha(baralho, carta, destino)
    else:
        destino = carta - movimentos[0]
        baralho = empilha(baralho, carta, destino)