from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
text= """
Artificial intelligence is a branch of computer science.
It enables machines to perform tasks that normally require human intelligence.
AI is used in healthcare,finance, education, and transportation.
Machine Learning is a subset of AI.
Deep Learning is a subset of ML.
"""
sentences= sent_tokenize(text)
print("=SENTENCES=")
print(sentences)
words= word_tokenize(text)
print("\n=WORDS=")
print(words[:20])
stop_words= set(stopwords.words("english"))
filtered_words=[]
for word in words:
    if word.lower() not in stop_words and word.isalpha():
        filtered_words.append(word)

print("\n=FILTERED WORDS=")
print(filtered_words)

word_freq= {}
for word in filtered_words:

    word= word.lower()
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

print("\n=WORD FREQUENCY=")
print(word_freq)