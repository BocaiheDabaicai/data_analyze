# 数据分析 - 人工智能

1. 辅助编程
   
   - 解释编程概念
   
   - 解决报错问题
   
   - 找出代码运行不合理的地方【找BUG】
   
   - 给知识点出题目
   
   - 提升代码质量

2. 辅助数据分析
   
   - 帮忙提供原始数据
   
   - 什么值得分析，某个行业有什么关键指标
   
   - 数据有哪些地方不干净，该怎么处理
   
   - 从数据集中能得到什么结论

3. Jupyter整合AI
   
   - 进入`Jupyter AI`官网进行安装
   
   - 绑定`ChatGPT`的密钥
   
   - 使用

4. jupyter使用AI
   
   - 导入AI库
   
   - 设置`AI.api_key = "xxx-yyy...zzz"`
   
   - 读取AI`%load_ext jupyter_ai_magics`
   
   - 展示模型列表`%ai list`
   
   - 使用AI，`%%ai chatgpt`、换行并输入问题【名称可以使用`Name`、`Target`】
   
   - 清楚对话历史，`%%ai chatgpt -r`
   
   - 解释报错信息，并给出正确解答：`%%ai chatgpt`换行，并输入`{Err[错误出现的行数s]}`
   
   - 解释最近一次报错信息，`%%ai error chatgpt`
   
   - 解释可运行代码，`%%ai chatgpt`换行，输入解释以下代码：{In[代码的行数]}
   
   - 获得一个可以得到类似结果的函数，`%%ai chatgpt`，输入写一个函数，参数为数列的长度，使得函数能返回类似以下的数列：{Out[22]}
