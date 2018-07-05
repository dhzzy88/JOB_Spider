# /bin/python
# author:leozhao

data = "10K-15K"
"""
data = data.split("K")
for num in data:
    tmp = []
    if num !="":
        tmp.append(abs(int(num)))

    tuple(tmp)
"""


class SarayToInt:

    def __init__(self, data):
        self.tmp = []
        self.data = data.split("K")
        for num in self.data:
            if num != "":
                if num in ["薪资面议", "工资面议", "待遇面议"]:
                    self.tmp.append(0)
                    self.tmp.append(3)
                else:
                    try:
                        self.tmp.append(abs(int(num)))
                    except ValueError:
                        self.tmp.append(abs(int(float(num))))

        self.up = 0
        self.down = 0

    def slove(self):
        self.up = self.tmp[0] * 1000
        self.down = self.tmp[1] * 1000


if __name__ == '__main__':
    # 这个模块不单独使用下面代码只是在测试程序时用
    datatest = "12.5K-30K,20K-40K,20K-40K,12.5K-30K,15K-30K,15K-30K,15K-25K,20K-30K,10K-20K,薪资面议"
    dats = datatest.split(",")
    for d in dats:
        Sa = SarayToInt(d)
        Sa.slove()
        print(Sa.up, Sa.down)
