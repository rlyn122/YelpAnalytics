import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter
import csv
import nltk

# Download necessary NLTK models
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

# Define stop words
stop_words = set(stopwords.words('english'))
manual_stopwords = ['emoji', 'emoticon', 'good', 'great', 'best', 'bad', 'first', 'new', 'nice', 'much']
stop_words.update(manual_stopwords)

def preprocess_and_find_adjectives(text):
    tokens = word_tokenize(text.lower())
    tagged_tokens = pos_tag(tokens)
    return ' '.join([word for word, tag in tagged_tokens if tag in ('JJ', 'JJR', 'JJS') and word not in stop_words and word.isalpha()])

def tfidf_analysis(grouped_texts):
    # Prepare data for TF-IDF analysis
    docs = grouped_texts['text'].tolist()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    return pd.DataFrame(dense, columns=feature_names, index=grouped_texts['stars_y'])

def save_tfidf(df_tfidf, cuisine):
    results_dir = "../results/TFIDFAnalysisByRating"
    os.makedirs(results_dir, exist_ok=True)
    filename = os.path.join(results_dir, f"{cuisine}_TFIDF.csv")
    df_tfidf.to_csv(filename)

cuisines = ["Mexican", "Chinese", "Japanese", "American"]

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    df = pd.read_csv(f"../data/output/merge{cuisine}.csv", usecols=['text', 'stars_y'], dtype={'text': 'string', 'stars_y': 'int'})
    grouped_texts = df.groupby('stars_y')['text'].apply(lambda texts: ' '.join(texts)).reset_index()
    grouped_texts['text'] = grouped_texts['text'].apply(preprocess_and_find_adjectives)
    
    df_tfidf = tfidf_analysis(grouped_texts)
    save_tfidf(df_tfidf, cuisine)
