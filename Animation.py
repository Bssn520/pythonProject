"""
Animation列表：
周一：<br>
国漫：星辰变，早10点；<br>
日漫：<br>

周二：<br>
国漫：诛仙，早10点；<br>
日漫：<br>

周三：<br>
国漫：一念永恒，早10点；<br>
日漫：恋爱Flops，晚20点；异世界舅舅，晚21点；<br>

周四：<br>
国漫：神印王座，早10点；<br>
日漫：<br>

周五：<br>
国漫：完美世界，早10点；炼气练了三千年，早11点；<br>
日漫：<br>

周六：<br>
国漫：斗罗大陆，早10点；三体，早11点；<br>
日漫：Spy Family，晚22点；点满农民相关技能后，不知为何就变强了，晚21点；<br>

周末：<br>
国漫：斗破苍穹，早10点；<br>
日漫：夫妇以上，恋人未满，晚21点；<br>

<br>

https://wxpusher.zjiecode.com/api/send/message/?appToken=AT_6crkVF8PkVbnK82DVr16RSWbqxCJ0keO&content=
&uid=UID_bhSNYY9Z28qQkIMyPjjkP13D7a0u&url=https%3A%2F%2Fgitee.com%2Fbssn007%2FAnimationUpdate%2Fraw%2Fmaster%2FAnimation
"""
import urllib.parse
#番剧列表
front = "https://wxpusher.zjiecode.com/api/send/message/?appToken=AT_6crkVF8PkVbnK82DVr16RSWbqxCJ0keO&content="
behind = "&uid=UID_bhSNYY9Z28qQkIMyPjjkP13D7a0u&url=https%3A%2F%2Fgitee.com%2Fbssn007%2FAnimationUpdate%2Fraw%2Fmaster%2FAnimation"

monday = ['星辰变，早10点；<br>']
monday_japan = ['<br>']

tuesday = ['诛仙，早10点；<br>']
tuesday_japan = ['<br>']

wednesday = ['一念永恒，早10点；<br>']
wednesday_japan = ['恋爱Flops，晚20点；', '异世界舅舅，晚21点；<br>']

thursday = ['神印王座，早10点；<br>']
thursday_japan = ['<br>']

friday = ['完美世界，早10点；', '炼气练了三千年，早11点；<br>']
friday_japan = ['<br>']

saturday = ['斗罗大陆，早10点；', '三体，早11点；<br>']
saturday_japan = ['Spy Family，晚22点；<br>']

sunday = ['斗破苍穹，早10点；<br>']
sunday_japan = ['夫妇以上，恋人未满，晚21点；<br>']
#--------------------
oneday = input("请问你想添加周几的动漫：")
kinds = input("请问是国漫还是日番：")
name = input("输入你想添加的番剧名称：")
#周一
if oneday=="周一" and kinds=="国漫":
    oringinal = monday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del monday[-1]
    monday.append(oringinal_new)
    name_new = name+"<br>"
    monday.append(name_new)
    print(monday)
    print(monday_japan)
    name_new2 = urllib.parse.quote(name_new)
    print("最终链接为：\n"+front+name_new2+behind)

elif oneday=="周一" and kinds=="日番":
    oringinal = monday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del monday_japan[-1]
    monday_japan.append(oringinal_new)
    name_new = name + "<br>"
    monday_japan.append(name_new)
    print(monday)
    print(monday_japan)

#周二
elif oneday=="周二" and kinds=="国漫":
    oringinal = tuesday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del tuesday[-1]
    tuesday.append(oringinal_new)
    name_new = name+"<br>"
    tuesday.append(name_new)
    print(tuesday)
    print(tuesday_japan)
elif oneday=="周二" and kinds=="日番":
    oringinal = tuesday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del tuesday_japan[-1]
    tuesday_japan.append(oringinal_new)
    name_new = name + "<br>"
    tuesday_japan.append(name_new)
    print(tuesday)
    print(tuesday_japan)

#周三
elif oneday=="周三" and kinds=="国漫":
    oringinal = wednesday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del wednesday[-1]
    wednesday.append(oringinal_new)
    name_new = name+"<br>"
    wednesday.append(name_new)
    print(wednesday)
    print(wednesday_japan)
elif oneday=="周三" and kinds=="日番":
    oringinal = wednesday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del wednesday_japan[-1]
    wednesday_japan.append(oringinal_new)
    name_new = name + "<br>"
    wednesday_japan.append(name_new)
    print(wednesday)
    print(wednesday_japan)

#周四
elif oneday=="周四" and kinds=="国漫":
    oringinal = thursday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del thursday[-1]
    thursday.append(oringinal_new)
    name_new = name+"<br>"
    thursday.append(name_new)
    print(thursday)
    print(thursday_japan)
elif oneday=="周四" and kinds=="日番":
    oringinal = thursday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del thursday_japan[-1]
    thursday_japan.append(oringinal_new)
    name_new = name + "<br>"
    thursday_japan.append(name_new)
    print(thursday)
    print(thursday_japan)

#周五
elif oneday=="周五" and kinds=="国漫":
    oringinal = friday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del friday[-1]
    friday.append(oringinal_new)
    name_new = name+"<br>"
    friday.append(name_new)
    print(friday)
    print(friday_japan)
elif oneday=="周五" and kinds=="日番":
    oringinal = friday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del friday_japan[-1]
    friday_japan.append(oringinal_new)
    name_new = name + "<br>"
    friday_japan.append(name_new)
    print(friday)
    print(friday_japan)

#周六
elif oneday=="周六" and kinds=="国漫":
    oringinal = saturday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del saturday[-1]
    saturday.append(oringinal_new)
    name_new = name+"<br>"
    saturday.append(name_new)
    print(saturday)
    print(saturday_japan)
elif oneday=="周六" and kinds=="日番":
    oringinal = saturday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del saturday_japan[-1]
    saturday_japan.append(oringinal_new)
    name_new = name + "<br>"
    saturday_japan.append(name_new)
    print(saturday)
    print(saturday_japan)

#周日
elif oneday=="周日" and kinds=="国漫":
    oringinal = sunday[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del sunday[-1]
    sunday.append(oringinal_new)
    name_new = name+"<br>"
    sunday.append(name_new)
    print(sunday)
    print(sunday_japan)
elif oneday=="周日" and kinds=="日番":
    oringinal = sunday_japan[-1]
    oringinal_new = oringinal.replace(oringinal[-4:], "", 1)
    del sunday_japan[-1]
    sunday_japan.append(oringinal_new)
    name_new = name + "<br>"
    sunday_japan.append(name_new)
    print(sunday)
    print(sunday_japan)


