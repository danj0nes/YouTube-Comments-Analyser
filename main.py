import pandas as pd
from youtube_manager import youtube_manager
from analysis import sentiment_analysis

# YouTube Data API v3 API Key
# Read the API key from key.txt
with open("key.txt", "r") as key_file:
    API_KEY = key_file.read().strip()

global df

while True:
    print(
        "Welcome to the project," +
        "\n0 - Quit" +
        "\n1 - Gather Comments" +
        "\n1 - Analyse Comments"
    )
    try:
        # Read the user's choice as an integer
        user_input = int(input("Enter Your Choice: "))

        # Gather Comments
        if user_input == 1:
            yt_manager = youtube_manager(API_KEY)
            df = yt_manager.collect()
            yt_manager.save_comments(df)
        # Analyse Comments
        elif user_input == 2:
            if not df:
                try:
                    # Read the CSV file into a DataFrame
                    df = pd.read_csv('youtube_comments.csv')
                except FileNotFoundError:
                    print("Gather Comments First")
                    continue

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
