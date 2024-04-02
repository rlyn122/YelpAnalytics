import pandas as pd

print('reading dataset...')
df = pd.read_json('yelp_dataset/yelp_academic_dataset_business.json',lines=True)
print(df)

min = 25

popular_businesses = df[df['review_count']>min]
print(f"number of {min} plus businesses: ", len(popular_businesses))

popular_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Restaurants',na=False)]
print(f"number of restaraunts with {min} reviews: ", len(popular_restaraunts))

restaraunts_by_state = popular_restaraunts.groupby("state").size()
print("restraunts by state: \n")
print(restaraunts_by_state)

#comment