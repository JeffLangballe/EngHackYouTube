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
examples = ["VADER is smart, handsome, and funny.",      # positive sentence example
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

    compound_score = 0

    #comments, next_id = youtube.get_comments(video_id)
    comments = [
        'Size doesn\'t matter',
        'What the fuck did you just fucking say about me you little bitch?',
        'delet this',
    ]
    for comment in comments:
        vs = analyzer.polarity_scores(comment)
        print("{:-<65} {}".format(comment, str(vs)))
        compound_score += vs['compound']

    compound_score /= len(comments)
    
    print('Average score')
    print(compound_score)