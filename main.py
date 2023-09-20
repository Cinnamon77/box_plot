import pandas as pd

# 读取CSV文件
csv_file = "school_data.csv"
df = pd.read_csv(csv_file)

# 用户输入国家和目标GPA
target_country = input("请输入国家: ")
target_gpa = float(input("请输入目标GPA: "))

# 1. 按国家筛选学校
filtered_df = df[df['Country'] == target_country]

# 2. 筛选符合GPA范围的学校（小于目标GPA）
filtered_df = filtered_df[filtered_df['Max'] < target_gpa]

# 打印筛选出的学校
if not filtered_df.empty:
    print("以下学校的最大GPA小于目标GPA:")
    for index, school in filtered_df.iterrows():
        print("学校:", school['School'])
        print("---------------")
else:
    print("没有符合条件的学校。")
