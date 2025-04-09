# 数据可视化

1. 统计学基础
   
   - 描述，对数据提供的特征进行概述
   
   - 数据
     
     - 分类数据，类别有限的数据
       
       - 定序数据，数据有顺序
       
       - 定类数据，数据没有顺序
     
     - 数值数据，可以进行数值运算和统计分析的数据【分析的重点】
       
       - 离散数据，数据只能以整数、自然数作为单位
       
       - 连续数据，数据没有最小的表示单位
       
       - 分析维度
         
         - 集中趋势【平均数、中位数、众数】
         
         - 离散趋势【极差（最大值-最小值）、方差/标准差（方差开根号 = 标准差；方差 = （各个数据 - 平均数）的平方 / 数据的个数）、四分位距（第三四分位数 - 第一四分位数）】
           
           - pandas里的`.var()`方法计算方差
           
           - pandas里的`.std()`方法计算标准差
           
           - 四方位距的计算：`.quantile(0.75) - .quantile(0.25)`
         
         - 分布形状【直方图、正态分布、正偏态/右偏态分布（看长尾巴的位置判断）、负偏态/左偏态分布】
           
           - 直方图：`.plot(kind='hist')`

2. 可视化数据
   
   - 一维数据图形
     
     - 直方图，用来表示数据的分布，用来表示一维数据的频率分布
     
     - 密度图，更精细化地表达数据的走向
     
     - 箱型图，表示数据的上界、下界、第一四分位数、中位数、第三四分位数、异常值，观察数据是否对称、紧密
     
     - 小提琴图，由箱型图和密度图组成，既可以观察数据的走向，也可以观察数据是否对称、紧密
   
   - 二维数据图形
     
     - 散点图，用来展示两个数据变量之间的关系，得出数据之间的相关性【两个数值变量】
     
     - 折线图，用来展示两个数据变量之间的趋势变化【两个数值变量】
     
     - 条形图，用来展示一个分类变量的数值变量，而直方图使用一个数值范围得到的数值变量，条形图的条柱分隔着不同的分类变量，直方图的条柱分割着不同的数据范围【一个分类变量、一个数值变量】
     
     - 饼图，用来展示各个分类变量之间的数值变量所占的比例
     
     - 气泡图，用来展示多个数据变量之间的关系【两、三个数值变量、一个分类变量】
     
     - 热力图，通过颜色来展示不同数据之间的差异【一个颜色变量、两个分类变量】
     
     - 多个数据变量的情况，那么可以在图形上绘制多种不同类型的点、线或条柱
     
     - 多个图像堆叠，也就可以明白不同数值的图像之间的差异

3. 绘制图表
   
   - matplotlib
     
     - 安装指令：`pip install matplotlib`
     
     - 常用模块：`import matplotlib.pyplot as plt`
   
   - seaborn【封装版的`matplotlib`】
     
     - 安装指令：`pip install seaborn`
     
     - 常用模块：`import seaborn as sns`
   
   - 操作流程
     
     - 绘制一维图表
       
       - `sns.histplot(s1)`：绘制一维直方图
       
       - `sns.kdeplot(s1)`：绘制一维密度图
       
       - `sns.boxplot(s1)`：绘制一维箱型图
       
       - `sns.violinplot(s1)`：绘制小提琴图
       
       - `sns.histplot(df1,x="bill_length_mm")`：绘制一维直方图，`dataframe`传入，并选择其中一列进行绘制
     
     - 绘制二维图表
       
       - `sns.scatterplot(df1,x="total_bill",y="tip")`：绘制二维散点图，x轴为总账单，y轴为小费，分析总账单与小费之间的关系
       
       - `sns.scatterplot(x=df1["total_bill"],y=df1["tip"])`：绘制二维散点图，第二种绘制散点图的方式
       
       - `sns.lineplot(df2,x="year",y="passengers")`：绘制二维折线图
       
       - `sns.barplot(df2,x="year",y="passengers",estimator=np.mean)`：绘制二维条形图，默认展示平均值
       
       - `sns.countplot(df3,x="species")`：绘制计数图
       
       - `plt.pie(df4["vote"],labels=df4["fruit"],autopct="%.1f%%")`：绘制饼图，标签为水果列，显示数据到小数位第一位
     
     - 绘制多个变量数据
       
       - `sns.scatterplot(iris,x="length",y="width",hue="species")`：绘制二维散点图，x轴为长度，y轴为宽度，以`species`进行分类
       
       - `sns.scatterplot(iris,x="length",y="width",hue="species", size="petal_length")`：绘制二维散点图，x轴为长度，y轴为宽度，以`species`进行类型分类，以`petal_length`进行点大小分类
       
       - `sns.heatmap(glue,annot=True)`：绘制热力图，并且每个小方块上显示数据数字，默认情况下`annot=False`
       
       - 显示聚合图表【适用于一维图表的聚合显示】，代码示例如下：
         
         ```python
         sns.histplot(s1,binwidth=0.1,label="test1")
         sns.histplot(s2,binwidth=0.1,label="test2")
         sns.histplot(s3,binwidth=0.1,label="test3")
         plt.legend()
         plt.show()
         ```
         
         在一张图表上，显示`s1`,`s2`,`s3`三张图表的聚合情况，每个条柱的宽度为0.1，每个条柱设置自己的标签，同时在图表内显示图例。
       
       - `sns.boxplot(s1,y="length",x="species")`：绘制箱型图，y轴表示长度，x轴用`species`进行分类
       
       - `plt.subplots(1,3)`：绘制一张表示一行三列的图表
       
       - `plt.subplots(1,3,figsize=(15,5))`：绘制一张表示一行三列的图表，为每个子图绘制大小，总图表大小为15，每个子图的大小为5
       
       - 显示多个子图【`plt.subplots`】，代码示例如下：
         
         ```python
         fig,axes = plt.subplots(1,3,figsize=(15,5))
         sns.boxplot(data=iris,y="length",x="species",ax=axes[0])
         sns.boxplot(data=iris,y="length",x="species",ax=axes[1])
         sns.boxplot(data=iris,y="length",x="species",ax=axes[2])
         plt.show()
         ```
         
         `fig`：表示整个大图，`axes`：表示子图列表
         
         `ax=axes[0]`：绘制箱型图表到第一个子图上
       
       - `sns.pairplot(iris)`：绘制一组图例，把数据里每个列之间的数据进行显示，并且把每个列与其他列之间的关系也绘制成图表
       
       - `sns.pairplot(iris,hue="species")`：绘制一组图例，把数据里每个列之间的数据进行显示，并且把每个列与其他列之间的关系也绘制成图表，并用`species`进行数据分类
       
       - `sns.pairplot(iris,hue="species",kind="reg")`：绘制一组图例，把数据里每个列之间的数据进行显示，并且把每个列与其他列之间的关系也绘制成图表，并用`species`进行数据分类，同时为每个散点图绘制线性回归线，大致上表示出散点群的走向、趋势
       
       - `sns.pairplot(iris,hue="species",kind="reg",plot_kws={'scatter_kws'}:{"alpha":0.5})`：绘制一组图例，把数据里每个列之间的数据进行显示，并且把每个列与其他列之间的关系也绘制成图表，并用`species`进行数据分类，同时为每个散点图绘制线性回归线，大致上表示出散点群的走向、趋势，最后调整散点图散点的透明度为0.5
     
     - 展示图表【`jupyter`里不需要这一步】
       
       - `plt.show()`
     
     - 添加副内容【这些方法都需要在`splt.show()`方法之前运行】
       
       - `plt.title("Adelie...")`：为图表添加标题，标题内容为：...
       
       - `plt.xlabel("单位:mm")`：为图表添加x轴的标签
       
       - `plt.ylabel("样本数量")`：为图表添加y轴的标签
       
       - `plt.legend(bbox_to_anchor=(1,1))`：将图表的图例显示在图表外侧右边【0,0 表示显示在图表内侧、0,1 表示显示在图表外侧左边、1,0 表示显示在图表外侧下边、1,1 表示显示在图表外侧右边】
     
     - 修改数据的表示【用在绘制方法中】
       
       - `color="red"`：把数据的表示颜色修改为红色【hex格式也支持】
       
       - `sns.set_palette("pastel")`：把数据的表示色盘修改为粉笔色，其它的色系还有`crest`等等【默认色盘是`muted`】

4. 可视化帕默群岛企鹅数据
   
   - 读取数据
   
   - 评估数据
   
   - 清理数据
   
   - 数据探索
     
     - 设置色盘
     
     - 检查数据
     
     - 企鹅种类比例，对企鹅的每个种类的数量进行统计【通过种类比例，得到合理的结论】
     
     - 企鹅所属岛屿的比例
     
     - 企鹅性别比例
     
     - 不同岛屿上的企鹅种类数量
     
     - 不同岛屿上的企鹅性别数量
     
     - 查看数值之间的相关关系，相关关系一般使用`pairplot`
     
     - 根据种类查看数值之间的相关关系
     
     - 根据性别查看数值之间的相关关系
