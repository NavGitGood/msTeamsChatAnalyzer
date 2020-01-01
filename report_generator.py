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
    groupPlotter(augDF, rawAugDF, rootDF, replyDF)
    new_pdf(['output/ax1_figure.png', 'output/ax2_figure.png', 
    'output/ax3_figure.png', 'output/ax4_figure.png',
    'output/ax5_figure.png', 'output/ax6_figure.png'],
    'Group_Report'
    )

def generateIndividualReport(user_name):
    rootDF = getRootMessages(1,2)
    replyDF = getReplies(list(removeDuplicates(rootDF[['ID']])['ID']))
    uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    df = pd.concat([uniqueRootDF,uniqueReplyDF])
    augDF = getAugmentedDataFrame(df)
    userPlotter(user_name, augDF)
    new_pdf(['output/ax_figure.png'], user_name)
    