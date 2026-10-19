import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

train = pd.read_csv("data/train.csv")
val = pd.read_csv("data/val.csv")

vec = TfidfVectorizer(max_features=50000, sublinear_tf=True, stop_words="english")
X_train = vec.fit_transform(train["text"])
X_val = vec.transform(val["text"])

dummy = DummyClassifier(strategy="most_frequent").fit(X_train, train["label"])
p = dummy.predict(X_val)
print("majority:", accuracy_score(val["label"], p), f1_score(val["label"], p, average="macro"))

clf = LogisticRegression(max_iter=1000).fit(X_train, train["label"])
p = clf.predict(X_val)
print("logreg:", accuracy_score(val["label"], p), f1_score(val["label"], p, average="macro"))
print(classification_report(val["label"], p, digits=3))