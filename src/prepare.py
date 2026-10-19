import pandas as pd
from sklearn.model_selection import train_test_split

classes = ["cs","math","cond-mat","astro-ph","physics","hep-ph"
           ,"quant-ph","hep-th","eess","gr-qc", "stat"]

df = pd.read_csv("data/sample.csv")
df["label"] = df["categories"].str.split().str[0].str.split(".").str[0]
df = df[df["label"].isin(classes)]
df["text"] = (df["title"] + " " + df["abstract"]).str.replace(r"\s+", " ", regex=True).str.strip()
df = df[["id", "text", "label"]]

train, temp = train_test_split(df, test_size=0.3, stratify=df["label"], random_state=0)
val, test = train_test_split(temp, test_size=0.5, stratify=temp["label"], random_state=0)

train.to_csv("data/train.csv", index=False)
val.to_csv("data/val.csv", index=False)
test.to_csv("data/test.csv", index=False)

print(len(train), len(val), len(test))
print(train["label"].value_counts(normalize=True).round(3))