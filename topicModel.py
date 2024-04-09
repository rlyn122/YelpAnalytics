import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.corpora import Dictionary
from gensim.models import LdaModel

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Load the merged CSV file
df = pd.read_csv("./data/output/merge.csv")

# Assume 'text' is the column with review texts and 'stars' is the ratings
documents = df['text'].tolist()
ratings = df['stars'].tolist()  # This could be used for different analyses

# Text preprocessing
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lower case
    filtered_tokens = [w for w in tokens if w not in stop_words and w.isalpha()]  # Remove stopwords and non-alphabetic tokens
    return filtered_tokens

processed_docs = [preprocess(doc) for doc in documents]

# Create a dictionary representation of the documents
dictionary = Dictionary(processed_docs)
dictionary.filter_extremes(no_below=2, no_above=0.5)  # Adjust thresholds according to your dataset

# Create a bag-of-words model for each document
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

# Set training parameters for LDA
num_topics = 5
chunksize = 2000
passes = 20
iterations = 400
eval_every = None  # optimization to skip model evaluation

# Train the LDA model
model = LdaModel(
    corpus=corpus,
    id2word=dictionary.id2token,
    chunksize=chunksize,
    alpha='auto',
    eta='auto',
    iterations=iterations,
    num_topics=num_topics,
    passes=passes,
    eval_every=eval_every
)

# Print the topics found by the LDA model
topics = model.print_topics(num_words=10)
for topic_id, topic in topics:
    print(f"Topic {topic_id}: {topic}")
