from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

docA="the cat sat on my face"
docB="the dog sat on my bed"

bowA=docA.split(" ")
bowB=docB.split(" ")

# print(bowA)
# print(bowB)

wordSet=set(bowA).union(set(bowB))
# print(wordSet)

wordDictA=dict.fromkeys(wordSet,0)
wordDictB=dict.fromkeys(wordSet,0)

for word in bowA:
    wordDictA[word]+=1

for word in bowB:
    wordDictB[word]+=1

# print(wordDictA)

# print()
# print(wordDictA)

# print(wordDictB)


pd.DataFrame([wordDictA,wordDictB])


def computeTF(wordDict,bow):
    tfDict={}
    bowCount=len(bow)
    for word,count in wordDict.items():
        tfDict[word]=count/float(bowCount)
    return tfDict

tfBowA=computeTF(wordDictA,bowA)
tfBowB=computeTF(wordDictB,bowB)

def computeTDF(docList):
    import math
    idfDict={}
    N=len(docList)

    idfDict=dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word,val in doc.items():
            if val>0:
                idfDict[word]+=1
    for word,val in idfDict.items():
        idfDict[word]=math.log(N/float(val))

    return idfDict

idfs=computeTDF([wordDictA,wordDictB])

def computeTFIDF(tfBow,idfs):
    tfidf={}
    for word,val in tfBow.items():
        tfidf[word]=val*idfs[word]
    return tfidf

tfidfBowA=computeTFIDF(tfBowA,idfs)
tfidfBowB=computeTFIDF(tfBowB,idfs)

pd.DataFrame([tfidfBowA,tfBowB])
