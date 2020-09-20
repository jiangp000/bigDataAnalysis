from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# 用一个for 循环 进行46个文件的处理   处理完之后 加入到 bowList之中去

#四十多个文本 怎么进行分割啊
docA="the cat sat on my face"
docB="the dog sat on my bed"
docC="the god is your people"
docD="we are in the same school"
docE="bao bao is a great job"
docF="jiang jiang is a great jon"
docG="same school in the world"
docH="we do not want to be a bad guy"

bowList=[]

bowList.append(docA)
bowList.append(docB)
bowList.append(docC)
bowList.append(docD)
bowList.append(docE)
bowList.append(docF)
bowList.append(docG)
bowList.append(docH)

bowUnion=[]
for i in range(len(bowList)):
    bowUnion.append(bowList[i].split(" "))
    print(bowUnion[i])

WordSet=set()

for i in range(len(bowUnion)):
    WordSet=WordSet.union(set(bowUnion[i]))


WordEach=[]

for i in range(len(bowList)):
    WordEach.append(dict.fromkeys(WordSet,0))


for i in range(len(WordEach)):
    for word in bowUnion:
        WordEach[i][word]+=1


def computeTF(wordDict,bow):
    tfDict={}
    bowCount=len(bow)
    for word,count in wordDict.items():
        tfDict[word]=count/float(bowCount)
    return tfDict

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

def computeTFIDF(tfBow,idfs):
    tfidf={}
    for word,val in tfBow.items():
        tfidf[word]=val*idfs[word]
    return tfidf
# 放TF的 数据

tfList=[]
for i in range(len(bowList)):
    tfList.append(computeTF(WordEach[i],bowUnion[i]));


# 放IDF 的数据
idf=computeTDF(WordEach)

# 放最后的 TF-IDF 的数据
tfidfList=[]

for i in range(len(bowList)):
    tfidfList.append(computeTFIDF(tfList[i],idf))

pd.DataFrame(tfidfList)







pd.DataFrame(WordEach)

#
# wordSet=set(bowA).union(set(bowB)).union((set(bowC))).union(set(bowD))
#
# wordDictA=dict.fromkeys(wordSet,0)
# wordDictB=dict.fromkeys(wordSet,0)
#
# for word in bowA:
#     wordDictA[word]+=1
#
# for word in bowB:
#     wordDictB[word]+=1
#
#
#
# pd.DataFrame([wordDictA,wordDictB])
#
#
# def computeTF(wordDict,bow):
#     tfDict={}
#     bowCount=len(bow)
#     for word,count in wordDict.items():
#         tfDict[word]=count/float(bowCount)
#     return tfDict
#
# tfBowA=computeTF(wordDictA,bowA)
# tfBowB=computeTF(wordDictB,bowB)
#
# def computeTDF(docList):
#     import math
#     idfDict={}
#     N=len(docList)
#
#     idfDict=dict.fromkeys(docList[0].keys(),0)
#     for doc in docList:
#         for word,val in doc.items():
#             if val>0:
#                 idfDict[word]+=1
#     for word,val in idfDict.items():
#         idfDict[word]=math.log(N/float(val))
#
#     return idfDict
#
# idfs=computeTDF([wordDictA,wordDictB])
#
# def computeTFIDF(tfBow,idfs):
#     tfidf={}
#     for word,val in tfBow.items():
#         tfidf[word]=val*idfs[word]
#     return tfidf
#
# tfidfBowA=computeTFIDF(tfBowA,idfs)
# tfidfBowB=computeTFIDF(tfBowB,idfs)
#
# pd.DataFrame([tfidfBowA,tfBowB])
