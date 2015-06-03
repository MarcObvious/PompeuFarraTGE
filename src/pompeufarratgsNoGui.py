import nltk;
#from nltk.corpus import treebank
import sys;

def resposta(tokens, estat):
    resposta = 'merda'
    estatSeguent = 0
    print("ara intentarem trobar resposta")
    return resposta, estatSeguent

def sortida(tokens):
    if ('surtJA' in tokens): 
        print ("Good bye")
        exit()

def draw():
    print()

def run(self):
#     loop
    print()
    
#A main em de definir tots els estats on podem anar i carregar els valors inicials
def main():
    print("Write something:")  
    for line in sys.stdin:
        print("has esrit:", line)
        tokens = nltk.word_tokenize(line)
        print(tokens)
        tagged = nltk.pos_tag(tokens)
        print (tagged[0:len(tagged)])
        sortida(tokens)
        print("What are you talking about? Try again")

if __name__ == "__main__":
    main()
