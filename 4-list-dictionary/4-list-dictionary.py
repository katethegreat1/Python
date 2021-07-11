#第4课 列表、字典、元组

#这一关，我们就会接触两种新的数据类型——列表和字典，
# 你会发现，它们比我们学过的“整数、浮点数、字符串”更加高级，更有“包容性”。

#一个列表需要用中括号[ ]把里面的各种数据框起来，里面的每一个数据叫作“元素”。每个元素之间都要用英文逗号隔开。
#现在请你创建一个列表名为list1的列表，列表里有三个元素：'小明'、18、1.70，并将其打印出来：

list=['小明',18,1.70]      # not list=([***])
print(list)

#知识点1：列表很包容，各种类型的数据（整数/浮点数/字符串）无所不能包。

#  1. 从列表提取单个元素

#知识点2：偏移量。列表中的各个元素，好比教室里的某排学生那样，是有序地排列的. 每个元素都有自己的位置编号（即偏移量）。
# OFFSET（偏移量）的特点：
#偏移量就是一个相对的位置。
#The first character in a string has an offset of 0, because it is zero characters from the start.

#偏移量(offset)就是字符的索引值(index value)。
#1.偏移量是从0开始的，而非我们习惯的从1开始；2.列表名后加带偏移量的中括号，就能取到相应位置的元素。

# 假如你现在要喊小明来回答问题，用代码怎么写呢？请补充下列代码，利用列表的偏移量来打印出'小明'这个元素。

list=['小明',18,1.70]
print([0])    # wrong!


list=['小明',18,1.70]
print(list[0])   #小明

print(list[:2])  #['小明', 18]
print(list[0:2])    #['小明', 18]

#  2. 从列表提取多个元素

list2 = [5,6,7,8,9]

print(list2[:])
# 打印出[5,6,7,8,9]
print(list2[2:])
# 打印出[7,8.9]
print(list2[:2])
# 打印出[5,6]
print(list2[1:3])
#打印出[6,7]
print(list2[2:4])
#打印出[7,8]

#!!! 我们要注意一个细节：
# 偏移量Offset取到的是列表中的元素 items，而切片Slice则是截取了列表的某部分，所以还是列表.

students = ['小明','小红','小刚']
print(students[2])      # 小刚
print(students[2:])     # ['小刚']

#    3. 给列表增加/删除元素

#教导主任突然领了一个新学生，说是转校生，要插到你们班。
#这时，我们就需要用到append()函数给列表增加元素，append的意思是附加，增补。

students = ['小明','小红','小刚']
students.append('Kate')                                # NOT students.append['Kate']
print(students)

# 将'小红'从列表中删除，并打印出来：（语法是：del 列表名[元素的索引]）

students = ['小明','小红','小刚','Kate']
del students[1]
print(students)

# 事实上del语句非常方便，既能删除一个元素，也能一次删除多个元素（原理和切片类似，左取右不取）。
students = ['小刚','小红','小刚','Kate']
del students[1:3]
print(students)                #['小刚', 'Kate']


#     数据类型：字典

#variable={Key1:value1,key2:value2}   # item=key:value

#这次期中考呢，小明、小红、小刚分别考了95、90和90分。
#假如我们还用列表来装数据的话，我们需要新创建一个列表来专门放分数，而且要保证和姓名的顺序是一致的，很麻烦。
#所以类似这种名字和数值（如分数、身高、体重等）两种数据存在一一对应的情况，用第二种数据类型——“字典”（dictionary）来存储会更方便。

students = ['小明','小红','小刚']             # list
scores = {'小明':95,'小红':90,'小刚':90}          #dictionary

#仔细看下，字典和列表有3个地方是一样的：1.有名称；2.要用=赋值；3.用逗号作为元素间的分隔符。
#而不一样的有两处：1.列表外层用的是中括号[ ]，字典的外层是大括号{ }
# 2.列表中的元素items是自成一体的，而字典的元素是由一个个键值对构成的，用英文冒号连接。
# 如'小明':95，其中我们把'小明'叫键（key），95叫值(value)。
#这样唯一的键和对应的值形成的组合，我们就叫做【键值对】，上述字典就有3个【键值对】：'小明':95、'小红':90、'小刚':90

#如果不想口算，我们可以用len()函数来得出一个列表或者字典的长度（元素个数），括号里放列表或字典名称。
print(len(students))
print(len(scores))

#字典中的键具备唯一性，而值可重复。也就是说字典里不能同时包含两个'小明'的键，但却可以有两个同为90的值
#Duplicates Not Allowed - Dictionaries cannot have two items with the same key.

#Example
#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)   #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


#   1.  从字典中提取单个元素
#我们尝试将小明的成绩从字典里打印出来。这就涉及到字典的索引，和列表通过偏移量来索引不同，字典靠的是键。
scores = {'小明': 95, '小红': 90, '小刚': 90}
print(scores['小明'])

#这便是从字典中提取对应的值的用法。和列表相似的是要用[ ]，不过因为字典没有偏移量，所以在中括号中应该写键的名称，即字典名[字典的键]。


#    2.  给字典增加/删除元素
#Changeable
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

scores = {'小明': 95, '小红': 90, '小刚': 90}
del scores['小明']
scores['Kate']=100
print(scores)

#！！！ 删除字典里键值对的代码是del语句del 字典名[键]，而新增键值对要用到赋值语句字典名[键] = 值。

#那么，请你把小刚的成绩改成92分吧。对了，新来的小美也考了，得了85。请你对字典里进行修改和新增，然后将整个字典都打印出来。
scores = {'小明': 95, '小红': 90, '小刚': 90}
scores['小刚']=92
scores['小美']=85
print(scores)

# List vs Dics

#不同点:列表中的元素是有自己明确的“位置”的，所以即使看似相同的元素，只要在列表所处的位置不同，它们就是两个不同的列表。

students1 = ['小明','小红','小刚']
students2 = ['小刚','小明','小红']
print(students1 == students2)               #  False

scores1 = {'小明':95,'小红':90,'小刚':100}
scores2 = {'小刚':100,'小明':95,'小红':90}
print(scores1 == scores2)                     # True

#而字典相比起来就显得随和很多，调动顺序也不影响。因为列表中的数据是有序排列的，而字典中的数据是随机排列的。
#这也是为什么两者数据读取方法会不同的原因：列表有序，要用偏移量定位；字典无序，便通过唯一的键来取值。

#!!!Ordered or Unordered?
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# 第一个共同点：在列表和字典中，如果要修改元素，都可用赋值语句来完成。看一下代码：

list1 = ['小明','小红','小刚','小美']
list1[1] = '小蓝'
print(list1)

dict1 = {'小明':'男'}
dict1['小明'] = '女'
print(dict1)

# 第二个共同点其实之前已经略有提及，即支持任意嵌套。除之前学过的数据类型外，列表可嵌套其他列表和字典，字典也可嵌套其他字典和列表。

# 第一种情况：列表嵌套列表。你在班级里成立了以四人为单位的学习小组。这时，列表的形式可以写成：

#从列表中取出小芳，并打印出来吧。

students = [['小明','小红','小刚','小美'],['小强','小兰','小伟','小芳']]
print(students[1][3])     # 小芳

#第二种情况：字典嵌套字典。

#和列表嵌套列表也是类似的，需要一层一层取出来，比如说要取出小芳的成绩，代码是这样写：

scores = {
    '第一组':{'小明':95,'小红':90,'小刚':100,'小美':85},
    '第二组':{'小强':99,'小兰':89,'小伟':93,'小芳':88}
    }
print(scores['第二组']['小芳'])


#  列表和字典相互嵌套的情况，可以将代码和注释结合起来看。

# 最外层是大括号，所以是字典嵌套列表，先找到字典的键对应的列表，再判断列表中要取出元素的偏移量
students = {
    '第一组':['小明','小红','小刚','小美'],
    '第二组':['小强','小兰','小伟','小芳']
    }
print(students['第一组'][3])
#取出'第一组'对应列表偏移量为3的元素，即'小美'

# 最外层是中括号，所以是列表嵌套字典，先判断字典是列表的第几个元素，再找出要取出的值相对应的键
scores = [
    {'小明':95,'小红':90,'小刚':100,'小美':85},
    {'小强':99,'小兰':89,'小伟':93,'小芳':88}
    ]
print(scores[1]['小强'])
#先定位到列表偏移量为1的元素，即第二个字典，再取出字典里键为'小强'对应的值，即99。
