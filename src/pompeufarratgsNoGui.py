import nltk;
#from nltk.corpus import treebank
import sys;
import random;

class State():
    def __init__(self, posicio, frase, data):
        self.frase = frase
        self.posicio = posicio
        self.data = data
    
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
    resposta = -1
    estatSeguent = -1
#     print("ara intentarem trobar resposta")
    #for token in tokens.split():
    resposta, estatSeguent = estat.getResposta(tokens[:-1])
    
    return resposta, estatSeguent

# def carregaestatsProva(estats):
#     s =  State(0,'Soplapenes',{'frase1':['resposta u',1], 'frase2':['resposta 2',2]})
#     estats.append(s)
#     s2 =  State(1,'fresca',{'frase3':['resposta 3',2], 'frase4':['resposta 4',3]})
#     estats.append(s2)
#     print("Carrega inicial feta") 
    
def carregaEstats(estats, raw_estat):
    print("Llegint estat", raw_estat)
    estat1 = open( "../estats/"+raw_estat+".txt", "r" ) 
    
    num_estat = raw_estat
    frase_inicial = ""
#     print (num_estat)
    diccionari = {}
    
    primer = True
    for line in estat1:
        if (primer):
            frase_inicial = line
#             print ("FRASE INICIAL",frase_inicial)
            primer = False
        else:
            separat = line.split('|')
#             print (separat)
            diccionari[separat[0]] = (separat[1],int(separat[2][:-1]))
#             print (separat[2][:-1])
    s = State(int(num_estat),frase_inicial,diccionari)
    
    estats.append(s)

def generaRespostaNLTK(typedline):
    extra = open( "../estats/extra.txt","r")
    for line in extra:
        separat = line.split('|')
        if typedline == separat[0]+"\n":
            return separat[1]
    tokens = nltk.word_tokenize(typedline)
    tagged = nltk.pos_tag(tokens)
    i = 0
    tags = []
    VBi = NNi = VBGi = NNSi = 0
    VB = NN = VBG = NNS = "none"
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
        i += 1
    print(VB+NN+VBG+NNS)
    if len(tagged) < 7 and VB != "none" and NN != "none" and VBG == "none" and NNS == "none":
        NLTKanswer = "do you think that "+VB+"ing a "+NN+" is a good idea right now?"
        return(NLTKanswer)
    elif len(tagged) < 7 and VB != "none" and NN == "none" and VBG == "none" and NNS != "none":
        NLTKanswer = "do you think that "+VB+"ing some "+NNS+" is a good idea right now?"
        return(NLTKanswer)
    elif len(tagged) < 7 and VB == "none" and NN != "none" and VBG != "none" and NNS == "none":
        NLTKanswer = "why are you "+VBG+" a "+NN+"? I think you have more important things to do"
        return(NLTKanswer)
    elif len(tagged) < 7 and VB == "none" and NN == "none" and VBG != "none" and NNS != "none":
        NLTKanswer = "why are you "+VBG+" some "+NNS+"? I think you have more important things to do"
        return(NLTKanswer)
    elif len(tagged) < 7 and VB == "am" and NN == "none" and VBG != "none" and NNS != "none":
        NLTKanswer = "why are you "+VBG+" some "+NNS+"? I think you have more important things to do"
        return(NLTKanswer)
    elif len(tagged) < 7 and VB == "am" and NN != "none" and VBG != "none" and NNS == "none":
        NLTKanswer = "why are you "+VBG+" a "+NN+"? I think you have more important things to do"
        return(NLTKanswer)
    return(NPIanswer())
    
def carregaNPI():
    extra = open( "../RespostesEstandar/NPI","r")
    for line in extra:
        npi_answers.append(line[:-1])
    return npi_answers
def NPIanswer():
    return npi_answers[random.randint(1,len(npi_answers)-1)]

def sortida(tokens):
    if ('surtJA' in tokens): 
        print ("Good bye")
        
        exit()

def draw():
    print()

#     loop
def run(self):
    print()
    
estats = []
npi_answers = []
#A main hem de definir tots els estats on podem anar i carregar els valors inicials
def main():
    
#     estats = []
    npi_answers = carregaNPI()
   
#     carregaestatsProva(estats)
    carregaEstats(estats, '0')
    carregaEstats(estats, '1')
    carregaEstats(estats, '2')
    carregaEstats(estats, '3')
    carregaEstats(estats, '4')
    carregaEstats(estats, '5')
    #print(estats[0].getResposta('frase1'))
#     print (estats)
#     print("Write something:")  
    estatAct = 0
    print (estats[estatAct].getFraseInicial())
    for line in sys.stdin:
       
        print("has esrit:", line)
        tokens = nltk.word_tokenize(line)
#         print(tokens)
        tagged = nltk.pos_tag(tokens)
        print (tagged[0:len(tagged)])
        sortida(tokens)
         
        resp, estatAct = resposta(line,estats[estatAct])
        if (resp == 0):
            print ("RESPOSTA: ",(generaRespostaNLTK(line)))
        else:
            print ("RESPOSTA: ",resp)
        print ("ESTAT ACTUAL: " ,estatAct)
#         resp, est = resposta(line,estats[1])
        print (estats[int(estatAct)].getFraseInicial())

if __name__ == "__main__":
    main()
