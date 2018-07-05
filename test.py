# /bin/python
# author:leozhao


class Te:
    def __init__(self, a):
        self.a = a

    def Te(self):
        self.a = 10


T = Te(20)
T.Te()
print(T.a)

f = open("BaiduCity.txt", "r")
string = f.read()
count = 0
gweizhi = []
nweizhi = []
stringdata = []
for st in string:
    stringdata.append(st)
    if st == "g":
        gweizhi.append(count)
    elif st == "n":
        nweizhi.append(count)
    print(st)
    count += 1

print(gweizhi, nweizhi)
print(stringdata)
count2 = 0
stringf = ""
for i in stringdata:
    if i == "n":
        stringdata[count2] = "\"n\""
    elif i == "g":
        stringdata[count2] = "\"g\""
    count2 += 1
stringf = stringf.join(stringdata)
print(stringf)
with open("newbaiducity.txt", "w") as f:
    f.write(stringf)
