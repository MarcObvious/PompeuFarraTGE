import nltk;
#from nltk.corpus import treebank
import sys;

class State():
    def __init__(self, posicio, data):
        self.posicio = posicio
        self.data = data
    
    def getResposta(self, input):
        if input in self.data.keys():
            return self.data[input]
        return 0
        
        

#Dona una resposta i estat seguent a partir d'una serie de tokens
def resposta(tokens, estat):
    resposta = 'merda'
    estatSeguent = 0
    print("ara intentarem trobar resposta")
    for token in tokens.split():
        resposta = estat.getResposta(token)
    
    return resposta, estatSeguent

def carregaestats(estats):
    s =  State(0,{'frase1':'resposta u', 'frase2':'resposta 2'})
    estats.append(s)
    s2 =  State(1,{'frase3':'resposta 3', 'frase4':'resposta 4'})
    estats.append(s2)
    print("Carrega inicial feta") 
    
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
    carregaestats(estats)
    #print(estats[0].getResposta('frase1'))
#     print (estats)
    print("Write something:")  
    for line in sys.stdin:
        print("has esrit:", line)
        tokens = nltk.word_tokenize(line)
        print(tokens)
        tagged = nltk.pos_tag(tokens)
        print (tagged[0:len(tagged)])
        sortida(tokens)
        
        resp, est = resposta(line,estats[0])
        print (resp)
        resp, est = resposta(line,estats[1])
        print (resp)
if __name__ == "__main__":
    main()
