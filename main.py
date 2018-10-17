###################################
# Criador: Gabriel Henrique Silva #
# Data: 21.01.2018                #
# Versão: 1.4                     #
# Python 3.5.2                    #
###################################


#Bibliotecas usadas
import pygame
from pygame.locals import *
from random import randint
from time import sleep
from pygame import mixer

#Iniciando o pygame e mixer
pygame.init()
mixer.init()

#Tamanho de tela
tela_largura = 700
tela_altura = 500
tela = pygame.display.set_mode((tela_largura, tela_altura))
pygame.display.set_caption('JOKENPO')

#Cores usadas
vermelho = (255, 0, 0)
preto = (0, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
branco = (255, 255 ,255)

#imagem pedra
imgPedra = pygame.image.load('pedra.png').convert_alpha()
img_pedra = pygame.transform.scale(imgPedra, (300, 150))

#imagem papel
imgPapel = pygame.image.load('papel.png').convert_alpha()
img_papel = pygame.transform.scale(imgPapel, (300, 150))

#imagem tesoura
imgTesoura = pygame.image.load('tesoura.png').convert_alpha()
img_tesoura = pygame.transform.scale(imgTesoura, (300, 150))

#Definindo a musica a de fundo
mixer.music.load('song.mp3')
mixer.music.play(-1)

#Definição de texto geral
def Text_Objects(text, font):
    textSurface = font.render(text, True, preto)
    return textSurface, textSurface.get_rect()

#Botões de escolha
def button_pedra(x, y, w, h, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h+5))
        if click[0] == 1 and action != None:
            if action == 'PEDRA':
                pedra_result()
                
    tela.blit(img_pedra, (x, y, w, h))
    
def button_papel(x, y, w, h, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h+5))
        if click[0] == 1 and action != None:
            if action == 'PAPEL':
                papel_result()
                
    tela.blit(img_papel, (x, y, w, h))

def button_tesoura(x, y, w, h, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, preto, (x, y, w, h+5))
        if click[0] == 1 and action != None:
            if action == 'TESOURA':
                tesoura_result()
                
    tela.blit(img_tesoura, (x, y, w, h))
    
#Tela de escolha
def tela_escolha():

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)
        
        button_pedra(200, 5, 300, 150, 'PEDRA')
        button_papel(200, 175, 300, 150, 'PAPEL')
        button_tesoura(200, 340, 300, 150, 'TESOURA')
        volt_button('Voltar', 30, 420, 100, 50, (0, 0, 200), azul, 'Voltar')
        
        pygame.display.update()
        
    pygame.quit()
    quit()

#Resultado caso a escolha for PEDRA
def pedra_result():

    #Resposta da IA
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você:', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot:', True, preto)
        tela.blit(palavra, (40, 420))
        
        tela.blit(img_pedra, (200, 5))
        if sistema == 0:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('EMPATE', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_pedra, (200, 340))
        
        elif sistema == 1:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('PERDEU', True, vermelho)
            tela.blit(palavra, (300, 250))
            tela.blit(img_papel, (200, 340))
            
        elif sistema == 2:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('VENCEU', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_tesoura, (200, 340))

        pygame.display.update()
        sleep(2)
        tela_escolha()

#Resultado caso a escolha for PAPEL
def papel_result():
    
    #Resposta da IA
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você:', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot:', True, preto)
        tela.blit(palavra, (40, 420))
        
        tela.blit(img_papel, (200, 5))
        
        if sistema == 0:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('VENCEU', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_pedra, (200, 340))
        
        elif sistema == 1:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('EMPATE', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_papel, (200, 340))
            
        elif sistema == 2:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('PERDEU', True, vermelho)
            tela.blit(palavra, (300, 250))
            tela.blit(img_tesoura, (200, 340))

        pygame.display.update()
        sleep(2)
        tela_escolha()

#Resultado caso a escolha for TESOURA
def tesoura_result():

    #Resposta da IA
    sistema = randint(0, 2)

    sair = False

    while not sair:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Você:', True, preto)
        tela.blit(palavra, (40, 60))

        texto = pygame.font.Font('freesansbold.ttf', 30)
        palavra = texto.render('Bot:', True, preto)
        tela.blit(palavra, (40, 420))
        
        tela.blit(img_tesoura, (200, 5))
        if sistema == 0:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('PERDEU', True, vermelho)
            tela.blit(palavra, (300, 250))
            tela.blit(img_pedra, (200, 340))
        
        elif sistema == 1:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('VENCEU', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_papel, (200, 340))
            
        elif sistema == 2:
            texto = pygame.font.Font('freesansbold.ttf', 30)
            palavra = texto.render('EMPATE', True, preto)
            tela.blit(palavra, (300, 250))
            tela.blit(img_tesoura, (200, 340))

        pygame.display.update()
        sleep(2)
        tela_escolha()

#Botão de voltar para tela de inicio
def volt_button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'Voltar':
                tela_inicio()

    else:
        pygame.draw.rect(tela, ic, (x, y, w, h))

    texto = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = Text_Objects(msg, texto)
    TextRect.center = ((x+(w/2), (y+(h/2))))
    tela.blit(TextSurf, TextRect)

#"Jogar" e "Sair" da tela de inicio
def button(msg, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(tela, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == 'Jogar':
                tela_escolha()
            elif action == 'Sair':
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(tela, ic, (x, y, w, h))
        
    texto = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = Text_Objects(msg, texto)
    TextRect.center = ((x+(w/2), (y+(h/2))))
    tela.blit(TextSurf, TextRect)
    
#Tela de apresentação/inicio do jogo
def tela_inicio():
    
    sair = False
    
    while not sair:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                quit()

        tela.fill(branco)
        
        largeText = pygame.font.Font('freesansbold.ttf', 55)
        TextSurf, TextRect = Text_Objects('JO-KEN-PO', largeText)
        TextRect.center = ((tela_largura/2), (tela_altura/2))
        tela.blit(TextSurf, TextRect)

        button('Jogar', 100, 400, 100, 50, (0, 200, 0), verde, 'Jogar')
        button('Sair', 500, 400, 100, 50, (200, 0, 0), vermelho, 'Sair')
        
        pygame.display.update()
#Funções
tela_inicio()
pygame.quit()
quit()
