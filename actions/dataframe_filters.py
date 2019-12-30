from .dataframe_metrics import getAugmentedDataFrame, getWordCountByAuthor, getLetterCountByAuthor, augmentDataFrameWithSentimentPolarity, augmentDataFrameWithDiscreetSentimentPolarity
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from helper import getColorMap

def messageCountByAuthor(augDF, num=None):
    df = getAugmentedDataFrame(augDF)
    author_value_counts = df['Author'].value_counts()
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