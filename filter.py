import pandas as pd

print('reading dataset...')
df = pd.read_json('yelp_dataset/yelp_academic_dataset_business.json',lines=True)
print(df)

min = 25
popular_businesses = df[df['review_count']>min]
print('number of {min} plus businesses ', len(popular_businesses))


