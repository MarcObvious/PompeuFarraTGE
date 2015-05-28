from pygame.locals import *
import pygame, sys, eztext

#mides pantalla i requadre de text
width = 1300
height = 900
textboxX = width*0.01
textboxY = height*0.8

#colors
blanc = (255,255,255)
vermell = (255,0,0)
blau = (0,0,255)
verd = (0,255,0)
negre = (0,0,0)

#inicialitzacio de la pantalla, titol del joc i input de text
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('PompeuFarra: The Great Scape')
font = pygame.font.Font(None, 36)
textin = eztext.Input(x=textboxX, y=textboxY, maxlength=100, color=(negre), prompt='Escriu: ')

#funcio que processa la resposta
def generaResposta():
    resposta = "Al pou"
    return resposta

#funcio que mostra per pantalla el mapa (quan estem apretant TAB)
def pintaMapa():
    screen.fill(negre)

#funcio que mostra per pantalla el que veu el protagonista
def pintaEntorn():
    screen.fill(vermell)

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
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if (keyPressed(K_TAB)): #mentre apretem tab mostra el mapa
            pintaMapa()
        else: pintaEntorn()
        pygame.draw.rect(screen,blanc,(0,height*0.79,width,height-height*0.79))
        textin.update(events)
        textin.draw(screen)
        if (keyPressed(K_RETURN)):#apretem enter per generar resposta
            textout = font.render(generaResposta(), 1, (blau))
            screen.blit(textout,(width*0.04,height*0.825))
        pygame.display.update()

if __name__ == '__main__': main()

