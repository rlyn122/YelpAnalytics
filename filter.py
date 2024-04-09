import pandas as pd

def filter_businesses(df, min = 10):
    """
    Takes the businesses data frame and filters for minimum review count and for restaraunts
    """

    popular_businesses = df[df['review_count']>min]
    popular_restaraunts = popular_businesses[popular_businesses['categories'].str.contains('Restaurants|Food',na=False)]
    print("Number of restaraunts: "+ str(len(popular_restaraunts)))

    #select only certain attributes
    popular_restaraunts = popular_restaraunts[['business_id','categories','stars','name','state']]
    print(popular_restaraunts.head(5))
    return popular_restaraunts


print("Reading...\n")

df_business = pd.read_json('data/yelp_academic_dataset_business.json',lines=True)
df_reviews = pd.read_json('data/yelp_academic_dataset_review.json',lines=True)

print("Done reading...\n")

print("Now filtering: \n")
df_business = filter_businesses(df_business)

print("Merging...\n")
merged_data = df_business.merge(df_reviews,on='business_id',how='inner')
filtered_data = merged_data[['text']]


merged_data.to_csv("./data/output/merge.csv")


# df_business.to_csv("./data/output/businesses.csv",sep=',',index=False,encoding='utf-8')
# df_reviews.to_csv("./data/output/reviews.csv",sep=',',index=False,encoding='utf-8')