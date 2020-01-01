import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import matplotlib.gridspec
import pandas as pd
import numpy as np
from config.constants import authors_by_letters, authors_by_words
from .dataframe_filters import messageCountByAuthor, wordCountByAuthor, letterCountByAuthor, sentimentPolarityCountByAuthor, discreetSentimentForIndividual, getUserMentions, getUsersWithReplies
from helper import getColorPalette, getExplosionArray, getColorMap, removeDuplicatesFromLegend

def userPlotter(username, augDF):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot()
    df = discreetSentimentForIndividual(username, augDF)
    author_value_counts = df['discreet-sentiment-polarity'].value_counts()
    author_value_counts.plot(kind='bar', stacked=True, ax=ax, color=getColorPalette(5))
    plt.xlabel('Sentiment Polarity', fontsize=15, fontweight='black', color = '#333F4B')
    plt.ylabel('Number of Messages', fontsize=15, fontweight='black', color = '#333F4B')
    plt.title('Distribution of Sentiment Polarity', fontsize=15, fontweight='black', color = '#333F4B')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax_figure.png', bbox_inches=extent.expanded(1.5,1.5))
    # plt.show()

def groupPlotter(augDF, rawAugDF, rootDF=None, replyDF=None): 
    # --------------------- to use rootDF and replyDF only as parameters --------------------
    # rawAugDF = pd.concat([rootDF,replyDF])
    # uniqueRootDF = removeDuplicates(rootDF[msteams_unique_columns])
    # uniqueReplyDF = removeDuplicates(replyDF[msteams_unique_columns])
    # df = pd.concat([uniqueRootDF,uniqueReplyDF])
    # augDF = getAugmentedDataFrame(df)

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
    df1 = messageCountByAuthor(augDF, 5)
    df1.plot.pie(ax=ax1, colors = getColorPalette(5), explode=getExplosionArray(5), shadow=True, 
    startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
    textprops={'fontsize': 22})
    extent = ax1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax1_figure.png', bbox_inches=extent.expanded(1.0,3.0))
    fig.delaxes(ax1)


    df2 = wordCountByAuthor(augDF, 5)
    ax2 = fig.add_subplot(gs[1:4,:])
    ax2.axis('equal')
    ax2.set_title('Word Count Distribution By Author',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df2['Word_Count'].groupby(df2['Author']).sum().plot.pie(ax=ax2, colors = getColorPalette(5),
    explode=getExplosionArray(5), shadow=True, startangle=90, autopct='%1.1f%%', pctdistance=0.5,
    radius=2,
    textprops={'fontsize': 22})
    extent = ax2.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax2_figure.png', bbox_inches=extent.expanded(1.0,3.0))
    fig.delaxes(ax2)


    df3 = letterCountByAuthor(augDF, 5)
    ax3 = fig.add_subplot(gs[1:4,:])
    ax3.axis('equal')
    ax3.set_title('Letter Count Distribution By Author',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df3['Letter_Count'].groupby(df3['Author']).sum().plot.pie(ax=ax3, colors = getColorPalette(5),
    explode=getExplosionArray(5), shadow=True, startangle=90, autopct='%1.1f%%', pctdistance=0.5,
    radius=2,
    textprops={'fontsize': 22})
    extent = ax3.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax3_figure.png', bbox_inches=extent.expanded(1.0,3.0))
    fig.delaxes(ax3)


    df4 = sentimentPolarityCountByAuthor(augDF)
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
    color_map = getColorMap(df4['Author'].unique())
    for i, r in df4.iterrows():
        ax4.plot(r['sentiment-polarity'], r['Message'], 'o', markersize=5, c=color_map[r['Author']], label=r['Author'])
    removeDuplicatesFromLegend(ax4)
    ax4.set_xlim([-1, 1])
    extent = ax4.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax4_figure.png', bbox_inches=extent.expanded(1.15,3.0))
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
    dfLen = len(df5.index)
    df5.plot.pie(ax=ax5, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
    startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
    textprops={'fontsize': 22})
    extent = ax5.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax5_figure.png', bbox_inches=extent.expanded(1.15,3.0))
    fig.delaxes(ax5)


    ax6 = fig.add_subplot(gs[1:4,:])
    ax6.axis('equal')
    ax6.set_title('Replies To User',
    {'fontsize': 25,
    'fontweight' : 'black',
    'verticalalignment': 'baseline'},
    loc="center", pad=150,
    )
    df6 = getUsersWithReplies(rootDF, replyDF)
    dfLen = len(df6.index)
    df6.plot.pie(ax=ax6, colors = getColorPalette(dfLen), explode=getExplosionArray(dfLen), shadow=True, 
    startangle=90, autopct='%1.1f%%', pctdistance=0.5, radius=2, 
    textprops={'fontsize': 22})
    extent = ax6.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig.savefig('output/ax6_figure.png', bbox_inches=extent.expanded(1.15,3.0))
    fig.delaxes(ax6)


    plt.tight_layout()
    # plt.show()

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