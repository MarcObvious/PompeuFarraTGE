import nltk;
#from nltk.corpus import treebank
import sys;

def sortida(tokens):
    if ('surtJA' in tokens): 
        print ("Good bye")
        exit()

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
