# 第8课- 如何解决问题

#   瓶颈1：知识学完就忘

#  1. 【用法查询笔记】
# 虽然课堂上我们也是以案例带出知识点，但老师还是建议你能在课后制作一份不同于课堂的案例，
# 写出“代码含义”和“实际运行结果”的注释，这样才能加深对知识的第一印象，需要的时候才想得起笔记在哪。

#   2. 【深度理解笔记】
#   重在“理解”，所以笔记内容主要是记录对知识的理解。
# 可以看到，如果说【用法查询笔记】解决的是“知识点是什么”的问题，那么【深度理解笔记】更侧重解决“为什么要用”以及“怎么用这个知识点”的问题。
# 通常来说，我们需要回答
# “什么时候需要用到这个知识？
# 这个知识有什么常见用法？
# 这个知识和其他知识有什么不同？”之类的问题，并写下自己的思考过程。

#    3. 【用法查询笔记】 vs  【深度理解笔记】
#  如果你学Python学到“走火入魔”的话，你会发现【深度理解笔记】和【用法查询笔记】本质上就是一个“字典嵌套列表”，
#  其中【深度理解笔记】是键，【用法查询笔记】是值。

#   4. 知识管理

# 基于这个结构，我们的知识框架就搭建起来了。因为我们有【深度理解笔记】，
# 所以在解决一个编程问题的时候，我们可以轻易想到需要用到哪块知识，接着就可以去【用法查询笔记】里寻找相关的知识细节和具体案例，形成解题的思路。

# 在解决了问题之后，我们还可以把一些特别典型的案例，继续补充在【用法查询笔记】，是不是有点像以前上学时我们所做的错题集。
# 同样地，在解题的过程中，我们可能会专门搜索并自学一些额外知识，比如random模块（里面有许多随机函数）的使用方法，也可以一并记录在笔记里。

#   瓶颈2：缺乏解题能力

# 打印出九九乘法表
# step1
# 分别用for循环打印出九九乘法表的第二行和第三行吧，

#题目要求：用两次for循环在终端打印出：
# 1 X 2 = 2  2 X 2 = 4
# 1 X 3 = 3  2 X 3 = 6  3 X 3 = 9

for i in range(1,3):
    print(str(i) + ' X 2 = ' + str(i*2))

for i in range(1,4):
    print(str(i) + ' X 3 = ' + str(i*3))

# 你会发现字符串只能与字符串用'+'号拼接，要拼接数字的话还得先用str()转换，煞是麻烦。
# 所以用我们刚才所说的格式化字符串处理会轻松得多。
# 这时，之前讲的【用法查询笔记】也能派上用场了。


for i in range(1,3):
    print('%d X 2 = %d' % (i,i*2))
for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3))

# 但是，运行后你会发现这样写的话每一个等式都会换行
# 现在我们希望print出来的东西不换行，那怎么实现呢？
# 你可能突发奇想，想到用拼接一个空字符串来实现。

for i in range(1,3):
    print('%d X %d = %d' % (1,2,1*2) +'  '+ '%d X %d = %d' % (2,2,2*2))

# 但这样写且不说麻烦，也会让循环发挥不了作用。
# 正如我反复强调的，很多零碎的知识点老师无法都直接教给你们，需要我们碰到实际问题的时候再去补充，这时就需要我们发挥“搜索大法”，主动搜索新知识。
# 原来print()函数里有个参数'end'是用来控制换行行数和结尾字符，
# 比如说，你可以运行下列代码，感受一下，留意'end='后面的内容：

print('hello',end='')
print('world')
print('hello',end='  ')
print('world')
print('hello',end='!')
print('world')

for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2),end = '  ')
for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3), end = '  ')

# 但是这样子会发现，天啊真是磨人的小机精，现在所有的等式又都挤在一行了 = =。
# 别愁，问题很好解决，这里就教给大家一个小技巧，用print('')

print('来控制换行，请你直接运行下下面的代码看一看：')

for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2),end = '  ')
print('')   #用来换行
for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3),end = '  ')
print('')     #用来换行

print('可算输出了我们想要的结果了，那么依葫芦画瓢，把所有的等式放在一起就是：')

for i in range(1,2):
    print( '%d X %d = %d' % (i,1,i*1) ,end = '  ' )
print('')

for i in range(1,3):
    print( '%d X %d = %d' % (i,2,i*2) ,end = '  ' )
print('')

for i in range(1,4):
    print( '%d X %d = %d' % (i,3,i*3) ,end = '  ' )
print('')

for i in range(1,5):
    print( '%d X %d = %d' % (i,4,i*4) ,end = '  ' )
print('')

for i in range(1,6):
    print( '%d X %d = %d' % (i,5,i*5) ,end = '  ' )
print('')

for i in range(1,7):
    print( '%d X %d = %d' % (i,6,i*6) ,end = '  ' )
print('')

for i in range(1,8):
    print( '%d X %d = %d' % (i,7,i*7) ,end = '  ' )
print('')

for i in range(1,9):
    print( '%d X %d = %d' % (i,8,i*8) ,end = '  ' )
print('')

for i in range(1,10):
    print( '%d X %d = %d' % (i,9,i*9) ,end = '  ' )
print('')

# 我们可以看到以上代码是有规律的三行结构，同一结构重复了九次，这提醒我们可以再用一层循环嵌套，来彻底解决重复劳动。
# 我们再来看看九九乘法表，可以发现行数是固定的，范围是range(1,10)，而列数（等式）则是逐行加一，即第N行就有N个等式。
# 基于此和上述已完成的代码，你想到了如何用两层for循环消灭重复吗？
print('请尝试一下，最外层的循环已经替你写好。（最终代码可以控制在四行）')

for i in range(1,10):
    for j in range(1,i+1):
        print( '%d X %d = %d' % (j,i,i*j),end = '  ' )
    print('  ')

print('当然，解法不是唯一的，有些同学的答案可能是这样，也能达到相同效果：')

for i in range (1,10):
    for j in range(1,10):
        print('%d X %d = %d' % (j,i,i*j),end = '  ')
        if i==j:
            print('')
            break

print('如果用while循环，也是可以的，不过对比一下，是不是还是第一种解法的代码最简洁呢～')

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d X %d = %d' % (j,i,i*j),end = '  ')
        j += 1
    print('')
    i += 1

print('''练习目标：
我们会通过今天的作业，掌握列表的两个新运用：合并列表和列表排序。

练习要求：
一次测评中，老师将 学习小组A 和 学习小组B 的测评成绩(满分 100 分)从低到高记录放进两个列表：
A=[91, 95, 97, 99]，B=[92, 93, 96, 98] 。
现在，老师想将两个小组的成绩合并为一个列表，并按照从低到高的顺序排序，你能帮老师完成吗？


合并列表-1

分析问题，明确结果
我们的问题是：将两个列表合并起来，并按照从低到高的顺序排序，要得到问题的结果，我们还需要借助打印函数看看我们合并的是否正确。

思考要用到的知识&思考切入点
增加列表的内容与合并列表的含义相同，所以我们可以使用append作为解题的切入点，请你试试！


合并列表-2

#上网搜索新知识&找到新的切入点

好了。你已经完成了第一个需求：合并列表。不过，有没有发现，这个代码还是比较冗余的。有没有更简单的方法呢？请你自己上网搜索一下
python 合并两个列表，看看是否有更简单的方法，学会后再回来继续做作业吧。
请你根据新学到的知识，简化代码。

两个提示：
1.如果你直接将 list2 合并到 list1 上，那就无法做到只看A组的成绩，所以，最好再建一个列表来合并两组的成绩；
2.合并后不要忘了打印一下合并的列表，看看结果是否正确。

列表排序

主动搜索，掌握新知
老师鼓励你自己去探寻解决问题的方法，上网搜索一下列表的排序方法吧。

有了知识，再写代码
请你根据搜索到的知识，完成列表的排序，再将其打印出来。''')

# 合并列表
# 使用append()函数
list1 =  [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]
for i in list2:
    list1.append(i)
print(list1)
list1.sort()
print(list1)

# or 使用extend()函数
list1 =  [91, 95, 97, 99]
list2 =  [92, 93, 96, 98]
list3 =list1
list3.extend(list2)
print(list3)
list3.sort()
print(list3)

print('''练习介绍

练习目标
这个练习，是建立在上一个练习之上，用代码帮老师完成更多的成绩处理工作。

练习要求
上一个练习中，我们完成了两组成绩的合并和排序。
不过，老师有了新的需求：想知道两组的平均分，以及把低于平均分的成绩也打印出来。
所以，在这个练习中，我们会帮老师计算出两组的平均分，并挑出那些在平均分之下的成绩。

明确结果，思考知识和切入点

你可以尝试自己写下代码，在思路卡住的时候，查看“步骤提示”。

参考代码-1
看下参考代码，并运行一下，看得出的结果是否和你的代码一样。
明确结果，找新知识和切入点


第二种 解题三连击：
1.目前我们想要的结果是：求平均值和判断比较；
2.我们可以去找的新知识有：Python 求平均值；
3.我们的切入点：请你通过搜索，找到更简单的求平均值的方法，来改造代码。

参考代码-2

你是否找到了这个库？
这其实是Python强大的原因之一：
有很多可以调用的库，可以让我们又好又快地做成一些操作。''')

# 方法一：通过for循环求出平均值并判断
scores1 =  [91, 95, 97, 99, 92, 93, 96, 98]
sum = 0
scores2 = []

for score in scores1:
    sum = sum + score  # 叠加成绩
    average = sum/len(scores1)   # 用len()函数计算出总人数，即列表的元素数量
print('平均成绩是：{}'.format(average))

for score in scores1:
    if score < average:  # 判断是否小于平均值
        scores2.append(score)
        continue
print(' 低于平均成绩的有：{}'.format(scores2))


# 方法二，通过mean()函数，直接求出平均值
import numpy as np

scores1 =  [91, 95, 97, 99, 92, 93, 96, 98]
scores2 = []

average = np.mean(scores1)  # 一行解决。
print('平均成绩是：{}'.format(average))

for score in scores1:
    if score < average:
        scores2.append(score)
        continue
print(' 低于平均成绩的有：{}'.format(scores2))




print('''# Import NumPy on PyCharm
ctrl-alt-s
click "project:projet name"
click project interperter
double click pip
search numpy from the top bar
click on numpy
click install package button''')