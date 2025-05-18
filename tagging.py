import pandas as pd
from transformers import pipeline

df = pd.read_csv("parenting_posts_cleaned.csv")

df = df[df["clean_text"].apply(lambda x: isinstance(x, str))].copy()

emotion_classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    top_k=1
)

def get_emotion(text):
    try:
        output = emotion_classifier(text[:512])
        result = output[0][0] if isinstance(output[0], list) else output[0]
        return result['label'], result['score']
    except Exception as e:
        print(f"Error for text: {text[:100]}... → {str(e)}")
        return "error", 0.0

results = df["clean_text"].apply(get_emotion)
df["emotion_label"], df["emotion_score"] = zip(*results)

df.to_csv("parenting_posts_emotion_tagged.csv", index=False)

print(df["emotion_label"].value_counts())
