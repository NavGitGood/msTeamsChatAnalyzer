from actions.plotter import userPlotter, groupPlotter
from actions.pdfmaker import add_image
# from config.constants import msteams_unique_columns
import sys
# from msteams.extract_to_df import getRootMessages, getReplies
from actions.dataframe_metrics import getAugmentedDataFrame #, getDataFrame
from actions.dataframe_filters import getUserMentions, getUsersWithReplies
# from helper import removeDuplicates
# import pandas as pd
from report_generator import generateGroupReport, generateIndividualReport

if __name__ == '__main__':
    # Map command line arguments to function arguments.

    # rootDF = getRootMessages(1,2)
    # replyDF = getReplies(list(removeDuplicates(rootDF[['ID']])['ID']))
    # rawAugDF = pd.concat([rootDF,replyDF])
   
    # uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    # uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    # df = pd.concat([uniqueRootDF,uniqueReplyDF])
    # augDF = getAugmentedDataFrame(df)
    # userPlotter(f'{sys.argv[1]} {sys.argv[2]}',augDF)
    # groupPlotter(augDF, rawAugDF, rootDF, replyDF)
    # add_image('output/ax1_figure.png', 'output/ax2_figure.png', 
    # 'output/ax3_figure.png', 'output/ax4_figure.png',
    # 'output/ax5_figure.png', 'output/ax6_figure.png'
    # )

    generateGroupReport()

    generateIndividualReport(f'{sys.argv[1]} {sys.argv[2]}')


# -------------------- only for demo --------------------

    # df = getDataFrame()
    # augDF = getAugmentedDataFrame(df)
    # print(augDF)

    # userPlotter(sys.argv[1],augDF)
    # groupPlotter(augDF)


