import json
import requests
import config
URL="https://api.telegram.org/bot{}/".format(config.token)
def getJSON(url):
    response = requests.get(url)
    jsonData=json.loads(response.content.decode("utf-8"))
    return jsonData

def getUpdates(offset=None):
    url=URL+"getUpdates?timeout=100"
    if offset:
        url=URL+"getUpdates?offset={}".format(offset)
    jsonData=getJSON(url)
    return jsonData


def getLatestUpdateID(updates):
    ids =[]
    for update in updates["result"]:
        ids.append(int(update["update_id"]))
    return max(ids)


def replyToAll(updates):
    for update in updates["result"]:
            text=update["message"]["text"]
            chatID=update["message"]["chat"]["id"]
            sendMessage(text,chatID)


def sendMessage(text,chatID):
    url=URL+"sendMessage?chat_id={}&text={}".format(chatID,text)
    response=requests.get(url)


lastUpdateID=None
while True:
    updates=getUpdates(lastUpdateID)
    if len(updates["result"])>0:
        lastUpdateID=getLatestUpdateID(updates) + 1
        replyToAll(updates)  
