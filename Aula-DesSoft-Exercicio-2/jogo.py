import random
from termcolor import colored
#'J♠', 'A♥', '4♣', '7♦'


def cria_baralho(): #Cria um baralho aleatório sem repetições
    cards = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']
    random.shuffle(cards)
    return cards
def display_baralho(deck):
    card_num = 1
    for i in deck:
        print(f"{card_num:2}. {i}")
        card_num += 1
def cor_naipe(naipe):
    
def extrai_naipe(carta):
    naipe = carta[-1]
    return naipe
def extrai_valor(carta):
    valor = carta[0:-1]
    return valor



baralho = cria_baralho()
display_baralho(baralho)