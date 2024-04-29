import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from gensim.corpora import Dictionary
from gensim.models import LdaModel
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



cuisines = ["American", "Mexican" ]
results_dir = "../results/byRating/Adjectives"
os.makedirs(results_dir, exist_ok=True)  # Ensure the results directory exists

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    # Load the merged CSV file
    df = pd.read_csv(f"./data/output/merge{cuisine}.csv", usecols=['text','stars_y','business_id','user_id'], dtype={'text': 'string','stars_y':'int'})
    print("csv loaded:")
    print(df.columns)
    grouped_texts = df.groupby(['stars_y'])['text'].agg(lambda texts: ' '.join(texts)).reset_index()
    docs = grouped_texts['text'].tolist()

    print("docs being processed..")
    reviews = [preprocess(v) for v in docs]
    print("preprocessing done..")
    print(len(reviews))
    for i in range(len(reviews)):
        print(len(reviews[i]))
        print(reviews[i][0:30])

    
    dictionary = Dictionary(reviews)
    dictionary.filter_extremes(no_below=2, no_above=0.5)
    corpus = [dictionary.doc2bow(doc) for doc in reviews]    

    dictionary[0]
    id2word = dictionary.id2token
    if not corpus:
        print(f"Corpus is empty after applying dictionary for {cuisine}. Skipping...")
        continue

    print("setting training parameters... ")
    # Set training parameters for LDA
    model = LdaModel(
        corpus=corpus,
        id2word=id2word,
        chunksize=2000,
        alpha='auto',
        eta='auto',
        iterations=400,
        num_topics=5,
        passes=20,
        eval_every=None  # Skip model evaluation to save time
    )

    # Print the topics found by the LDA model
    topics = model.print_topics(num_words=10)
    filename = os.path.join(results_dir, f"{cuisine}Topics.csv")

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Topic ID", "Words and Weights"])
        for topic_id, topic in topics:
            writer.writerow([f"Topic {topic_id}", topic])
            
    print(f"Topics written to {filename}")
