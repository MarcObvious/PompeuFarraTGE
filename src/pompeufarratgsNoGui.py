
import nltk;
#from nltk.corpus import treebank
from nltk.corpus import wordnet as wn
import sys;
import random;
from nltk.stem import *
from nltk.stem.wordnet import WordNetLemmatizer
from os import listdir
#import pyglet
from pygame.locals import*
import pygame, eztext, threading
#img = pygame.image.load('clouds.bmp')

#mides pantalla
width = 800
height = 500

#colors
black = (5,5,5)

def mapa():
#     aux = 0
    estatAct = 0
    clock = pygame.time.Clock()
    FPS = 5
    #inicialitzacio de la pantalla, titol del joc i input de text
    pygame.init()  # @UndefinedVariable
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('PompeuFarra: The Great Escape')
    mapapic = pygame.image.load("../pics/mapa.png")
    tracker = pygame.image.load("../pics/tracker.png")
    while 1:
        clock.tick(FPS)
        events = pygame.event.get()
        
        
        llegeix = open("aux","r")
        for line in llegeix:
            estatAct = int(line)
        llegeix.close()
        
        
        for event in events:
            #aixi tanquem apretant la creu
            if event.type == pygame.QUIT:  # @UndefinedVariable
                pygame.quit()  # @UndefinedVariable
                quit()
        screen.fill(black)
        screen.blit(mapapic,(15,15))
        #estatVerificat = verificaEstat(aux, estatAct)
        if estatAct == 0:
            screen.blit(tracker,(360,435))
        elif estatAct == 1:
            screen.blit (tracker,(360,390))
        elif estatAct == 2:
            screen.blit (tracker,(320,435))
        elif estatAct == 3:
            screen.blit (tracker,(280,435))
        elif estatAct == 4:
            screen.blit (tracker,(220,170))
        elif estatAct == 5:
            screen.blit (tracker,(360,170))
        elif estatAct == 6:
            screen.blit (tracker,(360,300))
        elif estatAct == 7:
            screen.blit (tracker,(190,360))
        elif estatAct == 8:
            screen.blit (tracker,(140,260))
        elif estatAct == 9:
            screen.blit (tracker,(140,320))
        elif estatAct == 10:
            screen.blit (tracker,(140,380))
        elif estatAct == 11:
            screen.blit (tracker,(180,80))
        elif estatAct == 12:
            screen.blit (tracker,(160,205))
        elif estatAct == 13:
            screen.blit (tracker,(90,30))
        elif estatAct == 14:
            screen.blit (tracker,(550,250))
        elif estatAct == 15:
            screen.blit (tracker,(570,40))
        elif estatAct == 16:
            screen.blit (tracker,(630,40))
        elif estatAct == 17:
            screen.blit (tracker,(670,40))
        elif estatAct == 18:
            screen.blit (tracker,(690,150))
        elif estatAct == 19:
            screen.blit (tracker,(680,400))
        pygame.display.update()

#def verificaEstat(estatAct):

        #return 

class State():
    def __init__(self, posicio, frase, data):
        self.frase = frase
        self.posicio = posicio
        self.data = data
    
    def __repr__(self):
        return repr((self.frase, self.posicio, self.data))
    
    def getResposta(self, entrada):
        #print ("ENTRADA:",entrada)
        valor = 0
        keyFinal = ""
        for key in self.data.keys():
#             print (key.split(" "))  
            keySp = key.split(" ")
            errors = []
            if (len(keySp) == 3):
                if (keySp[0] in entrada and keySp[1] in entrada and keySp[2] in entrada):
                    return self.data[key]
            
            elif len(keySp) == 2:
                if keySp[0] in entrada and keySp[1] in entrada:
                    return self.data[key]
                else:
                    if keySp[1] in entrada:
                        try:
                            for sinKey in wn.synsets(keySp[0]):
                                for paraula in entrada:
            #                         print(paraula)
                                    for sinParaula in wn.synsets(paraula):
                                        #print("AQUI",sinParaula)
                                        aux = sinKey.path_similarity(sinParaula)
                                        if (aux > valor):
                                            valor = aux
                                            keyFinal = key
                        except:
                            errors.append(keySp[0])
                    
            elif (len(keySp) == 1):
                try:
                    for sinKey in wn.synsets(key):
                        for paraula in entrada:
    #                         print(paraula)
                            for sinParaula in wn.synsets(paraula):
                                #print("AQUI",sinParaula)
                                aux = sinKey.path_similarity(sinParaula)
                                if (aux > valor):
                                    valor = aux
                                    keyFinal = key
                except:
                    errors.append(key)
            
             
            if key in entrada:
                return self.data[key]
                
        
        print ("Key guanyadora:", keyFinal, valor)
        if (valor >= 0.5):
            return self.data[keyFinal]
        return "",-1
    
    def getFraseInicial(self):
        return self.frase
    
    def getNumEstat(self):
        return self.posicio
    
    def getkeys(self):
        return 0
    
    def printKeys(self):
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for key in self.data.keys():
            print (key)
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
#Dona una resposta i estat seguent a partir d'una serie de tokens
def resposta(tokens, estat):
    resposta, estatSeguent = estat.getResposta(tokens)
    if (estatSeguent == -1):
        print("HINT: best phrases start with \"I' want\"")
        return resposta, estat.getNumEstat()
    return resposta,estatSeguent

#Carreguem tots els estats que hi hagi a la carpeta estat    
def carregaEstats():
    for fitxer in listdir("../estats/"): 
        #print("Loading state", fitxer)
        estat1 = open("../estats/"+fitxer, "r" ) 
        
        num_estat = int(fitxer[:-4])
        frase_inicial = ""
        diccionari = {}
        
        primer = True
        for line in estat1:
            if (primer):
                frase_inicial = line[:-1]
                primer = False
            else:
                separat = line.split('||')
                diccionari[separat[0]] = (separat[1],int(separat[2][:-1]))
        estat1.close()    
        s = State(int(num_estat),frase_inicial,diccionari)
        estats.append(s)
   
    #Com que llegim directament de la carpeta, els estats s'han dordenar
    estats.sort(key=lambda State: State.posicio,reverse=False)

def generaRespostaNLTK(typedline):
    tokens = nltk.word_tokenize(typedline)
    tagged = nltk.pos_tag(tokens)
    i = 0
    tags = []
    VBi = NNi = VBGi = NNSi = WRBi = 0
    VB = NN = VBG = NNS = WRB = "none"
    while i < len(tagged):
        tags.append(tagged[i][1])
        if tagged[i][1] == "VB" or tagged[i][1] == "VBP":
            VB = tagged[i][0]
            VBi = i
        if tagged[i][1] == "VBG":
            VBG = tagged[i][0]
            VBGi = i
        if tagged[i][1] == "NN":
            NN = tagged[i][0]
            NNi = i;
        if tagged[i][1] == "NNS":
            NNS = tagged[i][0]
            NNSi = i
        if tagged[i][1] == "WRB":
            WRB = tagged[i][0]
            WRBi = i
        i += 1
#     print(VB+NN+VBG+NNS)
    NLTKanswer  = ""
    if len(tagged) < 7 and VB != "none" and NN != "none" and VBG == "none" and NNS == "none" and WRB == "none":
        NLTKanswer = "do you think that "+VB+"ing a "+NN+" is a good idea right now?"
    elif len(tagged) < 7 and VB != "none" and NN == "none" and VBG == "none" and NNS != "none" and WRB == "none":
        NLTKanswer = "do you think that "+VB+"ing some "+NNS+" is a good idea right now?"
    elif len(tagged) < 7 and VB == "none" and NN != "none" and VBG != "none" and NNS == "none" and WRB == "none":
        NLTKanswer = "why are you "+VBG+" a "+NN+"? I think you have more important things to do"
    elif len(tagged) < 7 and VB == "none" and NN == "none" and VBG != "none" and NNS != "none" and WRB == "none":
        NLTKanswer = "why are you "+VBG+" some "+NNS+"? I think you have more important things to do"
    elif len(tagged) < 7 and VB == "am" and NN == "none" and VBG != "none" and NNS != "none" and WRB == "none":
        NLTKanswer = "why are you "+VBG+" some "+NNS+"? I think you have more important things to do"
    elif len(tagged) < 7 and VB == "am" and NN != "none" and VBG != "none" and NNS == "none" and WRB == "none":
        NLTKanswer = "why are you "+VBG+" a "+NN+"? I think you have more important things to do"
    elif len(tagged) < 10 and (WRB == "where" or WRB == "Where") and tokens[len(tagged)-1] == "?" and tags[len(tagged)-2] == "NNS":
        NLTKanswer = "I don't know "+WRB.lower()+" you could find "+tokens[len(tagged)-2]+" over here"
    elif len(tagged) < 10 and (WRB == "where" or WRB == "Where") and tokens[len(tagged)-1] == "?" and tags[len(tagged)-2] == "NN":
        NLTKanswer = "I don't know "+WRB.lower()+" you could find a "+tokens[len(tagged)-2]+" over here"
    elif len(tagged) < 10 and (WRB == "when" or WRB == "When") and tokens[len(tagged)-1] == "?":
        j = 0
        whenanswer = ""
        while j < len(tagged):
            if tokens[j] == "I" or tokens[j] == "i":
                tokens[j] = "you"
            elif tokens[j] == "you":
                tokens[j] = "I"
            if tokens[j] == "my":
                tokens[j] = "your"
            elif tokens[j] == "your":
                tokens[j] = "my"
            whenanswer = whenanswer+" "+tokens[j].lower()
            j += 1
        NLTKanswer = "I don't know "+whenanswer[:-2]+", God knows"
    
    if (NLTKanswer != ""):
        return NLTKanswer+"\nI'm having fun talking with you, but you gotta give orders in order to get out of here."
    return NPIanswer()
    
#Carrega les respostes NPI
def carregaNPI():
    extra = open( "../RespostesEstandar/NPI","r")
    for line in extra:
        npi_answers.append(line[:-1])
    extra.close()
        

def carregaExtra():
    extra = open( "../extra/extra.txt","r")
    for line in extra:
        separat = line.split('|')
        extra_answers[separat[0]] = separat[1][:-1]
    extra.close()

def EXTRAanswer(line):
    for key in extra_answers.keys():
        if key == line:
            return extra_answers[key] 
    return ""

#Torna una resposta random NPI
def NPIanswer():
    return npi_answers[random.randint(1,len(npi_answers)-1)]

def sortida(tokens):
    if "SURT" in  tokens: 
        print ("Good bye")
        exit()

#No implementat
def draw():
    print()

#No implementat,  loop
def run(self):
    print()
    
def lemmatize(entrada):
    lmtzr = WordNetLemmatizer()
    sortida = []
    for paraula in entrada:
        aux1 = lmtzr.lemmatize(paraula, 'v')
        aux2 = lmtzr.lemmatize(paraula)
        if (aux1 != paraula):
            sortida.append(aux1)
        elif (aux2 != paraula):
            sortida.append(aux2)
        else:
            sortida.append(paraula)
    return sortida


#VAriables globals
estats = []
extra_answers = {}
npi_answers = []
thread = threading.Thread(target=mapa)

#A main hem de definir tots els estats on podem anar i carregar els valors inicials
def main():
    carregaNPI()   
    carregaExtra()
    carregaEstats()
    
    print (len(estats), "States loaded")
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("POMPEUFARRA: THE GREAT ESCAPE") 
    print ("---------------------------------------------------------------------------------")   
    
    estatAct = 0
    print ("STATUS:", estats[estatAct].getFraseInicial())
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("Say something:")
    
    escriu = open("aux","w")
    escriu.write(str(estatAct))
    escriu.close()

    thread.start()

    for line in sys.stdin:
        line = line.lower()
        print("Your words were:", line[:-1])
        
        if "coward" in line[:-1] and ("i wanna" in line[:-1] or "show me" in line[:-1]) and "stats" in line[:-1]:
            print ("KEYS DISPONIBLES")
            estats[estatAct].printKeys()
            
        else:
            tokens = nltk.word_tokenize(line)
            print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            tagged = nltk.pos_tag(tokens)
            print ("NLTK", tagged[0:len(tagged)])
            sortida(tokens)
                
            lemma = lemmatize(tokens)
            print ("LEMMA", lemma)
    
            tagged2 = nltk.pos_tag(lemma)
            resp = ""
            print ("NLTK+LEMMA", tagged2)
            if '?' not in line:
                resp, estatAct = resposta(lemma,estats[estatAct])
            if resp == "":
                resp = EXTRAanswer(line[:-1])
            
            if resp == "":
                resp = generaRespostaNLTK(line)
            
            print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            
            print ("RESPOSTA: ",resp)
    
        print ("ESTAT ACTUAL: " ,estatAct)
        
        escriu = open("aux","w")
        escriu.write(str(estatAct))
        escriu.close()
        
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("STATUS:", estats[estatAct].getFraseInicial())
        print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("Say something:")

if __name__ == "__main__":
    main()
