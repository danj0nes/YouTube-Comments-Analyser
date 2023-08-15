import re  # regular expressions
import pandas as pd
from googleapiclient.discovery import build


class youtube_manager:
    def __init__(self, API_KEY):
        # Initialize the YouTube API client
        self.youtube = build("youtube", "v3", developerKey=API_KEY)

    def collect_comments(self):
        id = get_video_id()
        comments = get_top_comments(self.youtube, id)

        # Create a Pandas DataFrame
        df = pd.DataFrame(comments, columns=["Comment"])
        return df

    def save_comments(self, df):
        df.to_csv("youtube_comments.csv", index=False)
        print("Comments saved to 'youtube_comments.csv'.")


# Function to retrieve top 100 comments
def get_top_comments(youtube, video_id):
    comments = []
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        order="relevance",  # You can change the sorting order if needed
        maxResults=100
    ).execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(comment)

    print(f"Retrieved {len(comments)} comments.")
    return comments


# Function to extract video ID from URL
def extract_video_id(url):
    match = re.search(r"(?<=v=)[A-Za-z0-9_-]+", url)
    return match.group(0) if match else None


def get_video_id():
    while True:
        # User input for YouTube video URL
        video_url = input("Enter the YouTube video URL: ")
        video_id = extract_video_id(video_url)

        if video_id:
            return video_id
        else:
            print("Invalid YouTube video URL.")
