#!/usr/bin/env python3
"""
Extracts meaning from text using sentiment analysis
"""

import youtube
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

# --- examples -------
sentences = ["VADER is smart, handsome, and funny.",      # positive sentence example
            "VADER is not smart, handsome, nor funny.",   # negation sentence example
            "VADER is smart, handsome, and funny!",       # punctuation emphasis handled correctly (sentiment intensity adjusted)
            "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
            "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
            "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
            "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!",# booster words & punctuation make this close to ceiling for score
            "The book was good.",                                     # positive sentence
            "The book was kind of good.",                 # qualified positive sentence is handled correctly (intensity adjusted)
            "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
            "At least it isn't a horrible book.",         # negated negative sentence with contraction
            "Make sure you :) or :D today!",              # emoticons handled
            "Today SUX!",                                 # negative slang with capitalization emphasis
            "Today only kinda sux! But I'll get by, lol"  # mixed sentiment example with slang and constrastive conjunction "but"
             ]

if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()
    video_id = sys.argv[1]

    scores = {}
    scores['neg'] = 0
    scores['neu'] = 0
    scores['pos'] = 0
    scores['compound'] = 0

    comments, next_id = youtube.get_comments(video_id)
    for comment in comments:
        vs = analyzer.polarity_scores(comment)
        print("{:-<65} {}".format(comment, str(vs)))
        scores['neg'] += vs['neg']
        scores['neu'] += vs['neu']
        scores['pos'] += vs['pos']
        scores['compound'] += vs['compound']

    print('Total values')
    print(str(scores))

    scores['neg'] /= len(comments)
    scores['neu'] /= len(comments)
    scores['pos'] /= len(comments)
    scores['compound'] /= len(comments)
    
    print('Average values')
    print(str(scores))