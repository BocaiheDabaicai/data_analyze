import pandas as pd

students_data = {
    "001": {"姓名": "小陈", "考试1": 85, "考试2": 95, "考试3": 92},
    "002": {"姓名": "小李", "考试1": 91, "考试2": 92, "考试3": 94},
    "003": {"姓名": "小王", "考试1": 86, "考试2": 81, "考试3": 89},
    "004": {"姓名": "小张", "考试1": 79, "考试2": 89, "考试3": 95},
    "005": {"姓名": "小赵", "考试1": 96, "考试2": 91, "考试3": 91},
    "006": {"姓名": "小周", "考试1": 81, "考试2": 89, "考试3": 92}
}

students = pd.DataFrame(students_data)
print(students)
print(students.T)

students = students.T
# students["考试4"] = [72, 69, 79, 83, 82, 76]
students["考试4"] = pd.Series([72, 69, 79, 83, 82, 76], index=students.index)
print(students)

students.loc["007"] = ["小杨", 79, 82, 81, 69]
print(students)

print(students.drop(["006","007"],axis=0))
print(students.drop(["考试2","考试4"],axis=1))

bonus = pd.Series({"考试1": 2, "考试2": 3, "考试3": 2, "考试4": 5})
# print(bonus + students[["考试1","考试2","考试3","考试4"]])
print(bonus + students["考试1":"考试4"])

students["考试4"] = students["考试4"] + 10
print(students)