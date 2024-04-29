import pandas as pd

print('reading dataset...')
df = pd.read_json('data/yelp_academic_dataset_business.json',lines=True)

lendf = len(df[(df["review_count"] > 10) & (df["categories"].str.contains("Chinese", na=False)) & (df["categories"].str.contains("Restaraunt|Food", na=False))])

print("number of Chinese Restaraunts in merge.csv: " + str(lendf))
