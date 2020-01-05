from actions.plotter import userPlotter, groupPlotter
from actions.pdfmaker import new_pdf
from msteams.extract_to_df import getRootMessages, getReplies
from helper import removeDuplicates
from config.constants import msteams_unique_columns
from actions.dataframe_metrics import getAugmentedDataFrame
import pandas as pd

def generateGroupReport():
    rootDF = getRootMessages(1,2)
    replyDF = getReplies(list(removeDuplicates(rootDF[['ID']])['ID']))
    rawAugDF = pd.concat([rootDF,replyDF])
    uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    df = pd.concat([uniqueRootDF,uniqueReplyDF])
    augDF = getAugmentedDataFrame(df)
    file_list, message_count_df, word_count_df, letter_count_df = groupPlotter(augDF, rawAugDF, rootDF, replyDF)
    message_count_list = message_count_df.values.tolist()
    word_count_list = word_count_df.values.tolist()
    letter_count_list = letter_count_df.values.tolist()
    summary_data = [
        [message_count_list, 'Author', 'Message Count', 'Count of messages by each user'],
        [word_count_list, 'Author', 'Word Count', 'Count of words by each user'],
        [letter_count_list, 'Author', 'Letter Count', 'Count of letters by each user']
    ]
    new_pdf(file_list, 'Group_Report', table_data=summary_data)

def generateIndividualReport(user_name):
    rootDF = getRootMessages(1,2)
    replyDF = getReplies(list(removeDuplicates(rootDF[['ID']])['ID']))
    uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    df = pd.concat([uniqueRootDF,uniqueReplyDF])
    augDF = getAugmentedDataFrame(df)
    file_list, message_count_df, word_count_df, letter_count_df = userPlotter(user_name, augDF, rootDF, replyDF)
    message_count_df = message_count_df.loc[message_count_df['Author'] == user_name]
    word_count_df = word_count_df.loc[word_count_df['Author'] == user_name]
    letter_count_df = letter_count_df.loc[letter_count_df['Author'] == user_name]
    message_count_list = message_count_df.values.tolist()
    word_count_list = word_count_df.values.tolist()
    letter_count_list = letter_count_df.values.tolist()
    line_data_list = [
        ['Number of messages sent by you: ', message_count_list],
        ['Number of words used by you: ', word_count_list],
        ['Number of letters used by you: ', letter_count_list],
    ]
    new_pdf(file_list, user_name, line_data=line_data_list)
    