from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


class sentiment_analysis:
    def analyse(self, df):
        print("This may take a while...")

        comments = df["Comment"].tolist()

        sentiment_labels = ["Negative", "Neutral", "Positive"]
        sentiment_columns = {label: [] for label in sentiment_labels}

        for comment in comments:
            inputs = tokenizer(
                comment, padding=True, truncation=True, return_tensors="pt")
            outputs = model(**inputs)
            scores = outputs.logits[0].detach().numpy()
            scores = softmax(scores)

            for label, score in zip(sentiment_labels, scores):
                sentiment_columns[label].append(score)

        # Add sentiment score columns to the DataFrame
        for label in sentiment_labels:
            df[label] = sentiment_columns[label]

        return df


class analysis_displayer:
    def display(self):
        return
