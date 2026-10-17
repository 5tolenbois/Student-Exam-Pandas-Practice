# 学生考试成绩数据分析 Pandas实战
> 数据科学与大数据技术专业｜Pandas表格数据处理练习项目
## 项目简介
本项目使用学生考试数据集，完整练习Pandas全套基础数据预处理操作。包含多表合并、缺失值处理、描述统计、特征衍生、离散化、文本替换、映射转换、独热编码、分组聚合、transform组内广播等核心API，分析学生三门科目成绩，探索不同人群成绩分布规律。
> 技术栈：Python、Pandas、NumPy

## 数据集介绍
项目包含两份csv文件 `data/data1.csv`、`data/data2.csv`，共1000条学生样本
data1.csv（学生基础信息）
- ID：学生编号
- gender：性别
- race/ethnicity：种族分组
- parental level of education：父母教育水平
- lunch：午餐类型
- test preparation course：是否参加考前辅导课程

data2.csv（考试分数）
- ID：学生编号，作为两表连接主键
- math score：数学成绩
- reading score：阅读成绩
- writing score：写作成绩

##  运行结果总结
1. 数据情况：data1无缺失值；data2的reading score存在7条缺失记录，采用均值填充处理，填充后无缺失。
2. 相关性：数学、阅读、写作三科分数之间**高度正相关**，阅读与写作相关性最高达到0.95；学生ID和成绩几乎无关联。
3. 成绩分布：最高总分300分（三科满分），E组学生平均分显著高于其他种族分组。
4. 特征工程：新增`total score`总分、`total_level`成绩等级、`score_tag`高低分组、`total_mean`分组平均分；对性别、学历类别进行One-Hot编码，适合后续建模。
5. Pandas练习点：完整练习多表融合、索引操作、离散分箱、文本清洗、独热编码、分组聚合、transform广播等数据分析高频操作。

## 分析流程
2.1 读取两个数据集，预览前5行
2.2 查看字段数据类型，筛选字符类型字段
2.3 info()查看数据集基础信息，统计非空数量
2.4 describe()完成描述性统计
2.5 缺失值检测，使用均值填充reading score缺失数据
2.6 计算数值字段协方差矩阵、相关系数矩阵
2.7 通过ID做merge，完成两张数据表融合
2.8 设置索引、索引排序
2.9 新增总分字段，按照总分降序排序
2.10 使用cut对总分等距离散化，划分A/B/C/D四个等级
2.11 replace文本替换，简化父母学历文本
2.12 map字典映射，将课程状态文本转换Yes/No
2.13 get_dummies哑变量（One-Hot）编码，使用concat横向拼接
2.14 groupby分组：按性别、父母学历分组；自定义函数分组标记高低分
2.15 agg聚合：分组后一次性计算均值、方差、最大最小值
2.16 transform：将分组均值广播到每行，新增组平均分字段
2.17 map元素级类型转换，浮点转整数


## 项目运行方式
```bash
# 安装依赖
pip install pandas numpy
# 运行脚本
python student_exam_analysis.py
