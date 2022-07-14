#1.这是关于我们怎么选得分时刻的一个小想法
#2.pandas是一个库，可以读取csv或者xlsx文件（csv可以在excel里另存为csv），所以我们可以一个舞蹈对应一个csv（xlsx）文件，这样我们的使用者也就有了选择，
#他想跳什么舞，我们就导入哪个文件，文件里就是1，0这些数字，表示有没有这个分动作，一行对应某一秒
#3.最下面是我的预设格式，没用索引
#4.这是简单的我们可能用到的代码

#导入，他不是python自带的，所以要pip install 一下
import numpy as np
import pandas as pd

#读入
dance = pd.DataFrame(pd.read_csv('name.csv',header=1))
dance = pd.DataFrame(pd.read_excel('name.xlsx'))

#设置索引列
dance.set_index('id') #,这里的id是索引列名称
#按照索引列排序,就是说，如果我们想多加一个得分点，直接加在最后再调用函数排个序就行（。
dance.sort_index()
#按照特定列的值排序
dance.sort_values(by=['age'])

#loc函数按标签值进行提取，iloc按位置进行提取，ix可以同时按标签和位置进行提取
dance.iloc[1:] #先行后列，这里就是从第一行开始到最后一行的数据（从0开始计数），另一个小哥哥那里读取后，对于一秒的动作（那个poses的参数），就可以用这个传给我



![](https://github.com/SY-LG/AIDDR/blob/main/position_detection/1.png)
#那些三个点是省略号
#第一列是第几秒第几秒，从第二列向后，比如第二列，就表示第一个分动作是否存在
#每一行的意义就是某一秒的总动作
