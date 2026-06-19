import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

text = """
Artificial Intelligence is a branch of computer science.
Machine Learning is a subset of AI.
Deep Learning is a subset of Machine Learning.
AI is used in healthcare and finance.
"""

doc = nlp(text)

concepts = {}

for token in doc:

    if token.pos_ in ["NOUN", "PROPN"]:

        word = token.text

        if word in concepts:
            concepts[word] += 1
        else:
            concepts[word] = 1

print(concepts)

df = pd.DataFrame(
    concepts.items(),
    columns=["Concept", "Frequency"]
)

df = df.sort_values(
    by="Frequency",
    ascending=False
)

print("\n=== RESEARCH TABLE ===\n")
print(df)

df.to_csv(
    "data/research_table.csv",
    index=False
)

print("\nTable saved successfully")