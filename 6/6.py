#   6

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




