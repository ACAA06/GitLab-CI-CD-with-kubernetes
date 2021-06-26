from main import *
lastUpdateID=None
print ('firing up\n')
while True:
    updates=getUpdates(lastUpdateID)
    if len(updates["result"])>0:
        lastUpdateID=getLatestUpdateID(updates) + 1
        for update in updates["result"]:
            message,who,name=extract(update)
            try:
                print("from",name,"message",message)
            except:
                pass 
            if message=="/start":
                reply="Hello, "+name+". I'm Poetu Clem😃, the writer in ACAA. You can check his writings here ❄ and you can also get some geek jokes🤡😃.\n\nTo get Clement's writings: \n/Cq_r   (random)\n/Cq_l    (latest)\n/Cq_all (all his writings)\nTo get geek jokes:\n/Geek\nTo get info about Clement:\n/Ps"
            else:
                reply=process(message,who)
            sendMessage(reply,who)
            print(reply, "reply sent")    

       
