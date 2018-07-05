# /bin/python
# author:leo
# author@email : dhzzy88@163.com
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import sqlDeal
from Constant import PAGE_NUMBER


def init(key="JAVA"):
    # 智联招聘的主页搜索关键字，初始化到采集页面
    url = "https://www.zhaopin.com/"
    opt = webdriver.FirefoxOptions()
    opt.set_headless()
    driver = webdriver.Firefox(options=opt)
    driver.get(url)
    driver.find_element_by_class_name("zp-search-input").send_keys(key)
    # driver.find_element_by_class_name(".zp-search-btn zp-blue-button").click()
    driver.find_element_by_class_name("zp-search-input").send_keys(Keys.ENTER)
    import time
    time.sleep(2)
    all = driver.window_handles
    driver.switch_to_window(all[1])
    url = driver.current_url
    return url


class ZhiLian:

    def __init__(self, key='JAVA'):
        # 默认key:JAVA
        indexurl = init(key)
        self.url = indexurl
        self.opt = webdriver.FirefoxOptions()
        self.opt.set_headless()
        self.driver = webdriver.Firefox(options=self.opt)
        self.driver.get(self.url)

    def job_info(self):

        # 提取工作信息     可以把详情页面加载出来
        job_names = self.driver.find_elements_by_class_name("job_title")
        job_sarays = self.driver.find_elements_by_class_name("job_saray")
        job_demands = self.driver.find_elements_by_class_name("job_demand")
        job_welfares = self.driver.find_elements_by_class_name("job_welfare")
        for job_name, job_saray, job_demand, job_welfare in zip(job_names, job_sarays, job_demands, job_welfares):
            sqlDeal.sqldeal(str(job_name.text), str(job_saray.text), str(job_demand.text), str(job_welfare.text))

        # 等待页面加载
        print("等待页面加载")
        WebDriverWait(self.driver, 10, ).until(
            EC.presence_of_element_located((By.CLASS_NAME, "job_title"))
        )

    def page_next(self):
        try:
            self.driver.find_elements_by_class_name("btn btn-pager").click()
        except:
            return None
        self.url = self.driver.current_url
        return self.driver.current_url


def spidefmain(key="JAVA"):
    ZHi = ZhiLian(key)
    ZHi.job_info()
    # 设定一个爬取的页数
    page_count = 0
    while True:
        ZHi.job_info()
        ZHi.job_info()
        page_count += 1
        if page_count == PAGE_NUMBER:
            break
    # 采集结束后把对象清除
    del ZHi


if __name__ == '__main__':
    spidefmain("python")
