import json
import pandas as pd

def save_json(data):
    with open("data/data.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Saved to JSON")

def save_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("data/data.csv", index=False)
    print("Saved to CSV")