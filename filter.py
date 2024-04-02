import pandas as pd

print('reading dataset...')
df = pd.read_json('data/yelp_academic_dataset_business.json',lines=True)
print(df.head(10))


min = 25

popular_businesses = df[df['review_count']>min]
print(f"number of {min} plus businesses: ", len(popular_businesses))

popular_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Restaurants',na=False)]
print(f"number of restaraunts with {min} reviews: ", len(popular_restaraunts))

restaraunts_by_state = popular_restaraunts.groupby("state").size()

chinese_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Chinese',na=False)]
print("Chinese restaraunts ", len(chinese_restaraunts))

American_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('American',na=False)]
print("American restaraunts ", len(American_restaraunts))

Japanese_r = popular_businesses[popular_businesses['categories'].str.contains('Japanese',na=False)]
print("Japanese restaraunts ", len(Japanese_r))

mexican_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Mexican',na=False)]
print("mexican restaraunts ", len(mexican_restaraunts))

print("restraunts by state: \n")
print(restaraunts_by_state)

#comment