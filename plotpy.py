# /bin/python
# author:leozhao
# author@email : dhzzy88@163.com

import matplotlib.pyplot as plt
import numpy as np

from Constant import JOB_KEY


# 线型图


def plotl(dta):
    dta.sort()
    print("dta", [dta])
    num = len(dta)
    x = np.linspace(0, num - 1, num)
    plt.plot(x, [int(da) for da in dta])
    plt.plot(x, [sum(dta) / num for i in range(num)], )
    plt.xlim(0, 250)
    plt.title(JOB_KEY + 'Job_Info')
    plt.xlabel(JOB_KEY + 'Job_Salray')
    plt.ylabel('JobNumbers')
    plt.show()


# 条形图


def plots(dta):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.hist(dta, bins=15)
    plt.title(JOB_KEY + 'Job_Info')
    plt.xlabel(JOB_KEY + 'Job_Salray')
    plt.ylabel('JobNumbers')
    plt.show()
