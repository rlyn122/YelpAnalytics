import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import csv
import os

# Only download necessary NLTK resources if they're not already downloaded
nltk_resources = ['stopwords', 'punkt']
for resource in nltk_resources:
    try:
        nltk.data.find(f'tokenizers/{resource}')
    except LookupError:
        nltk.download(resource)

# Initialize stopwords once, outside the loop
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lower case
    filtered_tokens = [w for w in tokens if w not in stop_words and w.isalpha()]  # Remove stopwords and non-alphabetic tokens
    # if not filtered_tokens:
        # print("Empty after filtering:", text)  # Debug statement to check what's getting filtered out
    return filtered_tokens



cuisines = ["American", "Chinese", "Mexican", "Japanese",""]
results_dir = "./results/"
os.makedirs(results_dir, exist_ok=True)  # Ensure the results directory exists

for cuisine in cuisines:
    print(f"Processing {cuisine}")
    try:
        # Load the merged CSV file
        df = pd.read_csv(f"./data/output/merge{cuisine}.csv", usecols=['text'], dtype={'text': 'string'})
        print(df['text'].apply(lambda x: isinstance(x, str)).all())  # Ensure all entries are strings

        reviews = df['text'].tolist()
        print(f"Loaded {len(reviews)} reviews for {cuisine}")

        processed_reviews = [preprocess(review) for review in reviews]

        # Create a dictionary and corpus

        # After preprocessing
        non_empty_reviews = [doc for doc in processed_reviews if doc]  # Filter out empty documents 
        
        dictionary = Dictionary(non_empty_reviews)
        dictionary.filter_extremes(no_below=2, no_above=0.5)
        corpus = [dictionary.doc2bow(doc) for doc in non_empty_reviews]    

        temp = dictionary[0]
        id2word = dictionary.id2token

        print("setting training parameters... ")
        # Set training parameters for LDA
        model = LdaModel(
            corpus=corpus,
            id2word=dictionary.id2token,
            chunksize=2000,
            alpha='auto',
            eta='auto',
            iterations=400,
            num_topics=10,
            passes=20,
            eval_every=None  # Skip model evaluation to save time
        )

        # Print the topics found by the LDA model
        print("Creating topics...")
        topics = model.print_topics(num_words=10)
        filename = os.path.join(results_dir, f"{cuisine}Topics.csv")

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([f"Number of Reviews Sampled {len(non_empty_reviews)}"])
            writer.writerow(["Topic ID", "Words and Weights"])
            for topic_id, topic in topics:
                writer.writerow([f"Topic {topic_id}", topic])
                
        print(f"Topics written to {filename}")
    except Exception as e:
        print(f"Error processing {cuisine}: {e}")
