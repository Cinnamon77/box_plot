import pandas as pd
import numpy as np

# 读取Excel文件
excel_file = "/root/vitrual_env_test/project/国家，学校，gpa.xlsx"
df = pd.read_excel(excel_file)

# 创建一个新的DataFrame，只包含学校、国家和GPA列
data = df[['学校', '国家', 'GPA']]

# 创建一个函数来计算每个学校的箱线图参数
def calculate_box_plot_parameters(data):
    # 使用Tuckey方法计算上下四分位数
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # 去除异常值
    data_no_outliers = [x for x in data if lower_bound <= x <= upper_bound]

    # 计算最大值、最小值和中位数
    max_value = max(data_no_outliers)
    min_value = min(data_no_outliers)
    median = np.median(data_no_outliers)

    return max_value, min_value, median

# 创建一个字典来存储每个学校的箱线图参数
school_box_plot_parameters = {}

# 遍历每个学校
unique_schools = data['学校'].unique()
for school in unique_schools:
    school_data = data[data['学校'] == school]['GPA']
    max_val, min_val, median_val = calculate_box_plot_parameters(school_data)
    school_box_plot_parameters[school] = {'Max': max_val, 'Min': min_val, 'Median': median_val}

# 创建一个新的DataFrame，用于保存箱线图参数
output_df = pd.DataFrame.from_dict(school_box_plot_parameters, orient='index')

# 添加国家列
output_df['国家'] = [data[data['学校'] == school]['国家'].values[0] for school in output_df.index]

# 将数据保存到Excel文件，并设置编码为UTF-8
output_excel_file = "box_plot_parameters.xlsx"
with pd.ExcelWriter(output_excel_file, engine='xlsxwriter') as writer:
    output_df.to_excel(writer, sheet_name='Sheet1', encoding='utf-8', index=False)

print(f'数据已保存到Excel文件：{output_excel_file}')
