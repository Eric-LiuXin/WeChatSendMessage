msg = Inputbox("请输入你想发送的信息！")
set objshell=createobject("wscript.shell")
command = "%comspec% /k python WeChatSendMessage.py " + msg
objshell.run(command),1,true
