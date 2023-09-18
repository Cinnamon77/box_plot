import pandas as pd

# 读取CSV文件
csv_file = "school_data.csv"
df = pd.read_csv(csv_file)

# 用户输入国家和目标GPA
target_country = input("请输入国家: ")
target_gpa = float(input("请输入目标GPA: "))

# 1. 按国家筛选学校
filtered_df = df[df['Country'] == target_country]

# 2. 筛选符合GPA范围的学校
filtered_df = filtered_df[(filtered_df['Max'] >= target_gpa) & (filtered_df['Min'] <= target_gpa)]

# 3. 计算查询成绩与中位数的差值，按差异度最小排序
filtered_df['Difference'] = abs(filtered_df['Median'] - target_gpa)
filtered_df = filtered_df.sort_values(by='Difference')

# 打印推荐学校
if not filtered_df.empty:
    recommended_school = filtered_df.iloc[0]
    print("推荐学校:")
    print("学校:", recommended_school['School'])
    print("国家:", recommended_school['Country'])
    print("最大值:", recommended_school['Max'])
    print("最小值:", recommended_school['Min'])
    print("中位数:", recommended_school['Median'])
    print("差异度:", recommended_school['Difference'])
else:
    print("没有符合条件的学校。")
