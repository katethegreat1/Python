# 第3课 input()函数

# print()函数是输出函数。是人给程序下达一个打印命令，程序想都不想，一比一地打印出结果。
# 这种程序向屏幕输出信息的过程，就是人与计算机的单向沟通。

# input()函数是输入函数，当你在函数的括号内写出问题时，input()函数会将此问题原样显示在屏幕上，
# 并在终端区域等待你针对此问题的回答。实现真正的人机互动沟通。

#  1. input()函数结果的赋值
#为了能随时且方便地提取输入值（输入的结果），我们需要把input()函数的结果赋给变量。

name = input('请铲屎官输入宠物的名字：')
print('I Love '+name +'!')


#1.请求输入你喜欢的电影名：；2. 将结果赋值给变量movie；3. 打印结果movie+'是我最喜欢的电影！'
# 【要点提示：赋值，input()函数，变量拼接，print()函数】

movie=input("Name a movie:")
print(movie +' is my favourite movie!')

#首先，我们需要对input()函数的结果进行赋值，然后使用input()函数搜集信息，最后再用print()函数输出结果。

import time
print('亲爱的同学：')
time.sleep(0)
print('我们愉快地通知您，您已获准在霍格沃茨魔法学校就读。')
time.sleep(0.5)
print('那么，您的选择是什么？`1`接受，还是`2`放弃呢？')

choice = input('请输入您的选择：')
#变量赋值

if choice == '1':
#条件判断:条件1
    print('霍格沃茨欢迎您的到来。')
    #条件1的结果

else:
#条件判断：其他条件
    print('您可是被梅林选中的孩子，我们不接受这个选项。')
    #其他条件的结果

#为什么if条件下的变量choice是字符串'1'呢？如果不是字符串格式，是整数1会出现什么结果呢？
#怎么样？是不是不管你输入的是1还是2，显示的结果都是else条件下的结果：'您可是被梅林选中的孩子，我们不接受这个选项。'？

#  2.input()函数的数据类型

#!!! 对于input()函数来说，不管我们输入的回答是什么，
# input()函数的输入值（搜集到的回答），永远会被强制性地转换为字符串类型。（Python3固定规则）
# 就这样，因为我们输入的信息永远是字符串，永远不能满足if的整数条件。
# 所以，不管你输入的是什么，程序只有一个选择：执行else下的结果。

# Solution 1:

age = '7'    # NOT 7

choice = input('请你猜一下小埋今年多大了：')

if choice == age:
    print('猜对惹～你好厉害！ ヽ✿゜▽゜)ノ～～～')

elif choice < age:
    print('小埋的提示：你猜小了（；´д｀）ゞ。。。。')

else:
    print('小埋的提示：乃猜大了惹(＞﹏＜)～～')

# second solution:

age = 7

choice = int(input('请你猜一下小埋今年多大了：'))

if choice == age:
    print('猜对惹～你好厉害！ ヽ✿゜▽゜)ノ～～～')

elif choice < age:
    print('小埋的提示：你猜小了（；´д｀）ゞ。。。。')

else:
    print('小埋的提示：乃猜大了惹(＞﹏＜)～～')

# 下面，请挥舞你隐形的翅膀，将上方月工资的代码，添加另一条件：
# 【当工资大于5000，小于10000时】。打印结果：【我们都是搬砖族。。。】，
# 并将添加条件后的整段代码写在下方区域。【要点提示：三个条件并存时，请使用if…elif…else…语句】

money = int(input('你一个月工资多少钱？'))
#将输入的工资数（字符串），强制转换为整数

if money >= 10000:
    #当工资数（整数）大于等于10000（整数）时
    print('土豪我们做朋友吧！')
    #打印if条件下的结果

elif money >5000:                  #added
    print('我们都是搬砖族。。。')          #added

else:
    #当工资数（整数）小于等于10000（整数）时
    print('我负责赚钱养家，你负责貌美如花～')
    #打印else条件下

#人们都说代码是最冷酷无情的：错就是错，对就是对。但是在我看来，世界上没有比代码更有人情味的东西了，
# 因为代码会跨越语言障碍，链接整个世界的网络，拉近人与人之间的距离。

# HW1

num=input('input a number ')
if num==6:
    print(num+'1')
else:
    print(num+'3')

# Input 6, result is 63 not 7.

# Thoughts:
number=int(input('input a number '))
if number == 6:
    print('Your lucky number is ' + str(number+1))
else:
    print('Your lucky number is ' + str(number//9))

#HW2
#（实操题）薪酬计算器
# 答案解析：根据题干要求，整体的薪酬按照业绩分，可以分成四个区间，超过10万，8万至10万，5万至8万，小于5万，
# 这四个区间可以作为if添加句的判断依据，然后根据绩效提成比例计算出提成工资，再加上基础工资即可。

sales=int(input("What's your sales this month? "))
base=6000
if sales>=100000:
    print('Your salary is '+str(sales*0.1+base))
elif sales >=80000:
    print('Your salary is ' + str(sales * 0.08 + base))
elif sales>=50000:
    print('Your salary is ' + str(sales * 0.06 + base))
else:
    print('Your salary is '+ str(base))

#HW 3

name=input('name your pet ')
print(name + ' is your best poppy')


#HW 4
#请你写一段代码，并满足以下条件：
#如果罗恩一天吃超过10个巧克力蛙，罗恩要给哈利100块；
#如果罗恩一天吃小于等于10个的巧克力蛙，哈利就给罗恩100块。
#输入罗恩吃的巧克力数量，并判断是哈利给罗恩钱，还是罗恩给哈利钱。

num = int(input('How many chocolate did you have today? '))
if num>10:
    print('Ron own Harry $100')
else:
    print('Harry own Ron $100')

#HW5

print('''书写代码

请你综合四天所学知识，将下面的对话，用代码表现出来。

小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？
你：需要
小精灵：请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询
你：2
小精灵：金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币
小精灵：请问您需要兑换多少金加隆呢？
（你说了一个数字N）
小精灵：好的，我知道了，您需要兑换（你说的数字N）金加隆。
小精灵：那么，您需要付给我（你说的数字N*51.3）人民币。

注1：如果选择不需要帮助，小精灵会礼貌地说'好的，再见。'
注2: 如果选择帮助【1 存取款】，小精灵会推荐你去存取款窗口；
如果选择帮助【3 咨询】，小精灵会推荐你去咨询窗口。''')

answer1=input('小精灵：您好，欢迎古灵阁，请问您需要帮助吗？需要or不需要？')
if answer1=='需要':
    answer2=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if answer2==1:
        print('推荐你去存取款窗口')
    elif answer2==3:
        print('推荐你去咨询窗口')
    else:
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        answer3=float(input('小精灵：请问您需要兑换多少金加隆呢？'))
        print('好的，我知道了，您需要兑换 '+str(answer3)+ ' 金加隆.')
        #！！！错误：print('好的，我知道了，您需要兑换 str(answer3) 金加隆.')
        print('那么，您需要付给我 '+str(answer3*51.3)+' 人民币。' )
else:
    print('好的，再见。')


# 参考答案
chioce = input('您好，欢迎古灵阁，请问需要帮助吗？需要or不需要？')
if chioce == '需要':
    number = input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询')
    if number == '2':
        print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
        print('请问您需要兑换多少金加隆呢？')
        money = input('请输入你需要兑换的金加隆')
        print('好的，我知道了，您需要兑换' + money + '金加隆。')
        print('那么，您需要付给我'+str(int(float(money)*51.3))+'人民币。')
    elif number == '1':
        print('请到存取款窗口办理')
    elif number == '3':
        print('请到咨询窗口咨询')
    # 加上else语句当输入不是1、2、3时，提示输入错误
    else:
        print('输入错误，没有你需要的服务')

elif chioce == '不需要':
    print('好的，再见')
# 加上else语句当输入不是1、2、3时，提示输入错误
else:
    print('输入错误')
