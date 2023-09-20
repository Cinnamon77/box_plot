import matplotlib.pyplot as plt

data = [91.14, 88.02, 89.81]  # 更新数据列表

plt.boxplot(data)
plt.title('Box Plot for GPA at 康奈尔大学, 美国')  # 修改标题

plt.savefig('box_plot.png')

