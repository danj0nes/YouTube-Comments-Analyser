import pandas as pd
from youtube_manager import youtube_manager
from analysis import sentiment_analysis, analysis_displayer

# Load the YouTube Data API v3 API Key from key.txt
with open("key.txt", "r") as key_file:
    API_KEY = key_file.read().strip()


# Function to check if DataFrame has the required number of columns
def valid_df(required_columns):
    if df.shape[1] < required_columns:
        print("Cannot Perform this yet")
        return False
    return True


# Function to save DataFrame to a CSV file
def save_df():
    df.to_csv("saved_df.csv", index=False)
    print("DataFrame saved to 'saved_df.csv'.")


# Function to read DataFrame from a CSV file
def read_df():
    try:
        # Read the CSV file into a DataFrame
        return pd.read_csv('saved_df.csv')
    except FileNotFoundError:
        print("No Saved DataFrame")
        return pd.DataFrame()


# Load or initialize the DataFrame
df = read_df()

# Create instances of classes for YouTube management, sentiment analysis, and displaying analysis
yt_manager = youtube_manager(API_KEY)
sent_analyser = sentiment_analysis()
displayer = analysis_displayer()

# Main loop for user interaction
while True:
    print(
        "Welcome to the project," +
        "\n0 - Quit" +
        "\n1 - Gather Comments" +
        "\n2 - Conduct Sentiment Analysis" +
        "\n3 - Display Analysis"
    )
    try:
        # Read the user's choice as an integer
        user_input = int(input("Enter Your Choice: "))

        # Gather Comments
        if user_input == 1:
            df = yt_manager.collect_comments()
            save_df()

        # Conduct Sentiment Analysis
        elif user_input == 2:
            if valid_df(required_columns=1):
                df = sent_analyser.analyse(df)
                save_df()

        # Display Analysis
        elif user_input == 3:
            if valid_df(required_columns=2):
                displayer.display(df)
                displayer.display_negative_graph(df)
                displayer.display_positive_graph(df)

        # Exit the console
        elif user_input == 0:
            print("Goodbye")
            break  # Exit the function and terminate the loop

        else:
            # User enters an integer that is not a valid option
            print("Invalid Input")

    except Exception as e:
        # Error handling when input is in an invalid format (not an integer)
        print(e)
