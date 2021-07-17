#  7- Project 1 - Game

# 版本1.0：自定属性，人工PK

# 版本1.0

# 第一阶段的代码，我们的主要任务是理清战斗的逻辑，再用print()函数将战斗过程打印在终端。

# 根据这一版本的设定，我们要做的主要有三步：1.规定并显示出玩家和敌人的属性
# 2.双方同时互相攻击，血量根据对方的攻击力扣除
# 3.若有一方血量小于等于0，游戏结束。

#好，我们从第1步开始：设定【玩家】和【敌人】的属性，即【血量】和【攻击】。

print('【玩家】血量：100 攻击：50')  # 自定义玩家角色的血量和攻击
print('【敌人】血量：100 攻击：30')  # 自定义敌人角色的血量和攻击

#第2步：手动计算攻击一次，双方各自所剩的血量。

print('你发起了攻击，【敌人】剩余血量50')  # 人工计算敌人血量：100-50=50
print('敌人向你发起了攻击，【玩家】剩余血量70')  # 人工计算玩家血量：100-30=70

#第3步：继续做人工计算：算一算，玩家攻击2次敌人，敌人的血量就等于0了，这时候可以结束战斗，打印游戏结果。

print('你发起了攻击，【敌人】剩余血量0')  # 双方同时攻击，若血量出现小于等于0，游戏结束
print('敌人向你发起了攻击，【玩家】剩余血量40')

print('敌人死翘翘了，你赢了！') # 打印结果

#  很简单吧！现在我们要做的，就是把这三段代码拼起来，然后我会加一些修饰视觉的换行符和分割线，让运行结果看得更清楚一点。

print('【玩家】\n血量：100\n攻击：50')  # 自定义玩家角色的血量和攻击，用换行符'\n'来优化视觉
print('------------------------')  # 辅助功能，起到视觉分割的作用，让代码的运行结果更清晰

print('【敌人】\n血量：100\n攻击：30')
print('------------------------')

print('你发起了攻击，【敌人】剩余血量50')  # 人工计算敌人血量：100-50=50
print('敌人向你发起了攻击，【玩家】剩余血量70')  # 人工计算玩家血量：100-30=70
print('------------------------')

print('你发起了攻击，【敌人】剩余血量0')  # 双方同时攻击，若血量出现小于等于0，游戏结束
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')

print('敌人死翘翘了，你赢了！') # 打印结果

#  新知识点

import time   #调用time模块
# time.sleep(secs)
#使用time模块下面的sleep()函数，括号里填的是间隔的秒数（seconds，简称secs）
#time.sleep(1.5)就表示停留1.5秒再运行后续代码

#    这里有个新名词——模块，它是Python里一个重要的概念，我会在第16关给你详细介绍一番。
# 你可以把模块想象成是一个装着许多神奇函数的百宝箱，不过想要使用这个百宝箱里的函数，
# 得先用 import 模块名这样一句代码来打开它。

import time  #通常import语句会写到代码的开头

print('【玩家】\n血量：100\n攻击：50')
print('------------------------')
time.sleep(1.5)
#暂停1.5秒，再继续运行后面的代码

print('【敌人】\n血量：100\n攻击：30')
print('------------------------')
time.sleep(1.5)
#同上

print('你发起了攻击，【敌人】剩余血量50')
print('敌人向你发起了攻击，【玩家】剩余血量70')
print('------------------------')
time.sleep(1.5)

print('你发起了攻击，【敌人】剩余血量0')
print('敌人向你发起了攻击，【玩家】剩余血量40')
print('-----------------------')
time.sleep(1.5)

print('敌人死翘翘了，你赢了！')

#  这个版本的代码还有两个明显的缺陷：一是玩家和敌人的属性（血量&攻击）是我自己说了算，那胜负早已没有悬念；
# 二是战斗过程中血量的变化要自己手动算，那要计算机有何用？

# 你放心，这些都是我们会在版本2.0解决的问题。

# 版本2.0：随机属性，自动PK

#新知识点：
#Python-随机产生数据
# 1.random.random() 用于生成一个0到1的随机浮点数
# 2.random.randint(a,b) 用于生成一个最小值是a,最大值是b区间的整数
# 3.random.randrange(a,b,c)用于生成一个最小值是a,最大值是b区间，并且指定递增为c的整数


#可以多运行几次，看看结果是不是随机生成的~
import random
#调用random模块，与
a = random.randint(1,100)
# 随机生成1-100范围内（含1和100）的一个整数，并赋值给变量a
print(a)

#请听题：1.定义两个变量，来存储玩家血量和玩家攻击力的数值
# 2.血量是100-150的随机数，攻击力是30-50的随机数
# 3.将两个变量打印出来

import random
player_life = random.randint(100,150)
#表示玩家血量
player_attack = random.randint(30,50)
#表示玩家攻击
print(player_life)
print(player_attack)

# 对于取英文变量名，很多英语水平在高考即巅峰的同学会感到头疼，这里我推荐大家一个网站:CODELF
# （https://unbug.github.io/codelf），输入中文就可以看到别人是怎么命名的。

import time
import random
#也可合并写成一行：import time,random

# 生成随机属性
player_life = random.randint(100,150) # “player_life” 代表玩家血量
player_attack = random.randint(30,50) # “player_attack” 代表玩家攻击
enemy_life = random.randint(100,150) # “enemy_life” 代表敌人血量
enemy_attack = random.randint(30,50) # “enemy_attack” 代表敌人攻击

# 展示双方角色的属性
print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
#player_life和player_attack的数据类型都是整数，所以拼接时需要先用str()转换
print('------------------------')
time.sleep(1)
#暂停一秒再执行后续代码
print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
print('------------------------')

# 那截至目前，我们已经完成了随机生成属性和展示属性，接下来我们就来实现"自动战斗"。
# 说到循环，我们就要思考是要使用for循环还是while循环了。
# 因为现在双方的血量和攻击是随机生成，不是固定的。所以我们不知道具体要战斗多少回合才能分出胜负，也就是循环次数不明确，
# 那自然要用while循环。
# 我们进一步思考：while后面要接什么条件呢，也就是说什么条件下，战斗过程会一直持续呢？请你思考一下。
# 如果双方血量都大于0，战斗继续。
# 如果有一方血量小于等于0，战斗就结束了。

# 所以我们现在确定了让循环执行需要满足的条件就是——双方血量均大于零，也就是不死不休。
# 可见while后面要同时满足两个条件，即这两个条件要同时为真，所以我们要用and来连接，用代码来表示就是：
#      while (player_life >= 0) and (enemy_life >= 0):
#and两边的条件分别用括号括起，是一种习惯，方便阅读
# 其中【敌人】剩余血量=敌人当前血量-玩家攻击，【玩家】剩余血量=玩家当前血量-敌人攻击。
# 事实上我们之前已经定义好了这四个变量，每一次互相伤害后，player_life（玩家血量）和enemy_life（敌人血量）都会被重新赋值，
# 所以转换为代码逻辑就是：

#player_life = player_life - enemy_attack
#enemy_life = enemy_life - player_attack
# 赋值语句的执行顺序是先计算等号右边，再赋值给左边的变量

import time,random

player_life = random.randint(100,150)
player_attack = random.randint(30,50)
enemy_life = random.randint(100,150)
enemy_attack = random.randint(30,50)

print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
print('------------------------')
time.sleep(1)

while (player_life >0) and (enemy_life > 0):
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【玩家】剩余血量'+str(player_life))
    #player_life是整数，所以拼接时要先用str()转换
    print('敌人向你发起了攻击，【敌人】剩余血量'+str(enemy_life))
    print('------------------------')
    time.sleep(1.5)
    # 为了体现出战斗回合，这里停顿1.5秒

# 版本3.0：打印战果，三局两胜

#对比版本2.0，在版本3.0中，我们想要增加的功能是：
# 1.打印战果：每局战斗后，根据胜负平的结果打印出不同的提示；
# 2.三局两胜：双方战斗三局，胜率高的为最终赢家。

# 现在就请你根据代码区的提示，为游戏增加“打印战果”（单局）的功能。

import time,random

# 生成双方角色，并生成随机属性。
player_life = random.randint(100,150)
player_attack = random.randint(30,50)
enemy_life = random.randint(100,150)
enemy_attack = random.randint(30,50)

# 展示双方角色的属性
print('【玩家】\n'+'血量：'+str(player_life)+'\n攻击：'+str(player_attack))
print('------------------------')
time.sleep(1)
print('【敌人】\n'+'血量：'+str(enemy_life)+'\n攻击：'+str(enemy_attack))
print('------------------------')
time.sleep(1)

# 双方PK
while player_life > 0 and enemy_life > 0:
    player_life = player_life - enemy_attack
    enemy_life = enemy_life - player_attack
    print('你发起了攻击，【玩家】剩余血量'+str(player_life))
    print('敌人向你发起了攻击，【敌人】剩余血量'+str(enemy_life))
    print('-----------------------')
    time.sleep(1.5)

# 打印战果
if player_life > 0 and enemy_life <= 0:
    print('敌人死翘翘了，你赢了')
elif player_life <= 0 and enemy_life > 0:
    print('悲催，敌人把你干掉了！')
else:
    print('哎呀，你和敌人同归于尽了！')

# 我们可以将其拆分成两个部分：先来个三局，再判断最终胜负。
# 首先我们来看，三局战斗也是一个可以循环的结构，且循环次数是固定的，所以要用到for循环。

# 两个提示：
# 1.想清楚哪些代码要嵌套到for循环里，即一局战斗里包括什么信息。确定了for写在哪里之后，一句战斗包含的所有信息都要缩进；
# 2.细节也需要留意，如局与局之间要怎么区分开来（时间间隔&打印局数信息）

print('''如果做起来有些障碍，检查一下是否存在上面提示的这几个问题：

1. for循环语句的位置放的对不对？这个关键在于，你想让哪些信息被循环展示。
例如：如果你错将for循环语句放在了【随机属性】 和【自动战斗】之间，那每一局的战斗信息会是一样的，也就不存在什么三局两胜了。

2. 你写完for循环语句后，需要缩进的信息【整体】缩进了吗？如果没有缩进，可能存在报错，或者只有部分战斗信息循环的情况。

3. 细节注意到了吗？局与局之间要有明显间隔，那我们可以同时使用time.sleep()和print('现在是第x局')来完美解决这个问题。
此外，遇到各种报错的话，记得去搜索一下，看看报的是什么错，先自己尝试解决看看。

好，现在来看我的答案，请你主要看3-5行（后面内容都要放在for循环内部），然后运行看看效果。''')

player_victory = 0
enemy_victory = 0

if player_life > 0 and enemy_life <= 0:
    player_victory = player_victory + 1
    print('敌人死翘翘了，你赢了！')
elif player_life <= 0 and enemy_life > 0:
    enemy_victory  = enemy_victory + 1
    print('悲催，敌人把你干掉了！')
else:
    print('哎呀，你和敌人同归于尽了！')

#新知识点：
# 为了更方便地实现不同数据类型的拼接，用【格式符%】是更常用更便利的一种方式。
# 我们可以把%想象成：图书馆里用来占位的一本书。先占一个位置，之后再填上实际的变量。
# 举个例子：下面这两种写法是相同的，请你着重研究下第二行的语法。

print('血量：'+str(player_life)+' 攻击：'+str(player_attack))
print('血量：%s 攻击：%s' % (player_life,player_attack))

# 我们看到格式符%后面有一个字母s，这是一个类型码，用来控制数据显示的类型。%s就表示先占一个字符串类型的位置。
#占完位置之后，我们要以%的形式在后面补上要填充的内容，如此一来我们就免去了转换类型的烦恼。
# 如果是多个数据，就要把它们放进括号，按顺序填充，用逗号隔开。

lucky = 8
print('我的幸运数字是%d' % lucky)
print('我的幸运数字是%d' % 8)
print('我的幸运数字是%s' % '小龙女的生日816')
print('我的幸运数字是%d和%d' % (8,16))

print('''一个小小的提示：%后面的类型码用什么，取决于你希望这个%占住的这个位置的数据以什么类型展示出来，
如果你希望它以字符串形式展示，那就写%s，如果你希望它以整数形式展示，那就写%d。''')

print('我的幸运数字是%d，而且我不知道%d' % (8,16))  #8以整数展示
print('我的幸运数字是%s' % 8)  #8以字符串展示
print(8) #整数8与字符串'8'打印出来的结果是一样的
print('8')

# 版本3.0

import time
import random

player_victory = 0
enemy_victory = 0

for i in range(1,4):
    time.sleep(1.5)
    print('  \n——————现在是第 %s 局——————' % i)
    #对比之前：(' \n——————现在是第'+str(i)+'局——————')
    player_life = random.randint(100,150)
    player_attack = random.randint(30,50)
    enemy_life = random.randint(100,150)
    enemy_attack = random.randint(30,50)

    print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
    print('-----------------------')
    time.sleep(1)

    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('你发起了攻击，【玩家】剩余血量%s' % player_life)
        print('敌人向你发起了攻击，【敌人】的血量剩余%s' % enemy_life)
        print('-----------------------')
        time.sleep(1.2)

    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('敌人死翘翘了，你赢了！')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('悲催，敌人把你干掉了！')
    else:
        print('哎呀，你和敌人同归于尽了！')

if player_victory > enemy_victory :
    time.sleep(1)
    print('\n【最终结果：你赢了！】')
elif enemy_victory > player_victory:
    print('\n【最终结果：你输了！】')
else:
    print('\n【最终结果：平局！】')

print('''练习目标：
我们会在项目1代码的基础上，添加一个新功能，同时练习循环和判断的知识。

练习要求：
新功能是：每盘（3局）游戏结束后，游戏会问我们是否要继续游戏，再加一盘。
我们可以选择再来一盘，也可以选择退出游戏。

进一步拆解和分析

方案1：while True+break
开启一个无限循环，设定跳出条件。

方案2：while 变量名+变量名的布尔值判断
在开头设某变量的布尔值为True，input后开启判断变量的布尔值是否改变。

升级项目1

请你选用上面方案中的一种，为项目1增加“再来一局”的功能。

参考代码用了方案1。当然，方案2也是可以的——只要成功添加了新功能。''')

#方法一
import time
import random
while True:
    player_victory = 0
    enemy_victory = 0
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
        print('-----------------------')
        time.sleep(1)
        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【玩家】剩余血量%s' % player_life)
            print('敌人向你发起了攻击，【敌人】的血量剩余%s' % enemy_life)
            print('-----------------------')
            time.sleep(1.2)
        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')
    if player_victory > enemy_victory :
        time.sleep(1)
        print('\n【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')
    else:
        print('\n【最终结果：平局！】')
    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break

 #方法二
import time
import random

player_victory = 0
enemy_victory = 0
again = True
while again:
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 %s 局——————' % i)
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        print('【玩家】\n血量：%s\n攻击：%s' % (player_life,player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：%s\n攻击：%s' % (enemy_life,enemy_attack))
        print('-----------------------')
        time.sleep(1)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【玩家】剩余血量%s' % player_life)
            print('敌人向你发起了攻击，【敌人】的血量剩余%s' % enemy_life)
            print('-----------------------')
            time.sleep(1.2)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory :
        time.sleep(1)
        print('\n【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')
    else:
        print('\n【最终结果：平局！】')

    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')  # 在 while True 循环中设置跳出条件。
    if a1 == 'n':
        again = False
    else:
        again = True

print('''练习目标
在这个练习，我们会学会一种新的“格式化字符串”的方法：format()函数。

练习要求
在项目1的末尾，我们学会了一种简化代码的方式：格式化字符串。
不过，还有一种更强大的方法，下面我们会先学习，然后再练习。


!!! 学习format()函数

format()函数是从 Python2.6 起新增的一种格式化字符串的函数，功能比课堂上提到的方式更强大。
format()函数用来占位的是大括号{}，不用区分类型码（%+类型码）。
具体的语法是：'str.format()'，而不是课堂上提到的'str % ()'。
而且，它对后面数据的引用更灵活，不限次数，也可指定对应关系。
看完左侧的代码、结果和注释，你就懂上面几句话的意思了。


运用format()函数

将代码中字符串格式化的代码改成format()函数的方法，改完后运行一下，检验是否正确。

一共有5行代码需要改，你都找到了吗？
对了，format()在数字格式化的方面提供了很多种选择，有兴趣的可以查一下。''')

import time
import random

player_victory = 0
enemy_victory = 0

while True:
    for i in range(1,4):
        time.sleep(1.5)
        print('  \n——————现在是第 {} 局——————'.format(i))
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)

        print('【玩家】\n血量：{}\n攻击：{}'.format(player_life,player_attack))
        print('------------------------')
        time.sleep(1)
        print('【敌人】\n血量：{}\n攻击：{}'.format(enemy_life,enemy_attack))
        print('-----------------------')
        time.sleep(1)

        while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack
            enemy_life = enemy_life - player_attack
            print('敌人发起了攻击，【玩家】剩余血量{}'.format(player_life))
            print('你发起了攻击，【敌人】的血量剩余{}'.format(enemy_life))
            print('-----------------------')
            time.sleep(1.2)

        if player_life > 0 and enemy_life <= 0:
            player_victory += 1
            print('敌人死翘翘了，你赢了！')
        elif player_life <= 0 and enemy_life > 0:
            enemy_victory += 1
            print('悲催，敌人把你干掉了！')
        else:
            print('哎呀，你和敌人同归于尽了！')

    if player_victory > enemy_victory :
        time.sleep(1)
        print('\n【最终结果：你赢了！】')
    elif enemy_victory > player_victory:
        print('\n【最终结果：你输了！】')
    else:
        print('\n【最终结果：平局！】')

    a1 = input('要继续游戏吗，请输入n退出，输入其他继续：')
    if a1 == 'n':
        break
