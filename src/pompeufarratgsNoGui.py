import nltk;
#from nltk.corpus import treebank
import sys;

def main():
    print("Write something:")  
    for line in sys.stdin:
        print("has esrit:", line)
        tokens = nltk.word_tokenize(line)
        print(tokens)
        tagged = nltk.pos_tag(tokens)
        print (tagged[0:len(tagged)])
if __name__ == "__main__":
    main()
