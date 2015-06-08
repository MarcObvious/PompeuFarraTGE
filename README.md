# PompeuFarraTGE

------------------------------------------------------------------------------------------------------------

Llibreries externes:
1. Install Setuptools: http://pypi.python.org/pypi/setuptools
2. Install Pip: run sudo easy_install pip
4. Install pygame: sudo pip -U pygame
3. Install Numpy: sudo pip install -U numpy
4. Install NLTK: sudo pip install -U nltk
5. Download all the data: run python then type import nltk, nltk.download()
        

http://www.nltk.org/
------------------------------------------------------------------------------------------------------------

Generació de respostes en funció de l'input:
Primer mira si a l'arxiu txt de l'estat actual troba una resposta predeterminada per aquell input concret.
Sinó, mira si troba una resposta predeterminada en l'arxiu extra.txt.
Sinó, tracta de respondre l'input a partir dels tags trobats. [EXPLICACIÓ]
Sinó, genera de manera aleatòria una de les múltiples respostes de l'arxiu NPI.

[EXPLICACIÓ] 
De moment respon: 

1-frases simples de menys de 7 paraules que tenen un VB o VBP o VBG i un NN o NNS que fan referència 
a una acció que fa el protagonista. 
Exemples: I eat a banana, I eat apples, Jumping this desktop, Kissing girls...

2-frases simples de menys de 7 paraules que tenen un VBG, un VB="am" i un NN o NNS que fan referència 
a una acció que fa el protagonista. 
Exemples: I am eating a cherry, I am eating oranges, I am fucking all the bitches...

3-preguntes simples de menys de 10 paraules acabades en '?' on tenim un WRB="where" i on la cosa que preguntem on és un NN o NNS que es troba al final. 
Exemples: Where are all the pussies?, Where there is a wc?

4-preguntes simples de menys de 10 paraules acabades en '?' on tenim un WRB="when", en cas de preguntar 
per YOU o I s'intercanvien per que quedi bé la resposta. 
Exemples: When I will get out of here?, When you will leave?, When it will rain? 
