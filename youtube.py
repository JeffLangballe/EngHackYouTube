#!/usr/bin/env python3
"""
Uses YouTube API to fetch comments

Usage:
python youtube_comments.py <video_id>
"""

import sys
import requests
from api.keys import youtube_api_key
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


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
    
    if 'items' not in data:
        return [], None

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
    payload['maxResults'] = 20
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


def comment_collector(video_id):
    commentAggregate = []
    comments, next_page = get_comments(video_id)
    while next_page is not None and len(commentAggregate) < 100:
        comments, next_page = get_comments(video_id, next_page)
        commentAggregate = commentAggregate + comments
    return commentAggregate

def score_calculator(keyword):
    analyzer = SentimentIntensityAnalyzer()
    totalScore=0
    compound_score = 0
    idList = get_video_ids(keyword)
    print(idList)
    numIDs = len(idList)
    print(numIDs)
    for vidID in idList:
        comments = comment_collector(vidID)
       # print(comments)
        for comment in comments:
            if comment is not None:
                vs = analyzer.polarity_scores(comment)
                #print("{:-<65} {}".format(comment, str(vs)))
                compound_score += vs['compound']
        try:
            compound_score /= len(comments)
        except ZeroDivisionError:
            compount_score = compound_score
        totalScore += compound_score
            
    totalScore /= (numIDs * 1.0)
    print('Average score')
    print(totalScore)
    return totalScore

if __name__ == '__main__':
    keyword = sys.argv[1]
    score_calculator(keyword)
    


        
        
