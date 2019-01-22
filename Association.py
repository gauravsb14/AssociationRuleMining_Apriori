import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

# importing data file
data = pd.read_csv('/home/gaurav/AI/Proiba_ML/Clustering/data/store_data.csv')

# print and check data
print(data.head())


# in the data set there is no header row so create none header
data = pd.read_csv('/home/gaurav/AI/Proiba_ML/Clustering/data/store_data.csv', header=None)

# print and check data
print(data.head())

# The Apriori library we are going to use requires our dataset to be in the form of a list of lists
# transaction is represented as inner list
records = []
for i in range(0, 7499):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

print(records)

association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, min_length=2)
association_rules = list(association_rules)

# results
len(association_rules)

# to check the first rule
print(association_rules[0])

for item in association_rules:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0]
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")