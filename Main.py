# /bin/python
# author:leozhao
# author@email: dhzzy88@163.com

"""
这是整个爬虫系统的主程序

"""
import numpy as np

import dataFactory
import plotpy
import sqlDeal
import zhilian
from Constant import JOB_KEY

#
# 启动爬虫程序
zhilian.spidefmain(JOB_KEY)

"""
 爬取数据结束后对数据可视化处理
"""
# 从数据库读取爬取的数据
# 先得到的是元组name,salray，demand,welfare

value = sqlDeal.sqlselect()
# 工资上限，下限，平均值
updata = np.array([], dtype=np.int)
downdata = np.array([], dtype=np.int)
average = np.array([], dtype=np.int)
for item in value:
    salray = dataFactory.SarayToInt(item[1])
    salray.slove()
    updata = np.append(updata, salray.up)
    downdata = np.append(downdata, salray.down)
    average = np.append(average, (salray.up + salray.down) / 2)

# 工资上下限
average.sort()

# 匹配城市信息 暂时还未实现

# 统计信息
# 两种图形都加载出来 方便查看
plotpy.plotl(average)
plotpy.plots(average)

print(average, average.sum())
print("平均工资:", average.sum() / len(average))
print("最高：", average.max())
print("最低", average.min())
print("职位数", len(average))

# 画图
