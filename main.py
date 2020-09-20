# from beautifulsoup4 import beautifulsoup4

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import os

# fileList =os.listdir("D:\\bigdata\第二次作业\\test")
#
#
stopset=set(stopwords.words("english"))
stopset.update("it","It","the","a","you","none","none")
# wnl = WordNetLemmatizer()
# # lemmatize nouns
# print(wnl.lemmatize('cars', 'n'))
# print(wnl.lemmatize('features', 'n'))

docs=[["1","2","3"],["adsad","sasdffdqwqw"],["sdsfdsdfsdfs"]]

vectorizer =TfidfVectorizer(stop_words=stopset,use_idf=True,ngram_range=(1,3))

X=vectorizer.fit_transform(docs)
print(X[0])