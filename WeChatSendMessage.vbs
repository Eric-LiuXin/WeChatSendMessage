msg = Inputbox("���������뷢�͵���Ϣ��")
set objshell=createobject("wscript.shell")
command = "%comspec% /k python WeChatSendMessage.py " + msg
objshell.run(command),1,true
