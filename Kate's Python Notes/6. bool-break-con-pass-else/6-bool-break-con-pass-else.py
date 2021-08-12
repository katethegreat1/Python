#   第6课   布尔值  +  4个语句 break, con, pass, else

info = {1:2,3:4,5:6}
for i in info:
    print(i,info[3],info[5])

print(1==1)

# while True:
#     print('while True')   # 死循环

if False:
    print('if False')
if True:
    print('if True')    # 不会陷入死循环

if 1:
    print('熊猫')

# Python False Values: False, 0, '', [], {}, None.
# Everything else is Ture!!!

    #至于None，它代表的是【空值】，自成一派，数据类型是NoneType。
    # 要注意它和0的区别，0是整数0，可并非什么都没有。

# 我们可以使用bool()函数来查看一个数据会被判断为真还是假。这个函数的用法与type()函数相似（还有印象吧~），
# 在bool()函数括号中放入我们想要判断真假的数据，然后print出来即可。

print('以下数据判断结果都是【假】：')
print(bool(False))
print(bool(0))
print(bool(''))

dict = {'法国':'巴黎','日本':'东京','中国':'北京'}
a = '日本'
print(bool(a in dict))   # True
print(bool('法国'not in dict))      # False

a=True
print(not a)  # False

i = 1
while i<6 :
   print('把这句话打印5遍')
   i = i+1

print('''今天理解布尔运算原理后，可以把这段代码改造成更“程序员”的方式：''')

i = 5
while i:
   print('把这句话打印5遍')
   i = i-1     # 注意是-不是+，+就无限循环喇。-到0为假，停止循环。

   # break语句

print('下面是一个for循环代码，本来会循环5次，但循环到第4次的时候就被break语句打断，然后结束循环了。')

for i in range(5):     #   0,1,2,3,4
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        break # 结束循环

print('下面是一个while循环代码，本来会循环5次，但循环到第3次的时候就被break语句打断，然后结束循环了。')

i = 0
while i<5:
    print('明日复明日')
    i = i+1
    if i==3:  # 当i等于3的时候触发
        break # 结束循环

while True:
    print('上供一对童男童女')
    t = input('孙悟空来了吗')
    if t == 'yes':
        break
print('孙悟空制服了鲤鱼精，陈家庄再也不用上供童男童女了')

print('''第1行代码：while True我们在上面见过了，这个条件恒为真，就会开启无限循环。
而while True常和break语句搭配使用，你也可以学着使用这种写法。

第2行代码：打印上供一对童男童女的字符串。第3行代码：请用户输入一个信息。

第4行代码：如果用户输入的信息是 “来了”，那么if后面的条件被满足，执行下面的代码break；
如果没有，回到while True 继续循环。

第5行代码：break表示结束循环，然后去执行循环外部的代码，即第6行代码，打印孙悟空制服了鲤鱼精的字符串。''')

# 我想请你写下这样一个程序，功能是请用户输入密码，如果输入了错误的密码，就一直循环请用户继续输入；
# 如果输入了正确的密码，就结束循环。设定这个密码为'123'。

password = ''  # 变量password用来保存输入的密码
while password!='123':                 # 注意 不是 123
    password=input('尝试输入密码：')
print('结束循环')

print('''提示：① 用while True开启无限循环。② 在循环内部用input() 函数获取用户的数据。 
③ 使用if...break，如果变量p == '123'，那就break结束循环。否则又开始循环。
④ 结束循环后，打印--通过啦~''')

while True:
    code = input('尝试输入密码：')
    if code == '123':
        print('结束循环')
        break

# or

while True:
    code = input('尝试输入密码：')
    if code == '123':
        break
print('结束循环')



#   continue语句

# continue语句搭配for循环
for i in range(5):
    print('明日复明日')
    if i == 3:  # 当i等于3的时候触发
        continue  # 回到循环开头
    print('这句话在i等于3的时候打印不出来')


# continue语句搭配while循环
i = 0
while i < 5:
    print('明日复明日')
    i = i + 1
    if i == 3:  # 当i等于3的时候触发
        continue  # 回到循环开头
    print('这句话在i等于3的时候打印不出来')

# story time
while True:
    q1 = input('第一问：你一生之中，在什么地方最是快乐逍遥？')
    if q1 != 'ice':
        continue
    print('答对了，下面是第二问：')
    q2 = input('你生平最爱之人，叫什么名字？')
    if q2 != 'you':
        continue
    print('答对了，下面是第三问：')
    q3 = input('你最爱的这个人相貌如何？')
    if q3 == 'great':
        break
print('都答对了，你是虚竹。')


# pass语句

a = int(input('请输入一个整数:'))
if a >= 100:
    pass
else:
    print('你输入了一个小于100的数字')

#  这个代码的意思是：当a>=100的时候，跳过，什么都不做。其他情况，也就是a<100的时候，执行一个print语句。

#  else语句

for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')


# OR:

    i = 0
    while i < 5:
        a = int(input('请输入0结束循环，你有5次机会:'))
        i = i + 1
        if a == 0:
            print('你触发了break语句，导致else语句不会生效。')
            break
    else:
        print('5次循环你都错过了，else语句生效了。')

# 循环小练习
#
# 大家应该玩过一个小游戏，就是一个人在心里想好一个数，比如24，然后让另一个人猜。
# 如果他猜的数比24小，告诉他“太小了”，如果他猜的数比24大，告诉他“太大了”。
# 我们一起来完成这个“猜大小游戏”的编程，我的思路大概是这样的：

# 1.一个人在心里想好一个数————所以这个数字是提前准备好的，所以可以设置一个变量来保存这个数字。我就设置我的数字为24。
# 2.然后让另一个人猜————所以可以使用input()函数来接收另一个人输入的数字，并用int()转化为整数。
# 3.直到猜对为止————天知道几次才能猜对，所以肯定需要用到循环，并且由于不知道要循环几次，所以适合while循环。
# 4.如果他猜的数比24小就告诉他“太小了”，
# 如果他猜的数比24大就告诉他“太大了”——这里一看“如果……就……”的描述，就知道应该用if...else...写一个条件判断。

while True:
    num=int(input('guess a num'))
    if num<24:
        print('too small')
    elif num>24:
        print('too big')
    else:
        print('yes')
        break

print('这是老师的答案:')
secret = 24  #设定秘密数字
while True:
    guess = int(input('你来猜猜我的秘密数字是多少:'))   #输入猜测数字
    if guess ==secret:  #数字对比
        print('正确！你很棒哦。')
        break
    elif guess >secret:
        print('你猜的太大了，请重新猜猜~')
    else:
        print('你猜的太小了，请重新猜猜~')

print ('这个游戏只能猜3次，3次都猜不中，就告诉他“失败了”。')

num=24
for i in range (3):
    guess = int(input('Guess the num'))
    if guess == num:
        print('Yes!')
        break
    elif guess < num:
        print('Too small')
    else:
        print('Too big')
else:
    print('给你3次机会都猜不到，你失败了。')

#  for...in...可以和else语句搭配使用。意思是在for...in...循环结束之后，执行else语句里的命令。
#  不过如果for...in...是因为break结束的就不会执行else语句里的命令。


#   HW
#   （实操题）假如投资的年利润为5%，求从1000元增加到5000元，需要花费多少年？

i = 1000
j=0
while True:
    i = i * 1.05
    if i >=5000:
        break
    j+=1
print(j)

print('''练习目标：
我们会通过今天的作业，综合运用while True循环和 break。
练习要求：
假设有两名囚徒A和B因为合伙犯罪被抓捕，因没有确凿可以指认罪行的证据，审判者准备单独审判两位囚徒。
若两人都认罪，则两人各判10年；若一个认罪一个抵赖，则认罪的人判1年，抵赖的人判20年；
若两人都抵赖，则各判3年。''')

a=input('1号，你认罪吗？')
b=input('2号，你认罪吗？')
if a=='yes' and b=='yes':
    print('10years for both')
elif a=='yes' or b=='yes':
    print('1year for yes and 20years for no')
else:
    print('3years for both')

# 现在，请写个代码：当两人都抵赖时，打印判决，代码结束；若为其他结果，则在打印判决后继续循环。

while True:
    a = input('A，你认罪吗？请回答认罪或者不认:')
    b = input('B，你认罪吗？请回答认罪或者不认:')
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break  # 当满足开头提到的条件时，跳出循环。

    print('''现在有一个社会学家，在不同的人群中做这个实验，一旦遇到都不认罪的情况，就停止该人群中的实验。
同时，他希望程序能记录每一对实验者的选择，以及记录第几对实验者都选择不认罪。请你帮帮他吧。
几个提示：
为了记录每一对实验者的选择，需要用一个可拓展的“容器”来存放这些数据；
为了记录是第几对实验者做了最优选择，需要用一个变量来计数；
为了将每一对实验者的选择再打印出来，需要写一个循环。''')

n = 0
list_answer = []
while True:
    n += 1
    a = input('A，你认罪吗？请回答认罪或者不认：')
    b = input('B，你认罪吗？请回答认罪或者不认：')
    list_answer.append([a,b])
    if a == '认罪' and b == '认罪':
        print('两人都得判10年，唉')
    elif a == '不认' and b == '认罪':
        print('A判20年，B判1年，唉')
    elif a == '认罪' and b == '不认':
        print('A判1年，B判20年')
    else:
        print('都判3年，太棒了')
        break
print('第' + str(n) + '对实验者选了最优解。')
for i in range(n):
    print('第' + str(i+1) + '对实验者的选择是：' + str(list_answer[i]))

# 补充代码，让代码运行时输入演员的名字时，可以打印出：××出演了电影××。
# 注：这个练习的提示比较完整，建议先多尝试几次独立完成。


movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

movies = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}

actor = input('你想查询哪个演员？')
for  movie in movies:  # 用 for 遍历字典
    actors = movies[movie]  # 读取各个字典的主演表
    if actor in actors:
        print(actor + '出演了电影' + movie)




