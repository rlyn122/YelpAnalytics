import matplotlib.pyplot as plt

# Data from your input
data = [
    [('good', 19434), ('bad', 10477), ('first', 8417), ('great', 8159), ('worst', 7569), ('last', 7261), ('terrible', 7060), ('horrible', 7034), ('cold', 6150), ('new', 6098)],
    [('good', 32483), ('great', 13786), ('nice', 8217), ('bad', 8084), ('first', 7761), ('better', 7017), ('much', 6629), ('little', 6355), ('small', 5734), ('last', 5725)],
    [('good', 64381), ('great', 27838), ('nice', 17368), ('little', 14597), ('first', 9272), ('much', 9214), ('bad', 9024), ('best', 8550), ('small', 8342), ('delicious', 8056)],
    [('good', 122185), ('great', 89366), ('nice', 36468), ('delicious', 35974), ('little', 31075), ('best', 19888), ('friendly', 18909), ('first', 17317), ('fresh', 17298), ('hot', 15963)],
    [('great', 161608), ('good', 110637), ('delicious', 72475), ('best', 60772), ('nice', 36586), ('friendly', 35007), ('fresh', 31845), ('amazing', 30631), ('excellent', 27336), ('little', 26608)]
]

# Prepare data for plotting
ratings = [f"Rating {i}" for i in range(1, 6)]
adjectives_dict = {rating: {adj: count for adj, count in adj_list} for rating, adj_list in zip(ratings, data)}

# Plotting
num_adjectives_to_plot = 5  # Number of top adjectives to plot

for rating in ratings:
    top_adjectives = list(adjectives_dict[rating].keys())[:num_adjectives_to_plot]
    counts = [adjectives_dict[rating][adj] for adj in top_adjectives]
    
    plt.figure(figsize=(10, 6))
    plt.bar(top_adjectives, counts, color='skyblue')
    plt.xlabel('Adjectives')
    plt.ylabel('Count')
    plt.title(f'Top {num_adjectives_to_plot} Adjectives for {rating}')
    plt.xticks(rotation=45)
    plt.show()
