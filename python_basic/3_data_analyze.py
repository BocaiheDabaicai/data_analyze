import pandas as pd

# DataFrame 练习一
name = pd.Series(["小陈","小李","小王","小张","小赵","小周"],index=["001","002","003","004","005","006"])
gender = pd.Series(["女","女","男","男","女","男"],index=["006","005","004","003","002","001"])
height = pd.Series([172.5,168.0,178.2,181.3,161.7,155.9],index=["001","002","003","004","005","006"])

students = pd.DataFrame({"name":name,"gender":gender,"height":height})
print(students)

print(students.index)
print(students.columns)
print(students.T)

# 第二种方法更通用
print(students.height)
print(students["height"])

print(students[["gender","height"]])

print(students.loc["001"])
print(students.loc["003":"005"])

print(students.loc["005","height"])
print(students.loc[["003","005"],["name","height"]])

# 选定列，并圈定输出数据
print(students.loc[["003","005"],"name":"height"])
print(students.loc[["003","005"],"name"])
print(students.loc[["003","005"],:"height"])
print(students.loc[["003","005"]])

print(students["height"]>165.0)
print(students["gender"]=="女")
print(students[(students["height"]>165.0) & (students["gender"]=="女")])

print(students.head(5))