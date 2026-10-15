# 学生考试表现数据集 Pandas综合预处理实战
> 数据科学与大数据技术专业课堂实战项目
完整覆盖Pandas数据分析预处理全套常用API，适合简历作品集。

## 项目说明
将原始数据集拆分为 data1.csv、data2.csv，演示真实数据分析全流程：
数据读取、数据探查、数据类型查看、info、describe统计、缺失值检测与填充；
协方差、相关系数计算；merge表融合；索引设置、索引排序、按值排序；
cut等距离散化、replace替换、map字典映射；
get_dummies哑变量One‑Hot编码、concat表拼接；
groupby分组、自定义函数分组、agg多指标聚合；
transform组广播转换、applymap元素级函数处理。

## 数据集字段
- ID：学生编号
- gender：性别
- race/ethnicity：种族分组
- parental level of education：父母教育水平
- lunch：午餐类型
- test preparation course：是否参加考前复习
- math score、reading score、writing score：三科考试分数

## 环境依赖
```bash
pip install pandas numpy
