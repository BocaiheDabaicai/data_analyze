import pandas as pd

# 创建一维数组
series1 = pd.Series([1,2,3,4,5])
# 创建一维数组，带自定义序号
series2 = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
# 创建二维数组
data1 = {
    "data1":['asd','sad','dsd'],
    "data2":[1,2,3],
    "data3":[True,False,False],
}
data_frame1 = pd.DataFrame(data1,columns=["data1","data2","data3"])

# 写入数据和读取数据
data_frame1.to_csv("data1.csv")
data_frame2 = pd.read_csv("data1.csv",header=None,nrows=5)
# 从数据库中写入数据和读取数据
# from sqlalchemy import create_engine

print(series1)
print(series2)
print(data_frame1)
print(data_frame2)

# 寻求帮助
# help(pd.Series.loc)

# 选择数据
print(series2['b'])
print(data_frame1[1:])
# 通过位置查询数据
# iloc 可以查元素块、也可以查元素单元格
print(data_frame1.iloc[[0],[0]])
print(data_frame1.iloc[0,0])
print(data_frame1.iat[0,0])
# 通过标签查询数据
# loc 可以查元素块、也可以查元素单元格
print(data_frame1.loc[[0],['data1']])
print(data_frame1.loc[0,'data1'])
print(data_frame1.at[0,'data1'])
# 通过布尔值查询数据
print(series1[series1 > 2])
print(series1[(series1 > 3) | (series1 < 2)])
print(data_frame1[data_frame1['data2'] > 2])
# 设置值
series2['b'] = 3
print(series2)

# 删除数据
print(series2.drop(['b']))
print(data_frame1.drop(['data1'],axis=1))

# 数据排列
print(data_frame1.sort_index())
print(data_frame1.sort_values(by='data3'))
print(data_frame1.rank())

# 获取形状信息
print(data_frame1.shape)
# 获取序列信息
print(data_frame1.index)
# 获取列头信息
print(data_frame1.columns)
# 获取信息
print(data_frame1.info())
# 获取数量信息
print(data_frame1.count())
# 数组求和
print(data_frame1.sum())
# 数组累积求和
print(data_frame1.cumsum())
# 数组最大值、数组最大值序列
print(data_frame1.max())
print(data_frame1.idxmax())
# 数组最小值、数组最小值序列
print(data_frame1.min())
print(data_frame1.idxmin())
# 数组信息
print(data_frame1.describe())
# 数组平均值
print(data_frame1['data2'].mean())
# 数组中位数
print(data_frame1['data2'].median())

# 函数应用
f = lambda x : x*2
print(data_frame1.apply(f))
print(data_frame1.map(f))

# 数据计算
series3 = pd.Series([-1,-1,-1,-1],index=['a','b','c','d'])
print(series2 + series3)
# 数据计算，填充值
print(series2.add(series3,fill_value=0))
print(series2.sub(series3,fill_value=0))
print(series2.multiply(series3,fill_value=0))
print(series2.divide(series3,fill_value=0))