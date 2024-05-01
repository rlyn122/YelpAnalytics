import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter
import os
import pandas as pd
import csv

# Download necessary NLTK models
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

# Define stop words
stop_words = set(stopwords.words('english'))
manual_stopwords = ['emoji', 'emoticon','good','great','best','bad','first','new','nice','much']
stop_words.update(manual_stopwords)

def preprocess_and_find_adjectives(text):
    tokens = word_tokenize(text.lower())
    tagged_tokens = pos_tag(tokens)
    adjectives = [word for word, tag in tagged_tokens if tag in ('JJ', 'JJR', 'JJS') and word not in stop_words and word.isalpha()]
    return adjectives

def get_top_adjectives(text, top_n=10):
    adjectives = preprocess_and_find_adjectives(text)
    adjective_counts = Counter(adjectives)
    top_adjectives = adjective_counts.most_common(top_n)
    return top_adjectives

def save_adjectives(adjectives, cuisine):
    results_dir = "../results/TopAdjectivesByRating2"
    os.makedirs(results_dir, exist_ok=True)  # Ensure the directory exists
    filename = os.path.join(results_dir, f"{cuisine}_Top_Adjectives_.csv")
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Rating", "(Adjective, Count)"])
        for rating, adj_list in adjectives.items():
            writer.writerow([rating, adj_list])


cuisines = ["American"]

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    df = pd.read_csv(f"../data/output/merge{cuisine}.csv", usecols=['text','stars_y'], dtype={'text': 'string','stars_y':'int'})
    grouped_texts = df.groupby('stars_y')['text'].apply(lambda texts: ' '.join(texts)).reset_index()
    
    adjectives = {}
    for index, row in grouped_texts.iterrows():
        rating = row['stars_y']
        print(rating)
        text = row['text']
        print(text[:500])
        top_adjectives = get_top_adjectives(text)
        adjectives[rating] = top_adjectives

    save_adjectives(adjectives, cuisine)

