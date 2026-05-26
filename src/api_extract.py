from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

# Build YouTube API client
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

def get_channel_stats(channel_id):

    request = youtube.channels().list(
        part="snippet,statistics,contentDetails",
        id=channel_id
    )

    response = request.execute()

    data = []

    for item in response["items"]:

        stats = {
            "Channel_Name": item["snippet"]["title"],
            "Subscribers": item["statistics"].get("subscriberCount"),
            "Views": item["statistics"].get("viewCount"),
            "Total_Videos": item["statistics"].get("videoCount")
        }

        data.append(stats)

    return pd.DataFrame(data)

def get_video_details(video_ids):

    all_video_stats = []

    request = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    )

    response = request.execute()

    for video in response["items"]:

        stats = {
            "Title": video["snippet"]["title"],
            "Published_Date": video["snippet"]["publishedAt"],
            "Views": video["statistics"].get("viewCount", 0),
            "Likes": video["statistics"].get("likeCount", 0),
            "Comments": video["statistics"].get("commentCount", 0)
        }

        all_video_stats.append(stats)

    return pd.DataFrame(all_video_stats)

def get_uploads_playlist_id(channel_id):

    request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )

    response = request.execute()

    return response["items"][0]\
        ["contentDetails"]\
        ["relatedPlaylists"]\
        ["uploads"]

def get_video_ids(playlist_id):

    video_ids = []

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=playlist_id,
        maxResults=50
    )

    response = request.execute()

    for item in response["items"]:

        video_ids.append(
            item["contentDetails"]["videoId"]
        )

    return video_ids

def get_video_details(video_ids):

    import pandas as pd

    all_data = []

    request = youtube.videos().list(
        part="snippet,statistics",
        id=",".join(video_ids)
    )

    response = request.execute()

    for item in response["items"]:

        data = {
            "Title": item["snippet"]["title"],
            "Published_Date":
                item["snippet"]["publishedAt"],
            "Views":
                item["statistics"].get("viewCount", 0),
            "Likes":
                item["statistics"].get("likeCount", 0),
            "Comments":
                item["statistics"].get("commentCount", 0)
        }

        all_data.append(data)

    return pd.DataFrame(all_data)