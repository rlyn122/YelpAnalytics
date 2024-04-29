import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import csv
import os

# Download necessary NLTK resources
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')  # POS tagger

# Initialize spell checker and lemmatizer
spell = SpellChecker()
lemmatizer = WordNetLemmatizer()

# Only download necessary NLTK resources if they're not already downloaded
nltk_resources = ['stopwords', 'punkt']
for resource in nltk_resources:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)


stop_words = set(stopwords.words('english'))
manual_stopwords = ['emoji','emotica']
stop_words.update(manual_stopwords)

def preprocess(text):
    # Tokenize and convert to lower case
    tokens = word_tokenize(text.lower())
    # Apply POS tagging
    tagged_tokens = pos_tag(tokens)
    # Filter to get adjectives only, identified by 'JJ', 'JJR', 'JJS' tags
    adjectives = [word for word, tag in tagged_tokens if tag in ('JJ', 'JJR', 'JJS') and word not in stop_words and word.isalpha()]
    print("processed one doc")
    return adjectives



cuisines = [ "Mexican","Japanese","Chinese","American"]

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    # Load the merged CSV file
    df = pd.read_csv(f"../data/output/merge{cuisine}.csv", usecols=['text','stars_y','business_id','user_id'], dtype={'text': 'string','stars_y':'int'})
    grouped_texts = df.groupby(['stars_y'])['text'].agg(lambda texts: ' '.join(texts)).reset_index()
    docs = grouped_texts['text'].tolist()

    f = open(f"../data/preprocessed/{cuisine}.txt", "w")
    for doc in docs:
        f.write(doc)
    f.close()
