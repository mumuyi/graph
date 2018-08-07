import matplotlib.pyplot as plt
import numpy as np
import xlrd

# 打开文件
workbook = xlrd.open_workbook(r'C:\Users\ai\Desktop\Precision.xlsx')
#workbook = xlrd.open_workbook(r'C:\Users\ai\Desktop\NDCG.xlsx')
# 获取所有sheet
print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
# 获取sheet2
sheet1_name = workbook.sheet_names()[0]
print(sheet1_name)
# 根据sheet索引或者名称获取sheet内容
sheet1 = workbook.sheet_by_name('Sheet1')
# sheet的名称，行数，列数
print(sheet1.name, sheet1.nrows, sheet1.ncols)
rows = sheet1.row_values(3)  # 获取第四行内容
cols = sheet1.col_values(0)  # 获取第三列内容
print(rows)
print(cols)

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))

all_data = [sheet1.col_values(0), sheet1.col_values(1), sheet1.col_values(2)]

# fig = plt.figure(figsize=(8,6))

axes.violinplot(all_data,
                   showextrema=False,
                   showmeans=False,
                   showmedians=False,
                   )
axes.boxplot(all_data,
                showfliers=False,
                showcaps=False,
                showmeans=True,
                whiskerprops={'color': '0.5', 'linewidth': '0'}
                )
axes.set_title('Precision')
#axes.set_title('NDCG')

# adding horizontal grid lines
ax = axes
ax.yaxis.grid(True)
ax.set_xticks([y + 1 for y in range(len(all_data))], )
ax.set_ylabel('Precision@5')
#ax.set_ylabel('NDCG@5')

plt.setp(axes, xticks=[y + 1 for y in range(len(all_data))],
         xticklabels=['CLBCRS', 'Strathcona', 'Mohamman'],
         )

plt.show()

