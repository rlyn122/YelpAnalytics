import pandas as pd
import csv

def filter_businesses(df, cuisine, min = 10):
    """
    Takes the businesses data frame and filters for minimum review count and for restaraunts
    """

    popular_businesses = df[df['review_count']>min]

    conditions = popular_businesses['categories'].str.contains('Restaraunts|Food',na=False) & popular_businesses['categories'].str.contains(cuisine,na=False)
    popular_restaraunts = popular_businesses[conditions]
    print(f"Number of restaraunts for {cuisine}: {str(len(popular_restaraunts))}")

    #select only certain attributes
    popular_restaraunts = popular_restaraunts[['business_id','categories','stars','name','state']]
    return popular_restaraunts


print("Reading...\n")

df_business = pd.read_json('data/yelp_academic_dataset_business.json',lines=True)
df_reviews = pd.read_json('data/yelp_academic_dataset_review.json',lines=True)
df_reviews['text'] = df_reviews['text'].apply(lambda x: x.replace('\n', ' ').replace('\r', ' '))

print("Done reading...\n")

cuisines = ["American","Chinese","Mexican","Japanese"]

for cuisine in cuisines:
    print(f"Now filtering for {cuisine}: \n")
    df_filtered = filter_businesses(df_business,cuisine)

    print("Merging...\n")
    merged_data = df_filtered.merge(df_reviews,on='business_id',how='inner')
    merged_data.to_csv(f"./data/output/merge{cuisine}.csv", quoting=csv.QUOTE_NONNUMERIC)


# df_business.to_csv("./data/output/businesses.csv",sep=',',index=False,encoding='utf-8')
# df_reviews.to_csv("./data/output/reviews.csv",sep=',',index=False,encoding='utf-8') 