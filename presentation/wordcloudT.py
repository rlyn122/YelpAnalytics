from wordcloud import WordCloud
import matplotlib.pyplot as plt

ratings_data = [
[('worst', 7569), ('last', 7261), ('terrible', 7060), ('horrible', 7034), ('cold', 6150), ('better', 5496), ('wrong', 5226), ('sure', 5052), ('rude', 4986), ('many', 4980)],
[('better', 7017), ('little', 6355), ('small', 5734), ('last', 5725), ('sure', 5274), ('many', 4978), ('hot', 4376), ('cold', 4359), ('dry', 4269), ('disappointed', 4112)],
[('little', 14597), ('small', 8342), ('delicious', 8056), ('better', 8049), ('sure', 7684), ('hot', 7057), ('overall', 6920), ('decent', 6663), ('friendly', 6618), ('many', 6351)],
[('delicious', 35974), ('little', 31075), ('friendly', 18909), ('fresh', 17298), ('hot', 15963), ('tasty', 14599), ('small', 14589), ('excellent', 13234), ('happy', 12864), ('sure', 12721)],
[('delicious', 72475), ('friendly', 35007), ('fresh', 31845), ('amazing', 30631), ('excellent', 27336), ('little', 26608), ('awesome', 26275), ('favorite', 25463), ('perfect', 23289), ('hot', 22475)]
]

# Combine all words into a single dictionary with summed counts
word_freq = {}

for rating in ratings_data:
    for word, count in rating:
        if word in word_freq:
            word_freq[word] += count
        else:
            word_freq[word] = count

# Generate a word cloud image
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Display the generated image:
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
