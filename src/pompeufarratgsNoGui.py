import nltk;
#from nltk.corpus import treebank
import sys;
import random;
from nltk.stem import *
from nltk.stem.wordnet import WordNetLemmatizer
from os import listdir
#import pyglet

class State():
    def __init__(self, posicio, frase, data):
        self.frase = frase
        self.posicio = posicio
        self.data = data
    
    def __repr__(self):
        return repr((self.frase, self.posicio, self.data))
    
    def getResposta(self, entrada):
        if entrada in self.data.keys():
#             print ("AHA", self.data[input])
            return self.data[entrada]
        return 0,0
    
    def getFraseInicial(self):
        return self.frase
    
    def getNumEstat(self):
        return self.posicio
        
#Dona una resposta i estat seguent a partir d'una serie de tokens
def resposta(tokens, estat):
#     print("ara intentarem trobar resposta")
    #for token in tokens.split():
    resposta, estatSeguent = estat.getResposta(tokens)
    
    return resposta, estatSeguent

#Carreguem tots els estats que hi hagi a la carpeta estat    
def carregaEstats():
    for fitxer in listdir("../estats/"): 
        print("Llegint estat", fitxer)
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
                separat = line.split('|')
                diccionari[separat[0]] = (separat[1],int(separat[2][:-1]))
    
        s = State(int(num_estat),frase_inicial,diccionari)
        estats.append(s)
    
    #Com que llegim directament de la carpeta, els estats s'han dordenar
    estats.sort(key=lambda State: State.posicio,reverse=False)

def generaRespostaNLTK(typedline):
    extra = open( "../extra/extra.txt","r")
    for line in extra:
        separat = line.split('|')
        if typedline == separat[0]+"\n":
            return separat[1]
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
    print(VB+NN+VBG+NNS)
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
            whenanswer = whenanswer+" "+tokens[j].lower()
            j += 1
        NLTKanswer = "I don't know "+whenanswer[:-2]+", God knows"
    
    if (NLTKanswer != ""):
        return NLTKanswer+"\n I'm having fun talking with you, but you gotta give orders in order to get out of here."
    return NPIanswer()
    
#Carrega les respostes NPI
def carregaNPI():
    extra = open( "../RespostesEstandar/NPI","r")
    for line in extra:
        npi_answers.append(line[:-1])

#Torna una resposta random NPI
def NPIanswer():
    return npi_answers[random.randint(1,len(npi_answers)-1)]

def sortida(tokens):
    if ('surtJA' in tokens): 
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
npi_answers = []

#A main hem de definir tots els estats on podem anar i carregar els valors inicials
def main():
#     try:
#         song = pyglet.media.load("../songs/GameMusic.mp3", streaming=False)
#         song.play()
#         pyglet.app.run()
#     except pyglet.media.MediaException:
#         print("fuck, notira")

    carregaNPI()   
    carregaEstats()
    print ("#Estats",len(estats))
    
    estatAct = 0
    print (estats[estatAct].getFraseInicial())
    print ("Say something:")
    for line in sys.stdin:
       
        print("has esrit:", line)
        tokens = nltk.word_tokenize(line)

        tagged = nltk.pos_tag(tokens)
        print ("NLTK", tagged[0:len(tagged)])
        sortida(tokens)
        
        lemma = lemmatize(tokens)
        print ("LEMMA", lemma)
        l = ""
        for word in lemma:
            l += word+" "
        l = l[:-1]
        
        resp, estatAct = resposta(l,estats[estatAct])
        if (resp == 0):
            print ("RESPOSTA: ",(generaRespostaNLTK(line)))
        else:
            print ("RESPOSTA: ",resp)
        print ("ESTAT ACTUAL: " ,estatAct)
#         resp, est = resposta(line,estats[1])
        
        print (estats[int(estatAct)].getFraseInicial())
        
        print ("Say something:")

if __name__ == "__main__":
    main()
