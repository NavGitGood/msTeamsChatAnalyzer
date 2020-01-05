import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib.gridspec
import pandas as pd
import numpy as np
from config.constants import authors_by_letters, authors_by_words
from .dataframe_filters import messageCountByAuthor, wordCountByAuthor, letterCountByAuthor, sentimentPolarityCountByAuthor, discreetSentimentForIndividual, getUserMentions, getUsersWithReplies, getRepliesToUser, getRepliesByUser
from helper import getColorPalette, getExplosionArray, getColorMap, removeDuplicatesFromLegend

def userPlotter(username, augDF, rootDF=None, replyDF=None):
    # --------------------- to use rootDF and replyDF only as parameters --------------------
    # rawAugDF = pd.concat([rootDF,replyDF])
    # uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    # uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    # df = pd.concat([uniqueRootDF,uniqueReplyDF])
    # augDF = getAugmentedDataFrame(df)

    # fig = plt.figure(figsize=(15,15))
    # ax = fig.add_subplot()

    file_list = []
    table_data = []

    gs = matplotlib.gridspec.GridSpec(8, 2,  width_ratios=[1,1])
    fig = plt.figure(figsize=(15,15))
    ax1 = fig.add_subplot(gs[1:4,:])
    df = discreetSentimentForIndividual(username, augDF)
    if (df.empty):
        file_list.append('test_data/default.png')
    else:
        author_value_counts = df['discreet-sentiment-polarity'].value_counts()
        author_value_counts.plot(kind='bar', stacked=True, ax=ax1, color=getColorPalette(5))
        plt.xlabel('Sentiment Polarity', fontsize=15, fontweight='black', color = '#333F4B')
        plt.ylabel('Number of Messages', fontsize=15, fontweight='black', color = '#333F4B')
        plt.title('Distribution of Sentiment Polarity', fontsize=15, fontweight='black', color = '#333F4B')
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'Helvetica'
        plt.rcParams['axes.edgecolor']='#333F4B'
        plt.rcParams['axes.linewidth']=0.8
        plt.rcParams['xtick.color']='#333F4B'
        plt.rcParams['ytick.color']='#333F4B'
        ax1.spines['top'].set_color('none')
        ax1.spines['right'].set_color('none')
        ax1.spines['left'].set_smart_bounds(True)
        ax1.spines['bottom'].set_smart_bounds(True)
        extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/user_figure_1.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/user_figure_1.png')
    fig.delaxes(ax1)


    ax1 = fig.add_subplot(gs[1:4,:])
    ax1.axis('equal')
    ax1.set_title('Distribution of replies received from Users',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df1 = getRepliesToUser(rootDF, replyDF, username)
    if (df1.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(df1.index)
        df1.plot.pie(ax=ax1, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
        startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
        textprops={'fontsize': 22})
        extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/user_figure_2.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/user_figure_2.png')
    fig.delaxes(ax1)


    ax1 = fig.add_subplot(gs[1:4,:])
    ax1.axis('equal')
    ax1.set_title('Distribution of replies sent to Users',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df1 = getRepliesByUser(rootDF, replyDF, username)
    if (df1.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(df1.index)
        df1.plot.pie(ax=ax1, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
        startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
        textprops={'fontsize': 22})
        extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/user_figure_3.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/user_figure_3.png')
    fig.delaxes(ax1)
    
    message_count_df = messageCountByAuthor(augDF)
    message_count_df = message_count_df.reset_index()
    message_count_df.columns = ['Author', 'MessageCount']
    word_count_df = wordCountByAuthor(augDF)
    letter_count_df = letterCountByAuthor(augDF)
    return file_list, message_count_df, word_count_df, letter_count_df

    # plt.show()

def groupPlotter(augDF, rawAugDF, rootDF=None, replyDF=None): 
    # --------------------- to use rootDF and replyDF only as parameters --------------------
    # rawAugDF = pd.concat([rootDF,replyDF])
    # uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    # uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    # df = pd.concat([uniqueRootDF,uniqueReplyDF])
    # augDF = getAugmentedDataFrame(df)
    file_list = []
    gs = matplotlib.gridspec.GridSpec(8, 2,  width_ratios=[1,1]) #, height_ratios=[1,1,1,1,1,1]
    fig = plt.figure(figsize=(15,15))
    ax1 = fig.add_subplot(gs[1:4,:])
    ax1.axis('equal')
    ax1.set_title('Message Distribution By Author',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    message_count_df = messageCountByAuthor(augDF)
    if (message_count_df.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(message_count_df.index)
        message_count_df.plot.pie(ax=ax1, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
        startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
        textprops={'fontsize': 22})
        extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_1.png', bbox_inches=extent.expanded(1.0,3.0))
        file_list.append('output/group_figure_1.png')
        message_count_df = message_count_df.reset_index()
        message_count_df.columns = ['Author', 'MessageCount']
    fig.delaxes(ax1)

    ax2 = fig.add_subplot(gs[1:4,:])
    ax2.axis('equal')
    ax2.set_title('Word Count Distribution By Author',
        {'fontsize': 25,
        'fontweight' : 'black',
        'verticalalignment': 'baseline'},
        loc="center", pad=150,
        )
    word_count_df = wordCountByAuthor(augDF)
    if (word_count_df.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(word_count_df.index)
        word_count_df['Word_Count'].groupby(word_count_df['Author']).sum().plot.pie(ax=ax2, colors = getColorPalette(dfLen),
        explode=getExplosionArray(dfLen), shadow=True, startangle=90, autopct='%1.1f%%', pctdistance=0.5,
        radius=2,
        textprops={'fontsize': 22})
        extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_2.png', bbox_inches=extent.expanded(1.0,3.0))
        file_list.append('output/group_figure_2.png')
    fig.delaxes(ax2)

    ax3 = fig.add_subplot(gs[1:4,:])
    ax3.axis('equal')
    ax3.set_title('Letter Count Distribution By Author',
        {'fontsize': 25,
        'fontweight' : 'black',
        'verticalalignment': 'baseline'},
        loc="center", pad=150,
        )
    letter_count_df = letterCountByAuthor(augDF)
    if (letter_count_df.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(letter_count_df.index)
        letter_count_df['Letter_Count'].groupby(letter_count_df['Author']).sum().plot.pie(ax=ax3, colors = getColorPalette(dfLen),
        explode=getExplosionArray(dfLen), shadow=True, startangle=90, autopct='%1.1f%%', pctdistance=0.5,
        radius=2,
        textprops={'fontsize': 22})
        extent = ax3.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_3.png', bbox_inches=extent.expanded(1.0,3.0))
        file_list.append('output/group_figure_3.png')
    fig.delaxes(ax3)


    ax4 = fig.add_subplot(gs[1:4,:])
    ax4.set_title('Message Distribution By Sentiment Polarity',
        {'fontsize': 25,
        'fontweight' : 'black',
        'verticalalignment': 'baseline'},
        loc="center", pad=70)
    ax4.set_xlabel('Sentiment Polarity',
        {'fontsize': 12,
        'fontweight' : 'black',
        'verticalalignment': 'baseline'}, labelpad=25)
    ax4.set_ylabel('Message Count',
        {'fontsize': 12,
        'fontweight' : 'black',
        'verticalalignment': 'baseline'}, labelpad=15)
    df4 = sentimentPolarityCountByAuthor(augDF)
    if (df4.empty):
        file_list.append('test_data/default.png')
    else:
        color_map = getColorMap(df4['Author'].unique())
        for i, r in df4.iterrows():
            ax4.plot(r['sentiment-polarity'], r['Message'], 'o', markersize=5, c=color_map[r['Author']], label=r['Author'])
        removeDuplicatesFromLegend(ax4)
        ax4.set_xlim([-1, 1])
        extent = ax4.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_4.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/group_figure_4.png')
    fig.delaxes(ax4)

    ax5 = fig.add_subplot(gs[1:4,:])
    ax5.axis('equal')
    ax5.set_title('User Mentions',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df5 = getUserMentions(rawAugDF)
    if (df5.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(df5.index)
        df5.plot.pie(ax=ax5, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
        startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
        textprops={'fontsize': 22})
        extent = ax5.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_5.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/group_figure_5.png')
    fig.delaxes(ax5)


    ax6 = fig.add_subplot(gs[1:4,:])
    ax6.axis('equal')
    ax6.set_title('Replies To User',    # replies received by user
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df6 = getUsersWithReplies(rootDF, replyDF)
    if (df6.empty):
        file_list.append('test_data/default.png')
    else:
        dfLen = len(df6.index)
        df6.plot.pie(ax=ax6, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
        startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
        textprops={'fontsize': 22})
        extent = ax6.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('output/group_figure_6.png', bbox_inches=extent.expanded(1.15,3.0))
        file_list.append('output/group_figure_6.png')
    fig.delaxes(ax6)

    plt.tight_layout()
    # plt.show()
    return file_list, message_count_df, word_count_df, letter_count_df

def getFrequencyOfWordCount(df, num):
    plt.figure(figsize=(15, 2))
    word_count_value_counts = df['Word_Count'].value_counts()
    top_n_word_count_value_counts = word_count_value_counts.head(num)
    top_n_word_count_value_counts.plot.bar()
    plt.xlabel('Word Count')
    plt.ylabel('Frequency')
    plt.show()

def getFrequencyOfLetterCount(df, num):
    plt.figure(figsize=(15, 2))
    letter_count_value_counts = df['Letter_Count'].value_counts()
    top_n_word_count_value_counts = letter_count_value_counts.head(num)
    top_n_word_count_value_counts.plot.bar()
    plt.xlabel('Letter Count')
    plt.ylabel('Frequency')
    plt.show()