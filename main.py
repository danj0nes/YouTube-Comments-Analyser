import pandas as pd
from youtube_manager import youtube_manager
from analysis import sentiment_analysis
from analysis import analysis_displayer

# YouTube Data API v3 API Key
# Read the API key from key.txt
with open("key.txt", "r") as key_file:
    API_KEY = key_file.read().strip()


def valid_df(required_columns):
    if (df.shape[1] < required_columns):
        print("Cannot Perform this yet")
        return False
    return True


def save_df():
    df.to_csv("saved_df.csv", index=False)
    print("DataFrame saved to 'saved_df.csv'.")


def read_df():
    try:
        # Read the CSV file into a DataFrame
        return pd.read_csv('saved_df.csv')
    except FileNotFoundError:
        print("No Saved DataFrame")
        return pd.DataFrame()


df = read_df()
yt_manager = youtube_manager(API_KEY)
sent_analyser = sentiment_analysis()
displayer = analysis_displayer()

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
            if (valid_df(required_columns=1)):
                df = sent_analyser.analyse(df)
                save_df()
        # Display Analysis
        elif user_input == 3:
            if (valid_df(required_columns=2)):
                displayer.display()
         # Exit the console
        elif user_input == 0:
            print("Goodbye")
            break  # Exit the function and terminate the loop
        else:
            # User enters an integer that is not a valid option
            print("Invalid Input")
    except ValueError:
        # Error handling when input is in an invalid format (not an integer)
        print("Invalid Input")
