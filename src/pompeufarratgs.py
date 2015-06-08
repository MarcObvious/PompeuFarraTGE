
from pygame.locals import *
import pygame, sys, eztext

#mides pantalla i requadre de text
width = 800
height = 500
textboxX = width*0.01
textboxY = height*0.8

x = False

#colors
blanc = (255,255,255)
vermell = (255,0,0)
blau = (0,0,255)
verd = (0,255,0)
negre = (0,0,0)

#inicialitzacio de la pantalla, titol del joc i input de text
pygame.init()  # @UndefinedVariable
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PompeuFarra: The Great Escape')
font = pygame.font.Font(None, 36)
textin = eztext.Input(x=textboxX, y=textboxY, maxlength=100, color=(negre), prompt='Escriu: ')

#funcio que processa la resposta
def generaResposta(textin):
#     resposta = "Al pou"
    resposta = textin.value
    
    return resposta

#funcio que mostra per pantalla el mapa (quan estem apretant TAB)
def pintaMapa():
    screen.fill(vermell)

#funcio que mostra per pantalla el que veu el protagonista
def pintaEntorn():
    screen.fill(negre)

#funcio per saber quina tecla es prem
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False

def main():
    while 1:
        events = pygame.event.get()
        for event in events:
            #aixi tanquem apretant la creu
            if event.type == pygame.QUIT:  # @UndefinedVariable
                pygame.quit()  # @UndefinedVariable
                quit()
        if (keyPressed(K_TAB)):
            x = True
        else:
            x = False
        if x: pintaEntorn()
        if not x: pintaMapa()
        pygame.draw.rect(screen,blanc,(0,height*0.79,width,height-height*0.79))
        textin.update(events)
        textin.draw(screen)
        if (keyPressed(K_RETURN)):#apretem enter per generar resposta @UndefinedVariable
            textout = font.render(generaResposta(textin), 1, (blau))
            screen.blit(textout,(width*0.04,height*0.825))
            textin.value = ""
        pygame.display.update()

if __name__ == '__main__': main()

