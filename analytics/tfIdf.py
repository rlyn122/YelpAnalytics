import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter
import nltk

# Download necessary NLTK models
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('stopwords')

# Define stop words
stop_words = set(stopwords.words('english'))
manual_stopwords = ['emoji', 'emoticon', 'good', 'great', 'best', 'bad', 'first', 'new', 'nice', 'much']
stop_words.update(manual_stopwords)

def tokenize_words(text):
    tokens = word_tokenize(text.lower())  
    return ' '.join([word for word in tokens if word.isalpha() and word not in stop_words])
def extract_top_words_with_freq(df_tfidf, df_freq, top_n=10):
    top_words_data = []
    for index in df_tfidf.index:
        top_n_words = df_tfidf.loc[index].sort_values(ascending=False).head(top_n).index
        for word in top_n_words:
            top_words_data.append({
                "Rating": index,
                "Word": word,
                "TF-IDF": df_tfidf.at[index, word],
                "Frequency": df_freq.at[index, word]
            })
    return pd.DataFrame(top_words_data)

def tfidf_analysis(grouped_texts, top_n=10):
    docs = grouped_texts['text'].tolist()
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    feature_names = vectorizer.get_feature_names_out()
    dense = tfidf_matrix.todense()
    df_tfidf = pd.DataFrame(dense, columns=feature_names, index=grouped_texts['stars_y'])

    word_counts = []
    for doc in docs:
        words = doc.split()
        word_count = Counter(words)
        word_counts.append(dict(word_count))  

    df_freq = pd.DataFrame(word_counts, index=grouped_texts['stars_y']).fillna(0)
    return df_tfidf, df_freq

def save_tfidf(df_tfidf, cuisine):
    results_dir = "../results/TFIDFAnalysisByRatingAll"
    os.makedirs(results_dir, exist_ok=True)
    filename = os.path.join(results_dir, f"{cuisine}_TFIDF.csv")
    df_tfidf.to_csv(filename, index=False)  

cuisines = ["Mexican", "Chinese", "Japanese", "American"]

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    df = pd.read_csv(f"../data/output/merge{cuisine}.csv", usecols=['text', 'stars_y'], dtype={'text': 'string', 'stars_y': 'int'})
    grouped_texts = df.groupby('stars_y')['text'].apply(lambda texts: ' '.join(texts)).reset_index()
    grouped_texts['text'] = grouped_texts['text'].apply(tokenize_words)

    df_tfidf, df_freq = tfidf_analysis(grouped_texts)
    top_words_with_freq = extract_top_words_with_freq(df_tfidf, df_freq, top_n=10)
    save_tfidf(top_words_with_freq, cuisine)
