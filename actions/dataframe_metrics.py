from textblob import TextBlob
import pandas as pd
from config.constants import continuous_columns, msteams_columns, discrete_columns, msteams_unique_columns
import numpy as np
from helper import removeDuplicates

# ---------------------- only for demo -----------------

# from demo.parser import parse
# data = parse()

# def getDataFrame():
#     df = pd.DataFrame(data, columns=discrete_columns)
#     return df

# ---------------------- only for demo -----------------

def getAugmentedDataFrame(df):
    df[continuous_columns[0]] = df[msteams_columns[3]].apply(lambda msg : len(msg.split(' ')))
    df[continuous_columns[1]] = df[msteams_columns[3]].apply(lambda msg : len(msg))

    # ------------- only for demo ----------------
    # df[continuous_columns[0]] = df[discrete_columns[1]].apply(lambda msg : len(msg.split(' ')))
    # df[continuous_columns[1]] = df[discrete_columns[1]].apply(lambda msg : len(msg))
    return df

def getWordCountByAuthor(augDF):
    # df = getAugmentedDataFrame()
    augDF = augDF[['Author', 'Word_Count']].groupby('Author').sum()
    return augDF.reset_index()

def getLetterCountByAuthor(augDF):
    # df = getAugmentedDataFrame()
    augDF = augDF[['Author', 'Letter_Count']].groupby('Author').sum()
    return augDF.reset_index()

def getRepliesPerUser(rootDF, replyDF):
    rootDF = removeDuplicates(rootDF[msteams_unique_columns])
    replyDF = removeDuplicates(replyDF[msteams_unique_columns])
    replyDF = replyDF.set_index('ReplyToID')
    joinedDF = pd.merge(rootDF, replyDF, left_on='ID', right_index=True)
    joinedDF.reset_index(drop=True, inplace=True)
    # print(joinedDF[['Author_x', 'Author_y']])
    return joinedDF

# Sentiment Calculation

def calculateSentimentPolarity(msg):
    analysis = TextBlob(msg)
    return round(analysis.sentiment.polarity, 2)    # rounding to 2 decimal places

def calculateDiscreetSentimentPolarity(msg):
    analysis = TextBlob(msg)
    if analysis.sentiment.polarity > 0.6:
        return 'very positive'
    elif 0.20 < analysis.sentiment.polarity <= 0.60:
        return 'positive'
    elif -0.20 <= analysis.sentiment.polarity <= 0.20:
        return 'neutral'
    elif -0.60 <= analysis.sentiment.polarity < -0.20:
        return 'negative'
    elif analysis.sentiment.polarity < -0.60:
        return 'very negative'

def augmentDataFrameWithDiscreetSentimentPolarity(augDF):
    # df = getAugmentedDataFrame()
    augDF['discreet-sentiment-polarity'] = augDF['Message'].apply(lambda msg: calculateDiscreetSentimentPolarity(msg))
    return augDF

def augmentDataFrameWithSentimentPolarity(augDF):
    # df = getAugmentedDataFrame()
    augDF['sentiment-polarity'] = augDF['Message'].apply(lambda msg: calculateSentimentPolarity(msg))
    return augDF

