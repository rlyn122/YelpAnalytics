import matplotlib.pyplot as plt
import numpy as np

# Data from your input
data = [
[('worst', 7569), ('last', 7261), ('terrible', 7060), ('horrible', 7034), ('cold', 6150), ('better', 5496), ('wrong', 5226), ('sure', 5052), ('rude', 4986), ('many', 4980)],
[('better', 7017), ('little', 6355), ('small', 5734), ('last', 5725), ('sure', 5274), ('many', 4978), ('hot', 4376), ('cold', 4359), ('dry', 4269), ('disappointed', 4112)],
[('little', 14597), ('small', 8342), ('delicious', 8056), ('better', 8049), ('sure', 7684), ('hot', 7057), ('overall', 6920), ('decent', 6663), ('friendly', 6618), ('many', 6351)],
[('delicious', 35974), ('little', 31075), ('friendly', 18909), ('fresh', 17298), ('hot', 15963), ('tasty', 14599), ('small', 14589), ('excellent', 13234), ('happy', 12864), ('sure', 12721)],
[('delicious', 72475), ('friendly', 35007), ('fresh', 31845), ('amazing', 30631), ('excellent', 27336), ('little', 26608), ('awesome', 26275), ('favorite', 25463), ('perfect', 23289), ('hot', 22475)]

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
colors = ['blue', 'salmon', 'green', 'purple', 'orange']  # Color for each rating
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
