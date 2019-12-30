from actions.plotter import userPlotter, groupPlotter
from actions.pdfmaker import add_image
from config.constants import msteams_unique_columns
import sys
from msteams.extract_to_df import getRootMessages, getReplies, removeDuplicates
from actions.dataframe_metrics import getAugmentedDataFrame #, getDataFrame
import pandas as pd

if __name__ == '__main__':
    # Map command line arguments to function arguments.

    rootDF = getRootMessages(1,2)
    replyDF = getReplies(list(removeDuplicates(rootDF[['ID']])['ID']))

    uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    df = pd.concat([uniqueRootDF,uniqueReplyDF])
    augDF = getAugmentedDataFrame(df)
    userPlotter(f'{sys.argv[1]} {sys.argv[2]}',augDF)
    groupPlotter(augDF)

# -------------------- only for demo --------------------

    # df = getDataFrame()
    # augDF = getAugmentedDataFrame(df)
    # print(augDF)

    # userPlotter(sys.argv[1],augDF)
    # groupPlotter(augDF)

# add_image('ax1_figure.png', 'ax2_figure.png', 'ax3_figure.png', 'ax4_figure.png')

# groupPlotter()
# add_image('ax1_figure.png', 'ax2_figure.png', 'ax3_figure.png', 'ax4_figure.png')


