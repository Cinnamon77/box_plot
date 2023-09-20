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

# 3. 计算查询成绩与中位数的差值
filtered_df['Difference'] = abs(filtered_df['Median'] - target_gpa)

# 4. 按差异度升序排序
filtered_df = filtered_df.sort_values(by='Difference')

# 打印推荐学校列表
if not filtered_df.empty:
    print("推荐学校:")
    for index, school in filtered_df.iterrows():
        print("学校:", school['School'])
        print("---------------")
        # print("国家:", school['Country'])
        # print("最大值:", school['Max'])
        # print("最小值:", school['Min'])
        # print("中位数:", school['Median'])
        # print("差异度:", school['Difference'])
        # print("-------------")
else:
    print("没有符合条件的学校。")
