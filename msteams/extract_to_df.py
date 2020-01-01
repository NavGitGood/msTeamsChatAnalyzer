#GET https://graph.microsoft.com/beta/
# teams/303d2c1c-f1c5-40ce-b68e-544343d7f42b/
# channels/19:fec4b0f2825d4c8c82abc09027a64184@thread.skype/messages

#GET https://graph.microsoft.com/beta/
# teams/303d2c1c-f1c5-40ce-b68e-544343d7f42b/
# channels/19:fec4b0f2825d4c8c82abc09027a64184@thread.skype/
# messages/1555375673184/replies

import json
import pandas as pd
from helper import remove_tags
from config.constants import msteams_columns, msteams_unique_columns

def jsonParser(jsonList):
    username = []
    content = []
    id = []
    replyToId = []
    mentionedAuthor = []
    for jsonItem in jsonList:
        username.append(jsonItem['from']['user']['displayName'])
        content.append(jsonItem['body']['content'])
        replyToId.append(jsonItem['replyToId'])
        id.append(jsonItem['id'])
        if(jsonItem['mentions']):
            for mention in jsonItem['mentions']:
                mentionedAuthor.append(mention['mentioned']['user']['displayName'])
                username.append(jsonItem['from']['user']['displayName'])
                content.append(jsonItem['body']['content'])
                id.append(jsonItem['id'])
                replyToId.append(jsonItem['replyToId'])
            username.pop()
            content.pop()
            id.pop()
            replyToId.pop()
        else:
            mentionedAuthor.append('null')
    content = map(remove_tags, content)
    df = pd.DataFrame(list(zip(id, replyToId, username, content, mentionedAuthor)), 
               columns = msteams_columns)
    return df

def getRootMessages(teamid:None, channelid:None):
    file = './test_data/root-msgs.json'    # to be replaced with actual api call
    with open(file) as json_file:
        jsonData = json.load(json_file)
    jsonList = list(jsonData["value"])
    rootDF = jsonParser(jsonList)
    return rootDF

def getReplies(messageIds):
    dataList = []
    flatList = []
    for messageId in messageIds:
        if(messageId=='1548100551644'):
            continue
        else:
            file = f'./test_data/reply_{messageId}.json'  # to be replaced with actual api call and handle response with no replies
            with open(file) as json_file:
                jsonData = json.load(json_file)
            jsonList = list(jsonData["value"])
            dataList.append(jsonParser(jsonList).values.tolist())
    for itemList in dataList:
        for item in itemList:
            flatList.append(item)
    replyDF = pd.DataFrame(flatList, columns = msteams_columns)
    return replyDF