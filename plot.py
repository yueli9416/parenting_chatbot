import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

df = pd.read_csv("parenting_posts_emotion_tagged.csv")

# bar
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="emotion_label", order=df["emotion_label"].value_counts().index, palette="Set2")
plt.title("Emotion Label Distribution")
plt.xlabel("Emotion")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("emotion_label_distribution.png")
plt.show()

# word cloud
text = " ".join(df["clean_text"].dropna().astype(str))

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Parenting Posts")
plt.tight_layout()
plt.savefig("word_cloud.png")
plt.show()
