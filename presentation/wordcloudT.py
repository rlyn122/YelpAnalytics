from wordcloud import WordCloud
import matplotlib.pyplot as plt

ratings_data = [
[('worst', 3201), ('mexican', 2331), ('last', 2246), ('horrible', 2063), ('terrible', 2052), ('wrong', 1972), ('rude', 1803), ('sure', 1521), ('better', 1513), ('cold', 1512)],
[('mexican', 2244), ('better', 1350), ('little', 1235), ('last', 1107), ('small', 1068), ('sure', 1055), ('many', 901), ('hot', 819), ('disappointed', 778), ('fresh', 752)],
[('mexican', 3225), ('little', 2599), ('small', 1483), ('fresh', 1477), ('better', 1438), ('sure', 1302), ('delicious', 1278), ('hot', 1254), ('decent', 1168), ('friendly', 1147)],
[('mexican', 7010), ('delicious', 6301), ('little', 5398), ('fresh', 4862), ('friendly', 3387), ('tasty', 2995), ('hot', 2677), ('small', 2639), ('happy', 2465), ('sure', 2115)],
[('delicious', 15741), ('mexican', 12799), ('fresh', 10416), ('friendly', 7374), ('amazing', 6001), ('favorite', 5926), ('little', 5467), ('authentic', 5143), ('awesome', 5002), ('excellent', 4888)]

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
