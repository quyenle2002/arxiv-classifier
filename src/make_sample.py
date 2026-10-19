import json
import random
import pandas as pd

random.seed(0)
rows = []
with open("data/arxiv-metadata-oai-snapshot.json", encoding="utf-8") as f:
    for line in f:
        if random.random() < 0.02:
            p = json.loads(line)
            rows.append({
                "id": p["id"],
                "title": p["title"],
                "abstract": p["abstract"],
                "categories": p["categories"],
            })

pd.DataFrame(rows).to_csv("data/sample.csv", index=False)
print(len(rows))