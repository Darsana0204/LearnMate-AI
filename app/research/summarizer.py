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
words= word_tokenize(text)
stop_words= set(stopwords.words("english"))
filtered_words=[]
for word in words:
    if word.lower() not in stop_words and word.isalpha():
        filtered_words.append(word)

print("\n=FILTERED WORDS=")
print(filtered_words)

word_freq= {}
for word in filtered_words:

    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1

print("\n=WORD FREQUENCY=")
print(word_freq)

max_freq= max(word_freq.values())

for word in word_freq:
    word_freq[word]= word_freq[word]/max_freq

sentence_scores= {}

for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq:
            if sentence not in sentence_scores:
                sentence_scores[sentence]= word_freq[word]
            else:
                sentence_scores[sentence]+= word_freq[word]

summary_sentences= nlargest(2, sentence_scores, key= sentence_scores.get)
summary= " ".join(summary_sentences)
print("\n=ORIGINAL TEXT=\n")
print(text)
print("\n=SUMMARY=\n")
print(summary)