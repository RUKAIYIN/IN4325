############################################
# This script implements the LTR baseline
# Author: Rukai Yin
############################################

# linear algebra
import numpy as np 

# data processing
import pandas as pd 

# Regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

#  Training Techniques
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# Read table features from the file. Please refer to the report or the table features file to get more information about them.
df = pd.read_csv("/.../features.csv") # TBD: Fill in the file path to run the script

# Check missing data
total = df.isnull().sum().sort_values(ascending=False)
percent_1 = df.isnull().sum()/df.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])
missing_data.head(5) # turns out no missing data

# We extract training data and true lables
data = df.drop(['query', 'table_id'], axis=1)
X_train = data.drop("rel", axis=1) # features
Y_train = data["rel"] # lables

# Random Forest Regressor
# Number of trees = 1000, number of features in each tree = 3
random_forest = RandomForestRegressor(max_features=3, n_estimators=1000)
random_forest.fit(X_train, Y_train)

# We train the regressor using 5-fold cross-validation
scores = cross_val_score(random_forest, X_train, Y_train, cv=5)

# Now we will rank the tables based on their regression scores
ltr = df[["query_id", "table_id"]].copy()
y_pre= random_forest.predict(X_test)
ltr['score'] = y_pre.tolist()
ltr_ = ltr.sort_values(by=['query_id', 'score'], ascending = [True, False]).copy()
ltr_.groupby('query_id')[['query_id', 'score']].rank(ascending=False)

# Add two more columns to fit the input format of trec_eval tool
ltr_["query"] = "Q0"
ltr_["table"] = "smarttable"

# We take the first 5, 10, 15, 20 rankings
ltr_5 = ltr_[ltr_["rank"] < 6]
ltr_10 = ltr_[ltr_["rank"] < 11]
ltr_15 = ltr_[ltr_["rank"] < 16]
ltr_20 = ltr_[ltr_["rank"] < 21]

# We write all rankings into files
# TBD: Fill in the file path to run the script
ltr_5.to_csv(r'/.../LTR_5.csv', header=None, index=None, sep=',')
ltr_10.to_csv(r'/.../LTR_10.csv', header=None, index=None, sep=',')
ltr_15.to_csv(r'/.../LTR_15.csv', header=None, index=None, sep=',')
ltr_20.to_csv(r'/.../LTR_20.csv', header=None, index=None, sep=',')

# We will then feed the files to trec_eval and get the NDCG results
