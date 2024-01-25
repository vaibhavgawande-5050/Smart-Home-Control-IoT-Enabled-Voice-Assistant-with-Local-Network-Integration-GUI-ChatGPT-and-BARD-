
from configuration import youtube_key
from googleapiclient.discovery import build
import webbrowser

def Youtube_call(query):


    # Replace with your API key
    key = youtube_key

    # Build the YouTube API service
    youtube = build('youtube', 'v3', developerKey=key)

    def play_youtube_video(query):
        """Searches for a YouTube video based on the query and opens it in the browser."""
        request = youtube.search().list(q=query, part='snippet', type='VIDEO')
        response = request.execute()

        try:
            video_id = response['items'][0]['id']['videoId']  # Get the first result's video ID
            # video_url = f"https://www.youtube.com/watch?v={video_id}"
            video_url = f"https://www.youtube.com/watch?v={video_id}&autoplay=1" ## &autoplay=1 for autoplay directly on browser

            webbrowser.open(video_url)  # Open the video in the browser
        except IndexError:
            print("No videos found for that query.")

    # Play the video
    play_youtube_video(query)