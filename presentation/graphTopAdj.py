import matplotlib.pyplot as plt
import numpy as np

# Data from your input
data = [
[('worst', 3201), ('mexican', 2331), ('last', 2246), ('horrible', 2063), ('terrible', 2052), ('wrong', 1972), ('rude', 1803), ('sure', 1521), ('better', 1513), ('cold', 1512)],
[('mexican', 2244), ('better', 1350), ('little', 1235), ('last', 1107), ('small', 1068), ('sure', 1055), ('many', 901), ('hot', 819), ('disappointed', 778), ('fresh', 752)],
[('mexican', 3225), ('little', 2599), ('small', 1483), ('fresh', 1477), ('better', 1438), ('sure', 1302), ('delicious', 1278), ('hot', 1254), ('decent', 1168), ('friendly', 1147)],
[('mexican', 7010), ('delicious', 6301), ('little', 5398), ('fresh', 4862), ('friendly', 3387), ('tasty', 2995), ('hot', 2677), ('small', 2639), ('happy', 2465), ('sure', 2115)],
[('delicious', 15741), ('mexican', 12799), ('fresh', 10416), ('friendly', 7374), ('amazing', 6001), ('favorite', 5926), ('little', 5467), ('authentic', 5143), ('awesome', 5002), ('excellent', 4888)]

]

# Prepare data for plotting
ratings = [f"Rating {i}" for i in range(1, 6)]
adjectives_dict = {rating: {adj: count for adj, count in adj_list} for rating, adj_list in zip(ratings, data)}

# Consolidate adjectives for all ratings
all_adjectives = set()
for adj_list in data:
    all_adjectives.update([adj for adj, _ in adj_list])

# Create a plot data structure
plot_data = {adj: [adjectives_dict.get(rating, {}).get(adj, 0) for rating in ratings] for adj in all_adjectives}

# Create arrays for plotting
adjectives = list(plot_data.keys())
values = np.array(list(plot_data.values()))

# Plotting
colors = ['blue', 'red', 'green', 'grey', 'black']  # Color for each rating
fig, ax = plt.subplots(figsize=(15, 10))
bottom = np.zeros(len(adjectives))

for idx, rating in enumerate(ratings):
    ax.bar(adjectives, values[:, idx], bottom=bottom, label=rating, color=colors[idx])
    bottom += values[:, idx]

ax.set_xlabel('Adjectives')
ax.set_ylabel('Count')
ax.set_title('Comparison of Top Adjectives Across Different Ratings')
ax.set_xticks(range(len(adjectives)))
ax.set_xticklabels(adjectives, rotation=45)
ax.legend(title='Ratings')

plt.show()
