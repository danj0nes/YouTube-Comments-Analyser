import re  # regular expressions
import pandas as pd
from googleapiclient.discovery import build

# YouTube Data API v3 API Key
# Read the API key from key.txt
with open("key.txt", "r") as key_file:
    API_KEY = key_file.read().strip()

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)


# Function to extract video ID from URL
def extract_video_id(url):
    match = re.search(r"(?<=v=)[A-Za-z0-9_-]+", url)
    return match.group(0) if match else None


# Function to retrieve top 100 comments
def get_top_comments(video_id):
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

    return comments


def get_video_url():
    while True:
        # User input for YouTube video URL
        video_url = input("Enter the YouTube video URL: ")
        video_id = extract_video_id(video_url)

        if video_id:
            comments = get_top_comments(video_id)
            print(f"Retrieved {len(comments)} comments.")
            return comments
        else:
            print("Invalid YouTube video URL.")


comments = get_video_url()

# Create a Pandas DataFrame
df = pd.DataFrame(comments, columns=["Comment"])
df.to_csv("youtube_comments.csv", index=False)
print("Comments saved to 'youtube_comments.csv'.")
