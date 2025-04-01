# 数据分析流程

1. 数据读取
   
   - 将数据读入Jupyter，以便后续的工作可以顺利开展

相关代码：

```python
import pandas as pd

original_data = pd.read_csv("e_commerce.csv")
```

> `pd.read_csv`：读取CVS文件

2. 评估数据
   
   - 结构，保证结构的整齐度，即每列是一个变量、每行是一个观察值、每个单元格是一个值，每列的数据类型相同，每行都是类型相同的数据，每个单元格都是一个单一的值
   
   - 内容，保证数据的干净度，即消除丢失数据、重复数据、无效数据等等，判断是否要清除不符合结构的列、行
   
   - 流程，评估数据整齐度、评估数据干净度、评估缺失数据、评估重复数据、评估数据不一致的情况（两种数据表示同一个意思）、评估无效或错误数据

相关代码：

```python
original_data.sample(10)
original_data.info()
original_data[original_data["Description"].isnull()]
cleaned_titles.query("imdb_score.isnull()")
cleaned_titles.duplicated().sum()
original_data["Country"].value_counts()
original_data.describe()
```

> `original_data.sample(10)`：抽样检查数据
> 
> `original_data.info()`：查看每列数据的统计值
> 
> `original_data[original_data["Description"].isnull()]`：查看`Description`列为空的数据
> 
> `cleaned_titles.query("imdb_score.isnull()")`：查看`imdb_score`列为空的数据
> 
> `cleaned_titles.duplicated().sum()`：统计重复数据的数量
> 
> `original_data["Country"].value_counts()`：统计`Country`列不同数据出现的次数
> 
> `original_data.describe()`：查看列表的数据值一般计算表（得到平均值、中位数等等结果）

3. 清理数据
   
   - 通过数据评估得到的结果，对流程中出现不合规的情况进行处理
   
   - 开始操作清理不合规的数据

相关代码：

```python
cleaned_titles['genres'] = cleaned_titles['genres'].apply(lambda s: eval(s))
cleaned_titles = cleaned_titles.explode("genres")
pd.to_datetime(cleaned_titles["release_year"], format='%Y')
cleaned_credits["person_id"].astype("str")
cleaned_titles = cleaned_titles.dropna(subset=["imdb_score"])
cleaned_titles.query('genres != ""')
cleaned_titles["production_countries"] = cleaned_titles["production_countries"].replace({"Lebanon": "LB"})
credits_with_titles = pd.merge(cleaned_credits, cleaned_titles, on="id", how="inner")
```

> `lambda s: eval(s)`：把字符串转换成表达式并返回
> 
> `cleaned_titles.explode("genres")`：把`genres`列的列表拆分成一个个单行的值
> 
> `pd.to_datetime(cleaned_titles["release_year"], format='%Y')`：把`release_year`的列转换成年的格式
> 
> `cleaned_credits["person_id"].astype("str")`：把`person_id`列的数据转换为字符串格式
> 
> `cleaned_titles.dropna(subset=["imdb_score"])`：移除`imdb_score`列为空的每一行数据
> 
> `cleaned_titles.query('genres != ""')`：查询`genres`不为空的每一项数据
> 
> `cleaned_titles["production_countries"].replace({"Lebanon": "LB"})`：将`production_countries`列里的`Lebanon`替换为`LB`
> 
> `pd.merge(cleaned_credits, cleaned_titles, on="id", how="inner")`：合并`cleaned_credits`和`cleaned_titles`，以`id`作为合并键，方式是`inner`方式。【how：inner(取两个表的交集)、outer(取两个表的并集)、left(保留左表的结果)、right(保留右表的结果)】

groupby方法
