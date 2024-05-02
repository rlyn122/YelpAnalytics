import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# CSV data for Japanese cuisine reviews

for cuisine in ["Japanese","American","Chinese","Mexican"]:
    csv_data = pd.read_csv(f"../results/TFIDF/adj/{cuisine}_TFIDF.csv")
    # Create DataFrame from CSV data
    data = csv_data

    # Specific ratings to visualize
    ratings = [1, 2, 3, 4, 5]
    colors = ['skyblue', 'lightgreen', 'tan', 'salmon', 'violet']  # Colors for each rating

    # Create a figure for each selected rating
    for i, rating in enumerate(ratings):
        plt.figure(figsize=(10, 6))  # Create a new figure for each rating
        sub_df = data[data['Rating'] == rating].sort_values(by='TF-IDF', ascending=False)
        plt.bar(sub_df['Word'], sub_df['TF-IDF'], color=colors[i])
        plt.title(f'Top Words for Rating {rating} - {cuisine} Cuisine')
        plt.ylabel('TF-IDF')
        plt.xlabel('Words')
        plt.xticks(rotation=45)
        
        # Save plot to file
        plt.savefig(f'./graphs/TFIDF/{cuisine}{rating}_TFIDF.png')  # Save the figure
        