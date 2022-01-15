"""
lousy_plasma.py (15 points)
=====
See instructions on course site.
"""
"""
#part 0 + 1
thesaurus = {
    "happy" : ["glad",  "blissful", "ecstatic", "at ease"],
    "sad"   : ["bleak", "blue", "depressed"]
}
phrase = input("Please provide a phrase.\n>")
phraselist = phrase.split(" ")
newphrase = ""
for word in phraselist:
    word = word.lower()
    alpha = word.isalpha()
    wasspecial = 0
    if alpha == False:
        length = len(word)
        specialchar = word[length - 1]
        word = word[0 : length - 1]
        alpha = word.isalpha()
        wasspecial = 1
    if alpha == True:
        import random
        if word == "happy":
            newwords = thesaurus["happy"]
            happysyns = len(newwords)
            randhappy = random.randint(1, happysyns)
            newword = newwords[randhappy - 1]
            newword = newword.upper()
            newphrase += (" " + newword)
        elif word == "sad":
            newwords = thesaurus["sad"]
            sadsyns = len(newwords)
            randsad = random.randint(1, sadsyns)
            newword = newwords[randsad - 1]
            newword = newword.upper()
            newphrase += (" " + newword)
        else:
            newphrase += (" " + word)
    if wasspecial == 1:
        newphrase += specialchar
        wasspecial = 0
        specialchar = ""
newphraselength = len(newphrase)
newphrase = newphrase[1 : newphraselength]
print(newphrase)
"""
"""
#part 2

thesaurus = {}
f = open('thesaurus.txt', 'r')
for line in f:
    wordnsyns = line.split(",")
    length = len(wordnsyns)
    word = wordnsyns[0]
    lastsyn = str(wordnsyns[length - 1])
    lastlen = len(lastsyn)
    lastsyn = lastsyn[0:lastlen - 1]
    syns = wordnsyns[1:length - 1]
    syns.append(lastsyn)
    word_syns = {word :syns}
    thesaurus.update(word_syns)
    
phrase = input("Please provide a phrase.\n>")
phraselist = phrase.split(" ")
newphrase = ""
for word in phraselist:
    word = word.lower()
    alpha = word.isalpha()
    wasspecial = 0
    if alpha == False:
        length = len(word)
        specialchar = word[length - 1]
        word = word[0 : length - 1]
        alpha = word.isalpha()
        wasspecial = 1
    if alpha == True:
        import random
        theskeys = list(thesaurus.keys())
        wordinthes = theskeys.count(word)
        if wordinthes > 0:
            newwords = thesaurus[word]
            numsyns = len(newwords)
            randsyn = random.randint(1, numsyns)
            newword = newwords[randsyn - 1]
            newword = newword.upper()
            newphrase += (" " + newword)
        elif wordinthes <= 0:
            newphrase += (" " + word)
    if wasspecial == 1:
        newphrase += specialchar
        wasspecial = 0
        specialchar = ""
newphraselength = len(newphrase)
newphrase = newphrase[1 : newphraselength]
print(newphrase)
"""
#part 3

thesaurus = {}
f = open('thesaurus.txt', 'r')
for line in f:
    wordnsyns = line.split(",")
    length = len(wordnsyns)
    word = wordnsyns[0]
    lastsyn = str(wordnsyns[length - 1])
    lastlen = len(lastsyn)
    lastsyn = lastsyn[0:lastlen - 1]
    syns = wordnsyns[1:length - 1]
    syns.append(lastsyn)
    word_syns = {word :syns}
    thesaurus.update(word_syns)
b = open("bad_blood.txt", "r")
for line in b:
    words = line.split(" ")
    newphrase = ""
    theskeys = list(thesaurus.keys())
    wordlistlength = len(words)
    for word in words:
        word = word.lower()
        alpha = word.isalpha()
        wordinthes = theskeys.count(word)
        length = len(word)
        if word == words[wordlistlength - 1]:
            word = word[0:length - 1]
        if alpha == False:
            spechars = "!@3$%^&*()-_=+`~;:',<.>/?\|[{]}\""
            for i in word:
                spec = spechars.count(i)
                if spec > 0:
                    specialchar = i
            word = word.replace(specialchar, "")
            alpha = word.isalpha()
        if alpha == True:
            if wordinthes > 0:
                import random
                rand = random.randint(1,2)
                if rand == 1:
                    synonymlist = thesaurus[word]
                    synlistlen = len(synonymlist)
                    synonymrng = random.randint(1, synlistlen)
                    syn = synonymlist[synonymrng - 1]
                    syn = syn.upper()
                    newphrase += (" " + syn)
                if rand == 2:
                    newphrase += (" " + word)
            if wordinthes < 1:
                newphrase += (" " + word)
    print(newphrase)

    
