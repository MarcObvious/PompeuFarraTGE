import nltk;
from nltk.corpus import treebank
import sys;

for line in sys.stdin:
    print("has esrit:", line)
    tokens = nltk.word_tokenize(line)
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print (tagged[0:len(tagged)])
    