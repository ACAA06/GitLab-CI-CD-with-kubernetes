import json
import requests
import random
import os


URL="https://api.telegram.org/bot{}/".format("$token")
commands=["/Cq","/cq","/geek","/Geek","/ps","/Ps"]
n="clement"
def namefor(na):
    global n
    n=na

def sendImage(chat_id,what):
    url = "https://api.telegram.org/$token";
    files = {'photo': open(os.path.abspath(what), 'rb')}
    data = {'chat_id' : chat_id}
    r= requests.post(url, files=files, data=data)
    print(r.status_code, r.reason, r.content)

def sendMessagefake(text,chatID):
    url=URL+"sendMessage?chat_id={}&text={}".format(chatID,text)
    response=requests.get(url)
    return "done"

def sendMessage(text,chatID):
    url=URL+"sendMessage?chat_id={}&text={}".format(chatID,text)
    response=requests.get(url)


def geek():
    r=requests.get('https://geek-jokes.sameerkumar.website/api')
    k=0
    try:
        data=json.loads(r.content)
        k=1
    except:
        pass
    if k==1:
        sendMessagefake(n+" geek",400457856)
        return data
    else:
        return "Error!Not found!! :("
  




def Clem(fname,who):
    #s="Thank you❤️"+"\n"
    #s+="I was startled by the spark from your eyes...The heat I felt is from the heart , caused by the rapid flow of 'love' electrons in my body.\n\n"+"If I see u without a smile.I give u mine.\n\n"+"You are the clock in my timeline.... always ticking my heart💓✌️\n\n"+"The hardest feeling is that knowing , u love someone else.\n\n"+"When I have so much to whisper in your ears,but I couldn't as you are not mine. I keep talking to myself and burning in hell,but all I show you is a smiling face.🙂✌️\n\n"+"I look at many, but I gaze at just u... 😉✌️\n\n"+"Nobody knew , for , I never said it. But somehow, I expected u to see it. It was too late,when u actually realized it.I was still there,but, you were someone else's.😔✌️\n\n"+"I am following you like a parallel line, hopefully joining with u at infinity (love)😉✌️❣️\n\n"+"I hope I remember to tell you I LOVE YOU ❣️every single day\n\n"+"Dear C,Stop being emotional and caring. Stop hating yourself for every damn thing. Control the things u can and let go little. U cant make everyone happy. Now its time for u to change and get your rythm back. Never ever loose hope.\nWith love,The one who is eager to see the old you.\n\n"+"You are my most beautiful chaos.❣️\n\n"+"The most horrible feeling is when u have infinite possibilities of filling the void in you but still you can't take your chances.\n\n"+"Out of the available love equations, create a new love Formula for your loved one.❣️\n\n"+"He was never too loud or outspoken, whenever he talked to her, he would metamorphosize into a completely different person.\n\n"+"The worst thing in life is not losing the one u love, it's losing yourself in the process of loving too much.\n\n"+"You are in mad love, when u realise there are many people to hear your problems out,but your heart wants only that person to help you (which they don't do).\n\n"+"I can survive the cold weather even when you are not beside me by seeing you happy at a distance far away which provides me the warmth.\n\n"+"In case you love someone and they don't value you and when they avoid you or when they don't care about you,You'll feel sad,but you won't understand why are you sad. It's all just because of LOVE.\n\n"+"She is perfectly childish for fun conversations and on point mature for my emotional side.\n\n"+"I'd like for you to tell me.  Should I love or not?\n\n"+"I'm struck in a love desert longing for your love which seems to be a mirage, but still hopeful.\n\n"+"Ignoring is the best way to pretend you're not affected by things that hurt  you secretly.\n\n"+"I just can't forget our conversations lasting for hours...but now I don't even receive a message from you...which kills me like a slow poison...but I'm still waiting for your message and call... Just to hear that special ringtone...I will be waiting for you till the end of my life.Just for you.❣️\n\n"+"The people who are alone suffer from lack of care and love. As time pass by they are used to it and they become stronger with handling emotions. They never failed to give other people the care they were longing for. So don't worry that you have none to share your feelings, you have the strongest wings to fly, just be strong and face it with confidence 👊.\n\n"+"Relationship status :Committed with her memories💔\n\n"+"No Matter how many failures you face,  Believe that you will be fine, some-'one' good in the future , you will be fine 👍.\n\n"+"Nobody gets everything they want. There will always be something. New problems arise. Instead of striving for perfection, strive for contentedness ✨.\n\n"+"In this battle world everyone have their chance of either being a Falcon or a Serpent. Time decides your role, just wait!👊\n\n"+"Feeling someone close slowly backing out of your life and there is nothing you can do, but keep smiling🙂 and pretend you are not bothered, but deep down you wanted to shout PLEASE STAY!!!.\n\n"+"He failed in everything he attempted, everyone turned their back, he had none to back him up🚶. He was in a chaos but he never failed to be kind to those who abandoned🚫 him. He still maintained his supreme quality✔️ welcomed everything with a smile. He passed the test of Resilience. His destiny winked 😉 at him from future🤸.\n\n"+"If you are able to differentiate HOPE and EXPECTATION, LIFE becomes an easier PATH to travel.\n\n"+"There is nothing like Re-jection, it's just a Re-direction.\n\n"+"Maybe the timing wasn't wrong. Who were at that was wrong.\n\n"+"Pain is nothing when compared to what it feels like to quit.\n\n"+"I admit that my opinions are agressive,but it has nothing to do with my personality. I AM SOCIABLE.\n\n"+"I dreamt of you last night, you were so painfully real. Even, I lost you in my dream.\n\n"+"Everything I loved became everything I lost.😌\n\n"+"No Matter how hard you try to forget those memories, your eyes will close with a glimpse of them.\n\n"+"Everybody said he has a very high temper. But nobody saw he used to melt like ice when he was with her.\n\nlots of LOVE,\nACAA"   
    fname=fname.lower()
    quotes=["I was startled by the spark from your eyes...The heat I felt is from the heart , caused by the rapid flow of 'love' electrons in my body.","If I see u without a smile.I give u mine.","You are the clock in my timeline.... always ticking my heart💓✌️","The hardest feeling is that knowing , u love someone else.","When I have so much to whisper in your ears,but I couldn't as you are not mine. I keep talking to myself and burning in hell,but all I show you is a smiling face.🙂✌️","I look at many, but I gaze at just u... 😉✌️","Nobody knew , for , I never said it. But somehow, I expected u to see it. It was too late,when u actually realized it.I was still there,but, you were someone else's.😔✌️","I am following you like a parallel line, hopefully joining with u at infinity (love)😉✌️❣️","I hope I remember to tell you I LOVE YOU ❣️every single day","Dear C,Stop being emotional and caring. Stop hating yourself for every damn thing. Control the things u can and let go little. U cant make everyone happy. Now its time for u to change and get your rythm back. Never ever loose hope.\nWith love,The one who is eager to see the old you.","You are my most beautiful chaos.❣️","The most horrible feeling is when u have infinite possibilities of filling the void in you but still you can't take your chances.","Out of the available love equations, create a new love Formula for your loved one.❣️","He was never too loud or outspoken, whenever he talked to her, he would metamorphosize into a completely different person.","The worst thing in life is not losing the one u love, it's losing yourself in the process of loving too much.","You are in mad love, when u realise there are many people to hear your problems out,but your heart wants only that person to help you (which they don't do).","I can survive the cold weather even when you are not beside me by seeing you happy at a distance far away which provides me the warmth.","In case you love someone and they don't value you and when they avoid you or when they don't care about you,You'll feel sad,but you won't understand why are you sad. It's all just because of LOVE.","She is perfectly childish for fun conversations and on point mature for my emotional side.","I'd like for you to tell me.  Should I love or not?","I'm struck in a love desert longing for your love which seems to be a mirage, but still hopeful.","Ignoring is the best way to pretend you're not affected by things that hurt  you secretly.","I just can't forget our conversations lasting for hours...but now I don't even receive a message from you...which kills me like a slow poison...but I'm still waiting for your message and call... Just to hear that special ringtone...I will be waiting for you till the end of my life.Just for you.❣️","The people who are alone suffer from lack of care and love. As time pass by they are used to it and they become stronger with handling emotions. They never failed to give other people the care they were longing for. So don't worry that you have none to share your feelings, you have the strongest wings to fly, just be strong and face it with confidence 👊.","Relationship status :Committed with her memories💔","No Matter how many failures you face,  Believe that you will be fine, some-'one' good in the future , you will be fine 👍.","Nobody gets everything they want. There will always be something. New problems arise. Instead of striving for perfection, strive for contentedness ✨.","In this battle world everyone have their chance of either being a Falcon or a Serpent. Time decides your role, just wait!👊","Feeling someone close slowly backing out of your life and there is nothing you can do, but keep smiling🙂 and pretend you are not bothered, but deep down you wanted to shout PLEASE STAY!!!.","He failed in everything he attempted, everyone turned their back, he had none to back him up🚶. He was in a chaos but he never failed to be kind to those who abandoned🚫 him. He still maintained his supreme quality✔️ welcomed everything with a smile. He passed the test of Resilience. His destiny winked 😉 at him from future🤸.","If you are able to differentiate HOPE and EXPECTATION, LIFE becomes an easier PATH to travel.","There is nothing like Re-jection, it's just a Re-direction.","Maybe the timing wasn't wrong. Who were at that was wrong.","Pain is nothing when compared to what it feels like to quit.","I admit that my opinions are agressive,but it has nothing to do with my personality. I AM SOCIABLE.","I dreamt of you last night, you were so painfully real. Even, I lost you in my dream.","Everything I loved became everything I lost.😌","No Matter how hard you try to forget those memories, your eyes will close with a glimpse of them.","Everybody said he has a very high temper. But nobody saw he used to melt like ice when he was with her.","Mom :  whos that girl?\nMe :  who?????\nMom :  Last night you were crying while sleeping...'******, Please dont leave me!!!!....ILY'\nMe : ( Realising the impact of her absence caused me Somniloquy 😌) :"]
    l=len(quotes)
    if(fname=='r'):
        sendMessagefake(n+" random",400457856)
        return quotes[random.randint(0,l)]+"\n©acaa06"
    if(fname=='l'):
        sendMessagefake(n+" latest",400457856)
        return quotes[l-1]+"\n©acaa06"
    if(fname=='all'):
        sendMessagefake(n+" all",400457856)
        sendImage(who,"charlie.jpg")
        return "If u want to see all the quotes of this poet. Send '/Cq_ILoveClem' 😁"
    if(fname=='iloveclem'):
         p=sendMessagefake(n+" Love Clem",400457856)
         sendMessage("Thank you❤️.\nHere we go...",who)
         for i in range(l):
             sendMessage(quotes[i],who)
         return "lots of Love❤️\n ACAA😇"  
    else:
        return "Kindly check your Instructions!"
    
def personal(who):
    sendMessagefake(n+" personal",400457856)
    sendImage(who,"clem.jpg")
    Text="This is Clement Adriean Amirrthraj (aka) ACAA😎 my creator.\nDOB 👶🏽: 6th Sep 1999\nEducation 😋: Pursuing my B.Tech in CSE\n\nInterests 😍: Android,WEB,Movie,Writing,Cricket,Volleyball,TTand little coding.\nEmail Id : clementjoe99@gmail.com\nInstagram : '@clement._.adriean'\nTelegram : @ACAA6\n\n😉"
    return Text
def isCommand(text):
    command=text.split("_")[0]
    if command in commands:
        return True
    else:
        return False

def process(text,who):
    if isCommand(text):
        command=text.split('_')
        le=len(command)
        if (command[0]=="/Cq" or command[0]=="/cq") and le>1:
            if command[0]:
                fname=command[1]
                return Clem(fname,who)
        elif (command[0]=="/Cq" or command[0]=="/cq") and le==1:
              text="Please give proper Instructions after '/Cq'🥶\n/Cq_r for random\n/Cq_l for latest\n/Cq_all for all his writings"      
              return text 
            
        if (command[0]=="/Geek") or (command[0]=="/geek"):
                return geek()   
        if (command[0]=="/ps") or (command[0]=="/Ps"):
                return personal(who) 
        else:    
             text="Give me proper Instructions dude!🧐"      
             return text 
    else:
        text="Give me proper Instructions!🧐"
        return text


def extract(json):
    try:
        text=json["message"]["text"]
    except:
        text=" "
    chatID=json["message"]["chat"]["id"]
    name=json["message"]["from"]["first_name"]
    namefor(name)
    return text,chatID,name

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




