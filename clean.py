import re
import pandas as pd

df = pd.read_csv("parenting_posts_ai_mentions.csv")

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["raw_text"] = df["title"].fillna('') + " " + df["selftext"].fillna('')
df["clean_text"] = df["raw_text"].apply(clean_text)
df_cleaned = df.copy()
df_cleaned.to_csv("parenting_posts_cleaned.csv", index=False)

