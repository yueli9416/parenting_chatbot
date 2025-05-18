import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("parenting_posts_emotion_tagged.csv")

def save_emotion_wordcloud(df, emotion_label, filename):
    text_data = " ".join(df[df["emotion_label"] == emotion_label]["clean_text"].dropna())
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          stopwords=stopwords, max_words=100, collocations=False).generate(text_data)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(f"Word Cloud for Emotion: {emotion_label}", fontsize=16)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(filename, format='png')
    plt.close()
    print(f"Saved: {filename}")


save_emotion_wordcloud(df, "anger", "wordcloud_anger.png")
save_emotion_wordcloud(df, "joy", "wordcloud_joy.png")
