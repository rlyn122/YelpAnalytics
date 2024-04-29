import pandas as pd

def filter_businesses(df, min = 25):
    """
    Takes the businesses data frame and filters for minimum review count and for restaraunts
    """
    popular_businesses = df[df['review_count']>min]
    popular_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Restaurants|Food',na=False)]
    print("Number of restaraunts: "+len(popular_restaraunts))
    return popular_restaraunts

df_business = pd.read_json('data/yelp_academic_dataset_business.json',lines=True)
df_reviews = pd.read_json('data/yelp_academic_dataset_review.json',lines=True)

df_business.merge(df_reviews)
print(df_business.head(10))