import pandas as pd
from pandas import DataFrame
from itertools import groupby
from collections import OrderedDict
import json

# df = pd.read_csv("trainDseoul.csv")
# print(df)

# pd.DataFrame(df)

# # print(len(df.drop_duplicates()))

# df_nodup = df.drop_duplicates()

# print(df_nodup)

# ((pd.DataFrame(pd.read_csv("trainDseoul.csv"))).drop_duplicates())




df = pd.read_csv("trainDseoul.csv", dtype={
    "TranType" : str,
    "WayType" : str,
    "TrainType" : str,
    "DepCity" : str,
    "ArrCity" : str,
    "DepTime" : str,
    "ArrTime" : str,
    "Month" : str,
    "Day" : str
})
# print(df)
results = []

pd.DataFrame(df)

# print(len(df.drop_duplicates()))

df_nodup = df.drop_duplicates()
print(df_nodup)
# print(df_nodup)

for (DepCity, ArrCity), bag in df_nodup.groupby(["DepCity", "ArrCity"]):
    contents_df = bag.drop(["DepCity", "ArrCity"], axis=1)
    subset = [OrderedDict(row) for i,row in contents_df.iterrows()]
    results.append(OrderedDict([("DepCity", DepCity),
                                ("ArrCity", ArrCity), 
                                ("subset", subset)]))

with open("train_seoul.json", 'w') as outfile:
    outfile.write(json.dumps(results[0], indent=4))

print (json.dumps(results[0], indent=4))