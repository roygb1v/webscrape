import pandas as pd
import string
from sklearn.feature_extraction import text
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
#Load spreadsheet
file = 'redmart.xlsx'
xl = pd.ExcelFile(file)
print(xl.sheet_names)
df1 = xl.parse('Sheet1')


def remove_punctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s

df1["Full Text"] = df1["Full Text"].apply(remove_punctuation)

#Regex to remove stopwords
stopwords = text.ENGLISH_STOP_WORDS
pat = r'\b(?:{})\b'.format('|'.join(stopwords))
df1["Full Text"] = df1["Full Text"].str.replace(pat, '')
df1["Full Text"] = df1["Full Text"].str.replace(r'\s+', ' ')

#Define feature and response 
X = df1["Full Text"]
y = df1["Sentiment"]

X_train, X_test, y_train, y_test = train_test_split(df1['Full Text'],
                                                    pd.get_dummies(df1['Sentiment']), 
                                                    random_state=456)
"""pl = Pipeline([
        ('vec', CountVectorizer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

pl.fit(X_train, y_train)
accuracy = pl.score(X_test, y_test)
print("\nAccuracy on sample data - just text data: ", accuracy) """

#Apply KNN
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state= 42, stratify= y)
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)                    
#print(knn.score(X_test, y_test))