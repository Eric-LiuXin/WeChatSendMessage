# -*- coding: UTF-8 -*-
import sys
import itchat

def WeChatSend():
    itchat.auto_login(hotReload=True)
    user_list = list()
    friends = itchat.get_friends(update=True)[0:]
    [user_list.append(friend['UserName']) for friend in friends]
    [itchat.send_msg(msg=sys.argv[1], toUserName=to_user_name) for to_user_name in user_list]

if __name__=="__main__":
    if(len(sys.argv) != 2):
        print ("请输入你想发送的信息！")
    else:
        #print (sys.argv[1])
        WeChatSend()
