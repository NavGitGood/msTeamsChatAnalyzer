from actions.plotter import userPlotter, groupPlotter
from actions.pdfmaker import add_image
# from config.constants import msteams_unique_columns
import sys
# import readline
import shlex
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

    print('Enter a command to do something, e.g. `group` for generating group report or `individual firstname lastname` for generating individual report for a user.')

    while True:
        cmd, *args = shlex.split(input('> '))

        if cmd=='exit':
            break

        elif cmd.lower()=='group':
            print('Generating Goup Report')
            print('...')
            generateGroupReport()
            print('... done')

        elif cmd.lower()=='individual':
            firstname, lastname = args
            print(f'Generating Report for {firstname} {lastname}')
            print('...')
            generateIndividualReport(f'{firstname} {lastname}')
            print('... done')

        else:
            print('Unknown command: {}'.format(cmd))


# -------------------- only for demo --------------------

    # df = getDataFrame()
    # augDF = getAugmentedDataFrame(df)
    # print(augDF)

    # userPlotter(sys.argv[1],augDF)
    # groupPlotter(augDF)


