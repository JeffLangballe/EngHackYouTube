#!/usr/bin/env python3
"""
Uses YouTube API to fetch comments

Usage:
python youtube_comments.py <video_id>
"""

import sys
import requests
from api.keys import youtube_api_key


BASE_URL_COMMENTS = 'https://www.googleapis.com/youtube/v3/commentThreads'
BASE_URL_VIDEO_IDS = 'https://www.googleapis.com/youtube/v3/search'

def get_comments(video_id, page_token=None):
    """
    Returns tuple of the form (comments, next_page_token) for a video_id
    If the last page is reached, next_page_token is None
    """

    # Make API request and parse as JSON
    payload = {}
    payload['part'] = 'snippet'
    payload['textFormat'] = 'plainText'
    payload['videoId'] = video_id
    payload['key'] = youtube_api_key
    if page_token:
        payload['pageToken'] = page_token

    r = requests.get(BASE_URL_COMMENTS, params=payload)
    data = r.json()
    
    # Extract comment text
    comments = [
        item['snippet']['topLevelComment']['snippet']['textOriginal']
        for item in data['items']
        if item is not None
    ]

    # Get token for the next page
    next_page_token = None
    if 'nextPageToken' in data:
        next_page_token = data['nextPageToken']
        
    return comments, next_page_token

def get_video_ids(keyword, page_token=None):
    """
    Returns tuple of the form (comments, next_page_token) for a video_id
    If the last page is reached, next_page_token is None
    """

    # Make API request and parse as JSON
    payload = {}
    payload['part'] = 'snippet'
    payload['maxResults'] = 25
    payload['q'] = keyword
    payload['type'] = 'video'
    payload['key'] = youtube_api_key
    if page_token:
        payload['pageToken'] = page_token

    r = requests.get(BASE_URL_VIDEO_IDS, params=payload)
    data = r.json()
    
    # Extract videoids text
    videoIDs = [
        item['id']['videoId']
        for item in data['items']
        if item is not None
    ]
  
    return videoIDs

if __name__ == '__main__':
    commentAggregate = []
    video_id = sys.argv[1]
    comments, next_page = get_comments(video_id)
    print(comments)
    while next_page is not None and len(commentAggregate) < 100:
        comments, next_page = get_comments(video_id, next_page)
        commentAggregate = commentAggregate + comments
        print(comments)
    print len(commentAggregate) + 'comments collected' 

        
        
