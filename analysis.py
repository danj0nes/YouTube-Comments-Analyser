from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load RoBERTa sentiment analysis model
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Class for conducting sentiment analysis


class SentimentAnalysis:
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

# Class for displaying sentiment analysis results


class AnalysisDisplayer:
    def display(self, df):
        # Find the most positive comment
        most_positive_index = df["Positive"].idxmax()
        most_positive_comment = df.loc[most_positive_index, "Comment"]
        most_positive_score = df.loc[most_positive_index, "Positive"]

        print("Most Positive Comment:")
        print("Comment:", most_positive_comment)
        print("Positive Score:", most_positive_score)
        print()

        # Find the most negative comment
        most_negative_index = df["Negative"].idxmax()
        most_negative_comment = df.loc[most_negative_index, "Comment"]
        most_negative_score = df.loc[most_negative_index, "Negative"]

        print("Most Negative Comment:")
        print("Comment:", most_negative_comment)
        print("Negative Score:", most_negative_score)
        print()

        # Calculate the average positive score
        average_positive_score = df["Positive"].mean()
        print("Average Positive Score:", average_positive_score)

    def display_positive_graph(self, df):
        # Calculate intervals for positive scores
        num_intervals = 10
        interval_size = 1.0 / num_intervals
        interval_ranges = [(i * interval_size, (i + 1) * interval_size)
                           for i in range(num_intervals)]

        # Calculate the count of comments in each positive interval
        interval_counts = [((df["Positive"] >= lower) & (
            df["Positive"] < upper)).sum() for lower, upper in interval_ranges]

        # Create a bar chart for positive scores distribution
        plt.bar(range(num_intervals), interval_counts, tick_label=[
                f"{lower:.1f}-{upper:.1f}" for lower, upper in interval_ranges])
        plt.xlabel("Positive Score Intervals")
        plt.ylabel("Number of Comments")
        plt.title("Distribution of Positive Scores")
        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()
        plt.show()

    def display_negative_graph(self, df):
        # Calculate intervals for negative scores
        num_intervals = 10
        interval_size = 1.0 / num_intervals
        interval_ranges = [(i * interval_size, (i + 1) * interval_size)
                           for i in range(num_intervals)]

        # Calculate the count of comments in each negative interval
        interval_counts = [((df["Negative"] >= lower) & (
            df["Negative"] < upper)).sum() for lower, upper in interval_ranges]

        # Create a bar chart for negative scores distribution
        plt.bar(range(num_intervals), interval_counts, tick_label=[
                f"{lower:.1f}-{upper:.1f}" for lower, upper in interval_ranges])
        plt.xlabel("Negative Score Intervals")
        plt.ylabel("Number of Comments")
        plt.title("Distribution of Negative Scores")
        plt.xticks(rotation=45, ha="right")

        plt.tight_layout()
        plt.show()
