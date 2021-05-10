import random #A função shuffle() é necessária para o sorteio do baralho

#'♠', '♥', '♣', '♦' Template de naipes
#print(f"{cor}{texto}\033[00m") Template de cores

def cria_baralho(): 
    #Cria um baralho aleatório sem repetições
    cards = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥','A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠','A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦']
    random.shuffle(cards)
    return cards
def display_baralho(deck): 
    #Essa função dispõe o baralho, com uma carta por linha do terminal
    card_num = 1
    for i in deck:
        naipe = extrai_naipe(i)
        cor = cor_naipe(i)#Utilizamos códigos ANSI para gerar as cores do texto. A função cor_naipe retorna o código associado a cada naipe
        print(f"{card_num:2}. {cor}{i:3}\033[00m")#Usamos f-strings para formatar o texto, o código ANSI guardado na variável 'cor' muda a cor do texto posterior
        card_num += 1
def extrai_naipe(carta):
    #Recebendo a carta como string, retorna o último caracter do string, que é o naipe
    naipe = carta[-1]
    return naipe
def extrai_valor(carta):
    #Recebendo a carta como string, todos os caracteres do string exceto o último, separando o valor do naipe
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
    carta = baralho[origem] #Primeiramente guardamos o valor da carta a ser empilhada em uma variável
    baralho.remove(baralho[origem]) #Removemos a carta de origem para que seja empilhada no destino(Atenção: Se atualizarmos o valor do destino antes de remover a origem, o código quebra pois fica confuso em qual item deletar)  
    baralho[destino] = carta #Substituimos o valor do item na posição de destino pelo valor que desejamos empilhar
    return baralho
def possui_movimentos_possiveis(baralho):
    for i in baralho:
        movimentos = lista_movimentos_possiveis(baralho,baralho.index(i)) #Essa função é chamada para facilitar a achar os movimentos possíveis para cada carta. Se não houver nenhum movimento possível retornará uma lista vazia
        if movimentos == []:
            #Se a lista está vazia, não há movimentos possíveis para essa carta e passamos para a próxima no baralho
            None
        else:
            #Se a lista tiver qualquer valor que não vazio, há ao menos um movimento possível para essa carta. Não precisamos buscar as outras cartas já que só precisamos saber se existe ao menos um movimento possível
            return True
    return False #Se nenhuma carta tiver movimentos possíveis, o for loop completa e essa linha é executada e retorna o valor 'False'
def cor_naipe(carta):
    #Usando um dicionário, podemos retornar a cor associada com cada naipe chamando-o como uma chave do dicionário
    naipe = carta[-1]
    cores = {'♠':"\033[96m",'♥':"\033[91m",'♣':"\033[92m",'♦':"\033[93m"}
    return cores[naipe]

print("Paciência Acordeão")
while True:
    input("Aperte Enter para começar") #Esse input não está associado com nenhuma variável, somente existe para não bombardear o usuário com o baralho assim que abrir o programa
    continua = True
    fim = False #Criamos uma variavel para determinar se o jogo chegou a um fim
    while fim == False: 
        #Esse loop existe para podermos validar o baralho sem precisar passar pelo input incial várias vezes
        baralho = cria_baralho() #Cria o baralho inicial
        valido = possui_movimentos_possiveis(baralho) #Verifica se o baralho gerado é válido. Se for inválido o loop continua até um válido ser encontrado
        if valido == True:
            mudou = True #Essa variável guarda se uma operação modificou o baralho disposto no terminal
            while len(baralho) > 0: 
                #Esse loop continua até que o baralho tenha comprimento de 1(caso em que o jogador ganhou), ou seja interrompido prematuramente(o jogador perdeu, pois não há mais movimentos possíveis)
                if mudou == True:
                    #Se alguma ação mudou o baralho no loop anterior, atualizamos a visualização e o tamanho do baralho
                    display_baralho(baralho)
                    tamanho = len(baralho)
                while True:
                    #Esse loop valida a entrada do usuário. Se a entrada for válida o loop é quebrado, se não for, envia um aviso ao jogador e pede a entrada novamente
                    entrada = int(input(f"Entre um valor entre 1 e {tamanho}: "))
                    if entrada in range(1,tamanho+1):
                        break
                    else:
                        print("Por favor entre um número válido")
                carta = entrada - 1 #Temos que subtrair 1 do número entrado já que a lista começa em 0 mas a visualização começa em 1
                movimentos = lista_movimentos_possiveis(baralho, carta) #Chamamos a função para listar todos os movimentos possíveis da carta selecionada
                if len(movimentos) == 0: 
                    #Se a lista estiver vazia, não há movimentos possiveis, e pedimos que o usuário escolha outra carta e retornamos ao input
                    print("Não há movimentos possíveis para essa carta, por favor escolha outra")
                    mudou = False #O baralho não foi modificado nessa iteração, a variável é dada como False
                elif len(movimentos) == 2:
                    #Se a lista tiver dois movimentos possíveis, precisamos perguntar ao usuário qual movimento quer fazer
                    cor = cor_naipe(baralho[carta-1])
                    print(f"1. {cor}{baralho[carta-1]}\033[00m")
                    cor = cor_naipe(baralho[carta-3])
                    print(f"3. {cor}{baralho[carta-3]}\033[00m")
                    while True: #Esse loop valida a entrada, e funciona da mesma forma que o loop da entrada da carta de origem
                        escolha = int(input("Por favor escolha a carta em que quer empilhar(1 ou 3): "))
                        if escolha in [1,3]:
                            break
                        print("Por favor entre uma alternativa válida")
                    destino = carta - escolha
                    baralho = empilha(baralho, carta, destino) #Empilhamos a carta de origem na carta de destino
                    mudou = True
                else:
                    #Se a lista não estiver vazia, e não possuir exatamente dois movimentos, possui somente um e portanto podemos fazê-lo diretamente
                    destino = carta - movimentos[0] #Como 'movimentos' é uma lista de um item, pedimos seu único item, de índice 0
                    baralho = empilha(baralho, carta, destino)
                    mudou = True
                continua = possui_movimentos_possiveis(baralho) #Ao fim de cada iteração, verificamos se ainda existem movimentos possíveis. Se não houverem, quebramos o loop
                if continua == False:
                    ganha = False
                    break 
                
            if ganha == False:
                fim = True
                print("Não há mais movimentos possíveis. Tente novamente")
                print("")
                print("")
            else:
                fim = True
                print("Parabéns! Você ganhou!")
                print("")
                print("")