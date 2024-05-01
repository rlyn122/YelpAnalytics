import matplotlib.pyplot as plt

# Data from your input
data = [
    (1, 'worst', 0.25111730240199065, 7569),
    (1, 'last', 0.2408987624178695, 7261),
    (1, 'terrible', 0.2342301697658943, 7060),
    (1, 'horrible', 0.23336756574126072, 7034),
    (1, 'cold', 0.20403902890371814, 6150),
    (2, 'better', 0.25155862067151696, 7017),
    (2, 'little', 0.22782599891228306, 6355),
    (2, 'small', 0.20556322230732196, 5734),
    (2, 'last', 0.20524057337101817, 5725),
    (2, 'sure', 0.18907227667401744, 5274),
    (3, 'little', 0.3500847733852375, 14597),
    (3, 'small', 0.20006899908060913, 8342),
    (3, 'delicious', 0.19320976463598505, 8056),
    (3, 'better', 0.19304188127545227, 8049),
    (4, 'delicious', 0.3986293825225456, 35974),
    (4, 'little', 0.3443433608130345, 31075),
    (4, 'friendly', 0.20953141141154205, 18909),
    (4, 'fresh', 0.19167985375201516, 17298),
    (5, 'delicious', 0.5089405833498517, 72475),
    (5, 'friendly', 0.24582936186724055, 35007),
    (5, 'fresh', 0.2236248758437534, 31845),
    (5, 'amazing', 0.2150998138473861, 30631),
    (5, 'excellent', 0.19196136304175987, 27336),
    (5, 'little', 0.18684913476057752, 26608),
    (5, 'awesome', 0.18451071165943228, 26275),
    (5, 'favorite', 0.17880861088426733, 25463),
    (5, 'perfect', 0.16354214895667055, 23289),
    (5, 'hot', 0.15782600359831553, 22475)
]

# Organize data into dictionaries for each rating
ratings_data = {1: [], 2: [], 3: [], 4: [], 5: []}

for rating, word, tfidf, frequency in data:
    ratings_data[rating].append((word, tfidf, frequency))

# Plotting top TF-IDF scores for each rating
plt.figure(figsize=(14, 12))

for i, (rating, items) in enumerate(ratings_data.items(), 1):
    # Sort items by TF-IDF score in descending order
    items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
    top_words = [item[0] for item in items_sorted[:5]]
    tfidf_scores = [item[1] for item in items_sorted[:5]]
    
    plt.subplot(3, 2, i)
    plt.barh(top_words, tfidf_scores, color='skyblue')
    plt.xlabel('TF-IDF Score')
    plt.title(f'Rating {rating}')
    plt.gca().invert_yaxis()  # Invert y-axis for better readability

plt.tight_layout()
plt.show()

