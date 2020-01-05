from .dataframe_metrics import getAugmentedDataFrame, getWordCountByAuthor, getLetterCountByAuthor, augmentDataFrameWithSentimentPolarity, augmentDataFrameWithDiscreetSentimentPolarity, getRepliesPerUser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper import getColorMap

def messageCountByAuthor(df, num=None):
    augDF = getAugmentedDataFrame(df)
    author_value_counts = augDF['Author'].value_counts()
    return author_value_counts.head(num)

def wordCountByAuthor(augDF, num=None):
    wordCountByAuthorDF = getWordCountByAuthor(augDF)
    wordCountGroupedByAuthor = wordCountByAuthorDF.sort_values('Word_Count', ascending=False)
    return wordCountGroupedByAuthor.head(num)

def letterCountByAuthor(augDF, num=None):
    letterCountByAuthorDF = getLetterCountByAuthor(augDF)
    letterCountGroupedByAuthor = letterCountByAuthorDF.sort_values('Letter_Count', ascending=False)
    return letterCountGroupedByAuthor.head(num)

def sentimentPolarityCountByAuthor(augDF):
    df = augmentDataFrameWithSentimentPolarity(augDF)
    df = df.groupby(['Author', 'sentiment-polarity'])['Message'].count()
    return pd.DataFrame(df, dtype=np.int8).reset_index()

def discreetSentimentForIndividual(author_name, augDF):
    df = augmentDataFrameWithDiscreetSentimentPolarity(augDF)
    return df.loc[df['Author'] == author_name]

# group, users which were mentioned
def getUserMentions(mergedDF):
    mergedDF.reset_index(drop=True, inplace=True)
    rowsToRemove = mergedDF[mergedDF['Mentioned'].apply(lambda x: x.startswith('null'))].index
    mergedDF = mergedDF.drop(rowsToRemove)
    userMentionsDF = mergedDF['Mentioned'].value_counts()
    return userMentionsDF

# group, users receiving replies
def getUsersWithReplies(rootDF, replyDF):
    joinedDF = getRepliesPerUser(rootDF, replyDF)
    joinedDF = joinedDF['Author_x'].value_counts()
    return joinedDF

# individual
def getRepliesToUser(rootDF, replyDF, author_name):
    joinedDF = getRepliesPerUser(rootDF, replyDF)
    joinedDF = joinedDF.loc[joinedDF['Author_x'] == author_name]
    joinedDF = joinedDF['Author_y'].value_counts()
    return joinedDF

# individual
def getRepliesByUser(rootDF, replyDF, author_name):
    joinedDF = getRepliesPerUser(rootDF, replyDF)
    joinedDF = joinedDF.loc[joinedDF['Author_y'] == author_name]
    joinedDF = joinedDF['Author_x'].value_counts()
    return joinedDF