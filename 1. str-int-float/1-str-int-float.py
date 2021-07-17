# Python术语 中英对照表
# https://blog.csdn.net/qq_41420747/article/details/81534860

# 1. 字符串：
# 英文string，简写str。
# 只要是被【单/双/三引号】这层皮括起来的内容，不论那个内容是中文、英文、数字甚至火星文。只要是被括起来的，就表示是字符串类型。

#怎么样，字符串的使用是不是很简单？
#请你也来试一试，输出下面代码框中的内容，具体文本可直接复制粘贴。
# 【要点提示：1.文本用引号括住，创建字符串；2.将字符串赋值给变量；3. 使用4个print()函数，分别打印4个变量】。


slogan = '来呀，打我呀，你们抓不到我的！'
alarm = '保护我方鲁班七号！'
achieve = 'Double Kill!'
cooling = '10s'
print(slogan)
print(alarm)
print(achieve)
print(cooling)

# 2. 整数
# 英文为integer，简写做int。代码世界的整数，和我们数学课本中定义的一样：是正整数、负整数和零的统称，是没有小数点的数字。


print(499*561+10620-365)
print((5025-525)/100+18*17)

# 3. 运算优先级：Python世界的运算优先级，和我们平时的计算优先级是一样的。
# 代码【print((5025-525)/100+18*17)】，他的运算顺序是从左到右：最先计算括号里的【5025-525】。
# 然后将【5025-525】的结果除以100，第三步则计算【18*17】，最后将除法和乘法的结果相加。


#题目：
#假设我有一个15级李白，其基础物理攻击330，现在，为了让李白更强力，我在李白的红色铭文槽放了10个传承铭文，以提升其攻击力。
#穿上铭文后的李白，总物理攻击变为362。请问，每个传承铭文的攻击力为多少？[注]总物理攻击=基础攻击+每个铭文的攻击力*个数

print((362-330)/10)


# Note：10 Keyboard Shortcuts
# https://blog.logitech.com/2017/10/24/10-keyboard-shortcuts-every-designer-should-have-saved-to-memory/

# 4. 浮点数的英文名是float - 带小数点的数字，就是浮点数。
# 正如世界级C++大佬Herb Sutter说的：“世上的人可以分为3类：
# 一种是知道自己不懂浮点运算的；一种是以为自己懂浮点运算的；最后一种是极少的专家级人物，他们想知道自己是否有可能，最终完全理解浮点运算。”

print(0.55+0.3)

#这是因为，Python计算浮点数的方式与我们不一样。Python计算浮点数时，会先把0.55和0.3转化成二进制数
# 【注：二进制数由0和1表示，逢二进一】，如下列代码：
# 0.55(十进制) = 0.1000110011001100110011001100110011001100110011001101(二进制)
# 0.3(十进制) = 0.0100110011001100110011001100110011001100110011001101(二进制)
# 然后，这俩二进制数通过二进制法则运算后，再通过复杂的计算公式，将二进制结果转成十进制小数。
# 经过这两次转换，小数点后面就产生了多余的“尾巴”。这样，就造成了我们与程序计算结果的差异。

# 5. 数据拼接 "+"
hero = '亚瑟'
enemy = '敌方'
action = '团灭'
gain = '获得'
achieve = 'ACE称号'

print(hero+action+enemy+gain+achieve)


# 6. type()函数

print(type('查询的内容'))

#在type()函数的帮助下，我们知道了：原来字符串里面出了一个“奸细”整数。
# 难怪当时在终端区会给我报错说：数据类型不同呢。可是为什么不同类型的数据不能拼接在一起呢？
# 一句话：圈子不同不相融。

hero = '亚瑟'
enemy = '敌方'
action = '秒杀'
gain = '获得'
number = 5
achieve = 'Penta Kill'

# print(hero+action+number+enemy+gain+achieve)

#TypeError: must be str, not int

print(hero+action+str(number)+enemy+gain+achieve)
print(hero+action+'5'+enemy+gain+achieve)

#你看，我们是不是用两种不同的写法：str()函数和引号，输出了同一种结果？
#可是，为什么引号内我们使用的是数字，而不是变量名number呢？这是因为，当我们使用引号时，引号里的东西，都会被强制转换为字符串格式。

print(hero+action+'number'+enemy+gain+achieve)

#所以，如果我们把变量名number放进引号里后，被强制转换为字符串的，将是变量名number，而不是变量名代表的数字10000。


# 7. 数据转换

#负责转换数据类型的函数一共有3种：str()、int()和float()。

# a. str()函数能将数据转换成其字符串类型，不管这个数据是中文、数字、标点还是火星文，只要放到括号里。这个数据就能摇身一变，成为字符串类型。
#还有一种转换成字符串的方法，而且这种方法你已经学会了呢？那就是借用引号的帮助，

# b. int()函数: 将数据转换为整数类型的方法，将你需要转换的内容放在括号里就行，像这样：int(转换的内容)。

#计算出bug和hair这两个变量的和。【要点提示：1. int()函数转换数据类型；2. 运算符+计算；3. print()函数】
bug = '666'
hair = '0'
print(bug+hair)  #6660
print(int(bug)+int(hair))   #666

#不过对于int()函数的使用，大家要注意一点：只有符合整数规范的字符串类数据，才能被int()强制转换。
#别看它虽然只有一句话，但它其实带有三层含义：
# 首先，整数形式的字符串比如'666'和'0'，可以被int()函数强制转换。
# 其次，文字形式，比如中文、火星文或者标点符号，不可以被int()函数强制转换。
# 最后，小数形式的字符串，由于Python的语法规则，也不能使用int()函数强制转换。

print(int('3'))   #3
# print(int('3.8'))
# ValueError: invalid literal for int() with base 10: '3.8'

print(int(3.8))  #3
#上方的代码串，就是一条将浮点数3.8强制转换的语句。但是，为什么输出的结果是3呢？
#同我们平时对小数四舍五入的处理方法不同，int()函数会直接抹零，直接输出整数部分。

# c. float()函数
# float()函数也可以将整数和字符串转换为浮点类型。将需要转换的数据放在括号里，像这样：float(数据)。

#请补齐代码，将下列变量，转换为浮点类型，并打印出结果。【要点提示：print(float(数据))】

height = 183.5
weight = 79
age = '30'

print(float(height))
print(float(weight))
print(float(age))

#使用以下变量，输出这样一个结果人工智障说：3.8+1等于4。

word = '3.8'
number = 1
sentence = '人工智障说：3.8+1等于'

# print(sentence+str(int(int(word)+number)))
#ValueError: invalid literal for int() with base 10: '3.8'

print(sentence+str(int(number+int(float(word)))))
print(sentence+str(number+int(float(word))))

# 为了与整数【number = 1】进行计算，我们需要将字符串形式的【word = '3.8'】变为能做计算的数据类型。
# print(int('3.8')) ValueError: invalid literal for int() with base 10: '3.8'

print(int(float('3.8')))   #3

# print(float(变量))。经过转化后，我们的【word = '3.8'】已经成功脱去引号，成为了浮点型，可以做数学运算了。

print (HW1'''请运用所给变量，使用数据转换str()、int()、float()及数据拼接符号+，打印一句话：
脸黑怪我咯7张蓝票一个SSR都没有
其中，变量会在【书写代码】步骤里直接提供。

题目讲解

1.由于变量中有小数形式的字符串'7.8'，所以需要使用转换函数将此变量转换为浮点型
2.转换后使用int()函数取整
3.由于数据拼接需要变量为字符串形式，所以需要将变量转化为字符串类型
4.最后数据拼接，得出结果

书写代码

请运用所给变量，使用数据转换str()、int()、float()及数据拼接符号+，打印一句话： 
脸黑怪我咯7张蓝票一个SSR都没有''')

slogan = '脸黑怪我咯'
number = '7.8'
unit = '张'
sentence = '蓝票一个SSR都没有'

print(slogan+str(int(float(number)))+unit+sentence)

HW2
print(1+1.0)
print(type(1+1.0))
