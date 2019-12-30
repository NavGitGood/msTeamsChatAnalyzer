from config.constants import colors, explosion
import random
import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def getColorPalette(size):
    random.shuffle(colors)
    return colors[:size]

def getColorMap(arr):
    color_dict = {}
    for i in range(len(arr)):
        color_dict[arr[i]] = colors[i]
    return color_dict

def getExplosionArray(size):
    return explosion[:size]

def removeDuplicatesFromLegend(ax):
    handles, labels = ax.get_legend_handles_labels()
    unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
    ax.legend(*zip(*unique))
