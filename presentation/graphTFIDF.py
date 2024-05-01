import pandas as pd
import matplotlib.pyplot as plt

# TF-IDF data for Japanese cuisine
data = {
    "Rating": [1]*10 + [5]*10,
    "Word": [
        "worst", "last", "terrible", "horrible", "better", "small", "fresh", "many", "disappointed", "rude",
        "delicious", "fresh", "friendly", "favorite", "amazing", "little", "super", "excellent", "japanese", "sushi"
    ],
    "TF-IDF": [
        0.259, 0.247, 0.223, 0.211, 0.208, 0.182, 0.170, 0.164, 0.164, 0.158,
        0.493, 0.412, 0.226, 0.210, 0.176, 0.176, 0.169, 0.146, 0.143, 0.131
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Specific ratings to visualize
ratings = [1, 5]
colors = ['skyblue', 'salmon']  # Colors for each rating

# Create a figure for each selected rating
for i, rating in enumerate(ratings):
    plt.figure(figsize=(10, 6))  # Create a new figure for each rating
    sub_df = df[df['Rating'] == rating].sort_values(by='TF-IDF', ascending=False)
    plt.bar(sub_df['Word'], sub_df['TF-IDF'], color=colors[i])
    plt.title(f'Top Words for Rating {rating} - Japanese Cuisine')
    plt.ylabel('TF-IDF')
    plt.xlabel('Words')
    plt.xticks(rotation=45)
    plt.show()
