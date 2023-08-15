from transformers import Pipeline


class sentiment_analysis:
    def __init__(self):
        self.sentiment_analyser = Pipeline(
            "sentiment-analysis", model="roberta-large")

    def analyse(self, df):
        sentiments = self.sentiment_analyser(df["Comment"].tolist())

        # Extract sentiment labels and scores
        sentiment_labels = [sentiment["label"] for sentiment in sentiments]
        sentiment_scores = [sentiment["score"] for sentiment in sentiments]

        # Add sentiment columns to the DataFrame
        df["Sentiment_Label"] = sentiment_labels
        df["Sentiment_Score"] = sentiment_scores

        return df


class analysis_displayer:
    def display(self):
        return
