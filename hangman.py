##Rodrigo Drumond Valente
##Jogo da forca
##Manipulação de arquivos, loops...
##25/05/2023

from random import *

#Iniciando variavéis

palavras = []
palavra_tentativa = []
acerto = 0
chances = 6

#Abrindo arquivo com palavras do dicionário

with open("br-sem-acentos.txt", "r", encoding="UTF-8") as arquivo:

    #jogando palavras do dicionario para uma lista
    palavras = arquivo.readlines()

    #tirando o \n no final de cada palavra e jogando a lista para outra variável (nova_lista) após isso
    nova_lista = []

    for palavra in palavras:
        nova_lista.append(palavra.replace("\n", ""))

    #sorteando uma palavra para o usuário tentar acertar
    sorteio = randint(0, 261796)

    palavra_sorteada = nova_lista[sorteio]

    print(palavra_sorteada)

    #preenchendo a palavra_tentativa com "-" para cada letra que a palavra sorteada tiver
    for i in range(len(palavra_sorteada)):
        palavra_tentativa.append("-")

    print(palavra_sorteada == palavra_sorteada)

    #Loop do jogo em si
    while acerto != len(palavra_sorteada) and (chances > 0):
        posicao = -1
        #input para o usuário tentar acertar uma letra
        letra_escolhida = input(f"-----Forca-----\n{palavra_tentativa}\nDigite uma letra:\nChances: {chances}\n---------------")
        #se a letra existir na palavra sorteada, preencher o espaço em branco da variável tentativa e contabilizar um acerto
        for i in range(len(palavra_tentativa)):
            if letra_escolhida in palavra_sorteada[i]:
                posicao = i
                palavra_tentativa[posicao] = letra_escolhida
                acerto += 1
        #a cada erro uma chance é retirada
        if posicao == -1:
            chances -= 1
        #Se o número de letras acertadas for o mesmo número de letras da palavra sorteada, o usuário acertou
        if acerto == len(palavra_sorteada):
            print(f"Você acertou! A palavra era: {palavra_sorteada}")
        #Se o número de chances for igual a zero, o usuário errou a palavra
        if chances == 0:
            print(f"Você errou! Sem mais chances.\n A palavra era: {palavra_sorteada}")