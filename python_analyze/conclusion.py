# 导入numpy，并重命名
import numpy as np

# 生成一维、二维、三维数组，并定义数据类型
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], dtype=float)
a3 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], dtype=float)

# 实例化一个三行四列的数组，全部填充0
a4 = np.zeros((3, 4))
# 实例化一个三行四列的数组，全部填充1
a5 = np.ones((3, 4))
# 实例化一个一维数组，从10开始，25结束，每次增加5
a6 = np.arange(10, 25, 5)
# 实例化一个一维数组，从0开始，2结束，总共生成5个数字
a7 = np.linspace(0, 2, 5)
# 实例化一个两行两列的数组，全部填充7
a8 = np.full((2, 2), 7)
# 实例化一个四行四列的数组，主对角线填充1
a9 = np.eye(4)
# 实例化一个三行四列的数组，均随机填充0~1的数字
a10 = np.random.random((3, 4))
# 实例化一个三行四列的空数组
a11 = np.empty((3, 4))

# 保存文件，读取文件
np.save('test', a1)
np.load('test.npy')

# numpy的数据类型
print("""
int64,float32,complex,bool,object,string_,unicode_
""")

# 检查数组的形状
print(a10.shape)
# 检查数组的长度
print(len(a10))
print(len(a10[0]))
# 检查数组的维度
print(a10.ndim)
# 检查数组的元素个数
print(a10.size)
# 检查数组元素的数据类型以及名称
print(a10.dtype)
print(a10.dtype.name)
# 改变数组元素的数据类型以及名称
a10 = a10.astype(int)
print(a10.dtype)
print(a10.dtype.name)

a12 = np.full((3, 4), 3,dtype=float)
a13 = np.full((3, 4), 4,dtype=float)
a14 = np.full((4, 3), 2,dtype=float)
# 数组的加法运算
print(a12 + a13)
print(np.add(a12, a13))
# 数组的减法运算
print(a12 - a13)
print(np.subtract(a12, a13))
# 数组的乘法运算
print(a12 * a13)
print(np.multiply(a12, a13))
# 数组的除法运算
print(a12 / a13)
print(np.divide(a12, a13))
# 对a13的每个元素取e的次方
print(np.exp(a13))
# 对a13的每个元素开根号
print(np.sqrt(a13))
# 对a13的每个元素sin化
print(np.sin(a13))
# 对a13的每个元素cos化
print(np.cos(a13))
# 对a13的每个元素取对数
print(np.log(a13))
# 数组完成矩阵乘法
print(np.dot(a13,a14))

# 比较相等、大于小于
print(a13 == a12)
print(np.array_equal(a13, a14))
print(a13 < 2)

# 聚合函数【矩阵求和、矩阵最小值、矩阵最大值（行方向上）、累计和（列方向上）、平均值、标准差】
print(a14.sum())
print(a14.min())
print(a14.max(axis=0))
print(a14.cumsum(axis=1))
print(a14.mean())
print(np.std(a14))

# 复制矩阵【创建视图、复制矩阵】
print(a14.view())
print(a14.copy())

# 排序矩阵
a15 = np.array([2,34,5,78,9,1])
a15.sort()
print(a15)

# 选取值
print(a14[1,2])
print(a15[2])
# 切片【一维切片、二维切片（0到2行的第1列）、二维切片（直到第2行）、二维切片（第1行）】
print(a15[0:2])
print(a14[0:2,1])
print(a14[:2])
print(a14[1,...])
# 布尔判断
print(a15[a15>10])

# 矩阵转置
print(a14)
print(a14.T)
print(np.transpose(a14))

# 多维数组转换为一维数组
print(a14.ravel())
# 重塑维度
print(a15.reshape(2,-1))

# 重塑、添加、删除元素【需要重新赋值给原矩阵才能生效】
print(np.resize(a15,(2,8)))
print(np.append(a15,98))
print(np.insert(a15,2,300))
print(np.delete(a15,1))

# 联合函数
print(np.concatenate((a1,a15),axis=0))
# 堆叠函数
a16 = np.vstack((a1,np.array([6,4,2,3,1])))
a17 = np.hstack((a1,np.array([6,4,2,3,1])))
a18 = np.hstack((a1,np.array([6,4,2,3,1])))

print(a16)
print(a17)
print(a18)

# 分割矩阵
print(np.hsplit(a15,2))
print(np.vsplit(a15,2))




# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(a6)
# print(a7)
# print(a8)
# print(a9)
# print(a10)
# print(a11)
