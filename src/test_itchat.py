# -*- coding: utf-8 -*-  

import itchat as IC
from itchat import auto_login as login

print ("itchat Start!")

login (hotReload=True)

IC.send('Test 中文（全角字符utf-8）,发给自己', toUserName='wzk.py')

