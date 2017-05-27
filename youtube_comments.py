#!/usr/bin/env python3
"""
Uses YouTube API to fetch comments
"""

import sys
import requests
from api.keys import youtube_api_key


BASE_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

def get_comments(video_id):
    """
    Returns list of comments for video_id
    Only returns first page. ie. first 20 comments
    TODO: Get all the comments and do stuff
    """

    # Make API request and parse as JSON
    payload = {}
    payload['part'] = 'snippet'
    payload['textFormat'] = 'plainText'
    payload['videoId'] = video_id
    payload['key'] = youtube_api_key

    r = requests.get(BASE_URL, params=payload)
    data = r.json()

    # Extract comment text
    comments = [
        item['snippet']['topLevelComment']['snippet']['textOriginal']
        for item in data['items']
        if item is not None
    ]

    return comments


if __name__ == '__main__':
    video_id = sys.argv[1]
    comments = get_comments(video_id)
    print(comments)
