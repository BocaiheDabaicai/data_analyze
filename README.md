# Python、数据分析、AI大模型训练营

- 2025年2月8日开坑
  
  目前先回顾学习python

---

## 数据分析

- Juputer

官方安装地址：[Project Jupyter | Installing Jupyter](https://jupyter.org/install)

LaTex数学表达式：

$x=1+3$

$x-y$

$x^3$

$log_210$

$x\times y$

$x \div y$

$S_{sdjkkkw}$

$\sum(x^2+y^2)$

$\sqrt[3]x$

$\sqrt[3]{x^2+y^3-2}$

$\sqrt[3]xy^2$

$\frac{x+y}{x-y}$

- NumPy【科学和工程领域】，数据处理效率极高

- Pandas【构建在NumPy的基础之上】，更加完善

## 数据获取

- 公司数据获取，通过数据库获得

- 外部数据获取，下载、API、爬虫
  
  - 下载，良好的数据集，飞浆数据集、天池数据集、和鲸社区【很高效】
  
  - API，应用程序编程接口，客户端发送请求、服务器发送响应【高效】
  
  - 爬虫，对网页源代码的获取、解析【不要爬取公民隐私数据、受著作权保护的内容、国家事务、国防建设、尖端科技】【低效】

- JSON，通用编程时更加适合

- CSV，数据分析师更青睐的数据格式，通常有GB的大小

> sqlite也是一个轻内容的数据格式

## 数据清洗

- 数据由结构和内容组成

- 错误数据类型：数据丢失、数据重复、数据形式不一致、数据无效或错误

- 错误处理方法：
  
  - 获取开头或结尾的N行检查`.head() .tail() .sample()`
  
  - 评估数据丢失`.info() .isnull() .isnull().sum()`【有TRUE就表示有空缺值】，提取丢失的数据行`scores[scores["考试3"].isnull()]`
  
  - 评估重复数据`.duplicated() .duplicated(subset=["学号","性别"])`，提取数据重复的行`scores[scores.duplicated(subset=["学号","性别"])]`
  
  - 评估数据形式不一致`.value_counts()`
  
  - 评估无效或错误数据`.sort_values() .describe()`

- 数据清洗的流程
  
  - 规范结构，每列的数据规范、每行的数据规范、每个单元格规范
  - 清理索引和列名，`.rename(index={},columns={},inplace=True)`，排序`.sort_index(inplace=True)`
  - 清理混乱数据，`.str.split("/",expand=True)`
  - 清理脏数据，`.fillna(0) .dropna(subset="工资") .drop_duplicates(keep="last") astype("int" "str" "float" "bool")`
  - 保存干净数据，`.to_csv("路径",set_index=False)`



66
