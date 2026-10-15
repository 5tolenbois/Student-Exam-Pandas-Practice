import os
import pandas as pd
import numpy as np

# ========== 自动获取脚本所在目录，解决csv相对路径问题 ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ===================== 2.1 读取两个数据集 data1.csv data2.csv =====================
path1 = os.path.join(BASE_DIR, "data", "data1.csv")
path2 = os.path.join(BASE_DIR, "data", "data2.csv")

data1 = pd.read_csv(path1)   # 数据集1
data2 = pd.read_csv(path2)   # 数据集2

# 展示数据集前5行数据
print("="*60)
print("【data1前5行】")
print(data1.head(5))
print("="*60)
print("【data2前5行】")
print(data2.head(5))

# ===================== 2.2 查看数据类型 =====================
print("="*60)
print("【data1各字段数据类型】")
print(data1.dtypes)
print("="*60)
print("【data2各字段数据类型】")
print(data2.dtypes)

# 筛选字符型(object)数据
data1_str = data1.select_dtypes(include=['object'])
print("="*60)
print("【data1字符型字段数据】")
print(data1_str)

# ===================== 2.3 info()查看数据集基础信息 =====================
print("="*60)
print("【data1 info信息】")
data1.info()
print("="*60)
print("【data2 info信息】")
data2.info()

# ===================== 2.4 describe描述性统计 =====================
df1 = data1_str.describe(include='object')
df2 = data2.describe()
print("="*60)
print("【data1字符字段describe统计】")
print(df1)
print("="*60)
print("【data2数值字段describe统计】")
print(df2)

# ===================== 2.5 缺失值查询与缺失值填充 =====================
print("="*60)
print("【data1缺失值统计】")
print(data1.isnull().sum())
print("="*60)
print("【data2填充前缺失值统计】")
print(data2.isnull().sum())

# 使用均值填充data2缺失值(inplace原地修改)
data2.fillna(data2.mean(numeric_only=True), inplace=True)

print("="*60)
print("【data2均值填充后缺失值统计】")
print(data2.isnull().sum())

# ===================== 2.6 协方差矩阵、相关系数矩阵 =====================
# 只选取数值列计算协方差、相关系数
numeric_cols = data2.select_dtypes(include=[np.number]).columns
df_cov = data2[numeric_cols].cov()
df_corr = data2[numeric_cols].corr()
print("="*60)
print("【协方差矩阵】")
print(df_cov)
print("="*60)
print("【相关系数矩阵】")
print(df_corr)

# ===================== 2.7 数据融合 merge，根据ID连接两张表 =====================
df_merge = pd.merge(data1, data2, on="ID")
print("="*60)
print("【merge融合后数据前5行】")
print(df_merge.head(5))

# ===================== 2.8 索引设置、索引排序 =====================
# 将race/ethnicity设置为行索引
df_merge = df_merge.set_index('race/ethnicity')
print("="*60)
print("【设置索引后前5行】")
print(df_merge.head(5))

# 根据索引排序 sort_index
df_merge = df_merge.sort_index()
print("="*60)
print("【索引排序后前5行】")
print(df_merge.head(5))

# ===================== 2.9 新增总分列，按数值降序排序 sort_values =====================
df_merge["total score"] = df_merge['math score'] + df_merge['reading score'] + df_merge['writing score']

# 按照总分total score降序排序
df_merge = df_merge.sort_values(by='total score', ascending=False)
print("="*60)
print("【按总分降序排序，展示前10行】")
print(df_merge.head(10))

# ===================== 2.10 等距离散化 cut，总分划分等级A/B/C/D =====================
df_merge["total_level"] = pd.cut(df_merge['total score'], bins=4, labels=['D', 'C', 'B', 'A'])
print("="*60)
print("【总分离散化分级，随机抽取10行】")
print(df_merge.sample(n=10, replace=False))

# ===================== 2.11 replace替换文本字段内容 =====================
df_merge = df_merge.replace({
    'some college': 'college',
    'some high school': 'high school'
})
print("="*60)
print("【replace替换完成，随机抽取10行】")
print(df_merge.sample(n=10, replace=False))

# ===================== 2.12 map字典映射转换 =====================
# none → No ；completed → Yes
map_dict = {"none": "No", "completed": "Yes"}
df_merge['test preparation course'] = df_merge["test preparation course"].map(map_dict)
print("="*60)
print("【map映射转换完成，随机抽取10行】")
print(df_merge.sample(n=10, replace=False))

# ===================== 2.13 get_dummies哑变量(one‑hot)编码 + concat拼接 =====================
# gender列哑变量编码，drop_first=True去掉第一列避免多重共线性
df_dummies1 = pd.get_dummies(df_merge['gender'], drop_first=True)
print("="*60)
print("【gender哑变量编码前5行】")
print(df_dummies1.head(5))

# parental level of education One‑Hot编码，不删除列
df_dummies2 = pd.get_dummies(df_merge['parental level of education'], drop_first=False)
print("="*60)
print("【父母学历One‑Hot编码前5行】")
print(df_dummies2.head(5))

# concat横向拼接编码结果到原表
df_merge = pd.concat([df_merge, df_dummies1, df_dummies2], axis=1)
print("="*60)
print("【拼接编码后数据集前5行】")
print(df_merge.head(5))

# ===================== 2.14 groupby数据分组 =====================
# 按照gender分组
group_result = df_merge.groupby('gender')
result = list(group_result)
print("="*60)
print("【gender分组结果(转列表查看)】")
print(result)

# 按照parental level of education分组，查看每组样本数量size()
group_result = df_merge.groupby('parental level of education')
group_size = group_result.size()
print("="*60)
print("【父母学历分组样本数量】")
print(group_size)

# ===================== 2.14 groupby数据分组 =====================
# 按照gender分组
group_result = df_merge.groupby('gender')
result = list(group_result)
print("="*60)
print("【gender分组结果(转列表查看)】")
print(result)

# 按照parental level of education分组，查看每组样本数量size()
group_result = df_merge.groupby('parental level of education')
group_size = group_result.size()
print("="*60)
print("【父母学历分组样本数量】")
print(group_size)

# 自定义函数分组：apply生成标签列后再分组
df_merge["score_tag"] = df_merge["total score"].apply(lambda s: "高分组" if s >= 200 else "普通组")
group_func = df_merge.groupby("score_tag")
result_func = list(group_func)
print("="*60)
print("【自定义函数分组结果】")
print(result_func)

# ===================== 2.15 agg聚合：组内多统计指标计算 =====================
# 按race/ethnicity分组，数学分数：均值、方差、最大值、最小值
math_agg = df_merge.groupby("race/ethnicity")["math score"].agg(["mean", "var", "max", "min"])
print("="*60)
print("【按种族分组数学分数聚合统计】")
print(math_agg)

# ===================== 2.16 transform 组内转换，把分组均值广播回每一行 =====================
df_merge["total_mean"] = df_merge.groupby("race/ethnicity")["total score"].transform("mean")
print("="*60)
print("【transform增加组均分字段，随机抽取10行】")
print(df_merge.sample(n=10, replace=False))

# ===================== 2.17 map()元素级函数转换（新版pandas替代applymap） =====================
df_small = df_merge[["total_mean"]]
result_applymap = df_small.map(int)
print("="*60)
print("【map转为int类型，前5行】")
print(result_applymap.head(5))

print("\n全部Pandas预处理流程执行完毕！")
