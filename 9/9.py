#第9课 函数

#用贩卖机来打比方，贩卖机是设定好可以直接使用（组织好的），可以重复上架售卖不同的物品（重复使用），功能是卖东西（单一功能）。
#而函数呢？以print()函数为例，它也是设定好可以直接使用（组织好的），不论你想打印什么参数都可以（重复使用），
#而print函数能实现的单一功能就是“打印”。
#好，现在问题来了，就像贩卖机不总是有我们想要的东西。除了Python自带的内置函数，我们能不能根据自己编写程序的需要，自己定义一个独一无二的函数呢？
#答案是肯定的，下面我就来教大家如何DIY一个函数。

#  1. 定义函数

def greet(name):
    print(name+'早上好')
    return

#函数名：最好是取体现函数功能的名字，一般用小写字母和单下划线、数字等组合
def greet(name):
#参数：根据函数功能，括号里可以有多个参数，也可以不带参数，命名规则与函数名相同
#规范：括号是英文括号，后面的冒号不能丢
    print(name+'早上好')
#函数体：函数体就是体现函数功能的语句，要缩进，一般是四个空格
    return
#  看到第三行注释，你可能会有点疑问，怎么括号里可以有参数，又能没有参数？
#  接下来我举个小例子，你可以对比一下。

# 第一个函数
def pika1():
    print('我最喜爱的神奇宝贝是皮卡丘')

# 第二个函数
def pika2(name):
    print('我最喜爱的神奇宝贝是' + name)

# 第三个函数
def pika3(name, person):
    print('我最喜爱的神奇宝贝是' + name)
    print('我最喜爱的驯兽师是' + person)

#    2. 调用函数
def pika2(name):
    print('我最喜爱的神奇宝贝是'+name)
pika2('皮卡丘')  #调用函数，输入函数名pika()并输入参数'皮卡丘'
pika2('喷火龙')  #调用函数，输入函数名pika()并输入参数'喷火龙'

print(1)
def pika1():
    print('我最喜爱的神奇宝贝是皮卡丘')
# 该函数没有参数，直接调用函数名。记得英文括号一定不能少
pika1()

print(2)
def pika2(name):
    print('我最喜爱的神奇宝贝是' + name)
# 需要给参数name赋值，每次调用都可以给参数赋不同的值
pika2('皮卡丘')
pika2('喷火龙')

print(3)
def pika3(name, person):
    print('我最喜爱的神奇宝贝是' + name)
    print('我最喜爱的驯兽师是' + person)
# 需要给两个参数分别赋值，并用逗号隔开，否则会报错
pika3('卡比兽', '小智')


# Exercise:

def fav(name,color,pet):
    print(name+"'s fav color is " + color+'.')
    print(name+ "'s fave pet is "+pet+'.')
fav('Kate','blue','T')
fav('T','white', 'Kate')

#  通过这个例子，我们明白调用函数最关键的是：
#  得弄清楚这个函数有多少个参数，如何给参数赋值，这个过程在函数里叫做参数的传递(pass)。

#那么，定义和调用函数的基本语法就讲得差不多了。这里想强调的是，为了让大家理解基本概念，目前举的例子都只是在实现非常简单的功能。
#但函数的作用远不仅如此，它能将复杂的语句和功能统一封装进一个函数名里，调用者只需明白函数能实现什么，根据需要传递参数即可。
#例如，这个tree()函数能打印出一颗圣诞树，参数是圣诞树的层高。现在请你调用该函数两次，分别传递参数4和8，点击运行。

def tree(Height):
    print('Merry Christmas!')
    for i in range(Height):
        print((Height-i)*2*' '+'o'+ i*'~x~o')
        print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
tree(4)
tree(8)

# 主要的参数类型有：位置参数、默认参数、不定长参数。我会用一个案例把这些参数串起来。

#    1. 【位置参数】
def  menu(appetizer,course):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course)
menu('话梅花生','牛肉拉面')

# 这里的'话梅花生'和'牛肉拉面'是对应参数appetizer和course的位置顺序传递的，所以被叫作【位置参数】 ，
print('这也是最常见的参数类型。之前的神奇宝贝函数也有用到.')

def  menu(appetizer,course):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course+'\n')   #还记得转义字符\n吧，表示换行
menu('牛肉拉面','话梅花生')
menu('话梅花生','牛肉拉面')
#如果采用下面这种形式传递，就不需要理会参数位置
menu(course='牛肉拉面',appetizer='话梅花生')

#   2.  【默认参数】
# 回到这个食堂的故事。经营了一阵子之后，为了吸引更多的人流，你决定给每个顾客免费送上一份甜品绿豆沙，
# 这时候你就可以用到【默认参数】，注意：默认参数必须放在位置参数之后。

def  menu(appetizer,course,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course)
    print('一份甜品：'+dessert)
menu('话梅花生','牛肉拉面')
#因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。

# 如果一个参数的值是相对固定的，那么设置默认参数就免去了每次都要传递的麻烦。
# 但默认参数并不意味着不能改变，试试运行下列结果。

def menu(appetizer,course,dessert='绿豆沙'):
    print('一份开胃菜：'+appetizer)
    print('一份主食：'+course)
    print('一份甜品：'+dessert)
menu('话梅花生','牛肉拉面')
menu('话梅花生','牛肉拉面','银耳羹')
#银耳羹对应参数dessert



#   3. 【不定长参数】
# 后来呢，盛夏来袭，你觉得卖烧烤是个不错的主意。
# 但问题是每个人点的烤串数量都不同，你也不能限定死数量，
# 这时候【不定长参数】就能派上用场，即不确定传递参数的数量。
# 它的格式比较特殊，是一个星号*加上参数名，来看下面的例子。

def menu(*barbeque):
    print(barbeque)
menu('烤鸡翅','烤茄子','烤玉米')
#这几个值都会传递给参数barbeque

# 你会发现输出的是这样的结果：('烤鸡翅', '烤茄子', '烤玉米')，这种数据类型叫做元组(tuple)，
# 曾在第4关的必做练习中与你打过照面。我们就趁势来复习一下：
# 元组的写法是把数据放在小括号()中，它的用法和列表用法类似，
# 主要区别在于列表中的元素可以随时修改，但元组中的元素不可更改。
# 当然我们也可以先生成一个元组，再传入参数。上述代码等价于：

order=('烤鸡翅','烤茄子','烤玉米')     #元组的长度没有限制
def menu(*barbeque):
    print(barbeque)
menu(*order)

print('和列表一样，元组是可迭代对象，这意味着我们可以用for循环来遍历它，这时候的代码就可以写成：')


def menu(appetizer, course, *barbeque, dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主菜：' + course)
    print('一份甜品：' + dessert)
    for i in barbeque:
        print('一份烤串：' + i)
menu('话梅花生', '牛肉拉面', '烤鸡翅', '烤茄子', '烤玉米')

# 需要注意的是，这时候默认参数也需要放在不定长参数的后面，即dessert=’绿豆沙'要放在*barbeque后面，否则传递的值会对应不上。
print('现在请你重现上面的代码（自己手打哦~），注意参数的顺序，调用函数时可以换成你爱吃的食物')

def menu(starter,main,*soup,dessert = 'chocolate ice cream' ):
    print('starter: ' + starter)
    print('main: ' + main)
    print('dessert: '+ dessert)
    for i in soup:
        print('soup: ' +i)
menu('chicken feet', 'BBQ pork', 'pumpkin soup','tomato soup')

#      return语句
# 前面我们提到，return是返回值，当你输入参数给函数，函数就会返回一个值给你。
# 事实上每个函数都会有返回值，像我们之前学过的len()函数。
a=[1,2,3]
print(len(a))

# 当你把参数a放进len() 函数中，它返回来的是3这个数值（列表的长度）。
# 之后，我们就可以调用这个值，比如用print()函数打印出来或干点儿别的。

# 像常见的type()函数、数据类型转换函数，还有我们之前学过的bool()都是这样，会返回一个值。

# 而print()函数本身比较特殊，它在屏幕上显示完相关的文本内容就没了，并不会返回一个值给我们。
# 所以，它返回的是空值（None）。

# 在自定义函数的时候，我们就可以用return语句规定该函数要返回什么值给我们。带return语句的函数是这样的：

def niduoda(age):
    if age < 12:
        return '哈，是祖国的花朵啊'
    elif age < 25:
        return '哇，是小鲜肉呢'
    else:
        return '嗯，人生才刚刚开始'

print(niduoda(30))

# 可能你会觉得在这个例子中，直接用print不就行了吗，为啥还要用return呢？
# 还有，我们前面讲了那么多函数，好像都是省略了return的啊，比如刚讲的深夜食堂函数和神奇宝贝函数.
# 其实是因为在这些例题中，我们的函数功能都是第一时间把参数打印出来。
# 而在很多时候，当多个函数之间相互配合时，我们并不需要第一时间就将结果打印出来，
# 而是需要将某个返回值先放着，等到需要的时候再做进一步的处理。

# 下面来看个例子：
# 在我们关于爱情的天真幻想中，我希望我的梦中情人拥有XXX的脸蛋和XXX的身材。
# 现在需求如下：一、分别定义两个函数，参数为人名，能够返回字符串'XXX的脸蛋'和'XXX的身材'；
# 二、将上述两个函数的返回值拼接在一起之后，再打印出来。

# Kate's Answer:
def person(face,body):
    print('我希望我的梦中情人拥有'+face+'的脸蛋和'+body+'的身材')
person('都敏俊', 'Rain')

# 老师的答案：
def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
print('我的梦中情人：'+face('李若彤') +' + ' + body('林志玲'))

# 这只是一个非常简单的例子，在类似这种多个函数相互配合的代码中，我们就会非常需要return语句，
# 来帮我们先保留某个函数的返回值，等要用到的时候再调出来用。

# 但是这样的代码还有个问题，当我想多次调用函数的时候，就需要先复制print那行代码，再分别修改两个函数里的参数。
# 这样的操作既不简洁，也不优雅。就像这样：

def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
print('我的梦中情人：'+face('李若彤') +' + ' + body('林志玲'))
#要再次调用就要复制一遍，然后改参数
print('我的梦中情人：'+face('新垣结衣') +' + ' + body('长泽雅美'))

#  所以更常见的做法是：再定义一个主函数main()，参数调用前两个函数的返回值。
print('''老师先给出代码，你可以琢磨一下，主要思考第5行和第6行代码。''')

def face(name):
    return name + '的脸蛋'
def body(name):
    return name + '的身材'
def main(dream_face,dream_body):       #5
    return '我的梦中情人：' + face(dream_face) + ' + ' + body(dream_body)   #6
print(main('李若彤','林志玲'))
print(main('新垣结衣','长泽雅美'))

# main()函数内部分别调用了face()和body()函数，
# 参数dream_face和dream_body传递给了face()和body()函数的参数name，得到返回值，并打印。

# 现在，请你自己写一遍，相信印象会更深。尽量不要看原来的代码，参数名可以另取。

def face(name):
    return name + "'s face"
def body(name):
    return name + "'s body"
def person(dream_face,dream_body):
    return 'I want my bf to have ' + face(dream_face) + ' and '+ body(dream_body)
print(person('都敏俊','Rain'))
print(person('周兴哲','李敏镐'))



