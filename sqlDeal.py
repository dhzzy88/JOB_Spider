# /bin/python
# author:leozhao
# author@email :dhzzy88@163.com

import mysql.connector

from Constant import SELECT
from Constant import SQL_USER
from Constant import database
from Constant import password


def sqldeal(job_name, job_salray, job_demand, job_welfare):
    conn = mysql.connector.connect(user=SQL_USER, password=password, database=database, use_unicode=True)
    cursor = conn.cursor()
    infostring = "insert into zhilian value('%s','%s','%s','%s')" % (
        job_name, job_salray, job_demand, job_welfare) + ";"
    cursor.execute(infostring)
    conn.commit()
    conn.close()


def sqlselect():
    conn = mysql.connector.connect(user=SQL_USER, password=password, database=database, use_unicode=True)
    print("连接数据库读取信息")
    cursor = conn.cursor()

    cursor.execute(SELECT)
    values = cursor.fetchall()
    conn.commit()
    conn.close()
    return values


if __name__ == '__main__':
    job_name = "自如管家（销售均薪一万＋，房租五折）"
    job_saray = "8K-10K"
    job_demand = "北京 经验不限 学历不限"
    job_welfare = "五险一金 绩效奖金 餐补 房补 弹性工作"
    sqldeal(job_name, job_saray, job_demand, job_welfare)
    print(sqlselect())
