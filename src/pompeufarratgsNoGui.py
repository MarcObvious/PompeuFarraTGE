import nltk;
#from nltk.corpus import treebank
import sys;

class State():
    def __init__(self, posicio, frase, data):
        self.frase = frase
        self.posicio = posicio
        self.data = data
    
    def getResposta(self, input):
        if input in self.data.keys():
#             print ("AHA", self.data[input])
            return self.data[input]
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

def carregaestatsProva(estats):
    s =  State(0,'Soplapenes',{'frase1':['resposta u',1], 'frase2':['resposta 2',2]})
    estats.append(s)
    s2 =  State(1,'fresca',{'frase3':['resposta 3',2], 'frase4':['resposta 4',3]})
    estats.append(s2)
    print("Carrega inicial feta") 
    
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
    
def sortida(tokens):
    if ('surtJA' in tokens): 
        print ("Good bye")
        exit()

def draw():
    print()

#     loop
def run(self):
    print()
    
#A main hem de definir tots els estats on podem anar i carregar els valors inicials
def main():
    estats = []
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
        print ("RESPOSTA: ",resp)
        print ("ESTAT ACTUAL: " ,estatAct)
#         resp, est = resposta(line,estats[1])
        print (estats[int(estatAct)].getFraseInicial())

if __name__ == "__main__":
    main()
