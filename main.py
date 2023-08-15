import pandas as pd
from youtube_manager import youtube_manager
from analysis import sentiment_analysis
from analysis import analysis_displayer

# YouTube Data API v3 API Key
# Read the API key from key.txt
with open("key.txt", "r") as key_file:
    API_KEY = key_file.read().strip()

global df


def is_df():
    if not df:
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv('saved_df.csv')
        except FileNotFoundError:
            print("Gather Comments First")
            return False
    return True


def save_df():
    df.to_csv("saved_df.csv", index=False)
    print("Comments saved to 'saved_df.csv'.")


def df_analysed():
    if ("Sentiment" in df.columns):
        return True
    else:
        print("Conduct Sentiment Analysis First")
        return False


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
            yt_manager = youtube_manager(API_KEY)
            df = yt_manager.collect_comments()
            save_df()
        # Conduct Sentiment Analysis
        elif user_input == 2:
            if (is_df()):
                sent_analyser = sentiment_analysis()
                df = sent_analyser.analyse(df)
                save_df()
        # Display Analysis
        elif user_input == 3:
            if (is_df() and df_analysed()):
                displayer = analysis_displayer()
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
