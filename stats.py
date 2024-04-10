import pandas as pd

print('reading dataset...')
df = pd.read_csv("./data/output/merge.csv")

print("number of reviews in merge.csv: " + str(len(df)))


print(df.head(10))

