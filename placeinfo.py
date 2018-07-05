# /bin/python
# author:leozhao
# author@email :dhzzy88@163.com

import json

"""
        这个模块还在坐主要设想是做一个地理热点图
"""


class JsonDate:
    def jsondeal(self):
        with open("baiducity.json", "r") as f:
            string = f.read()
        data = json.loads(string)
        for placename in data:
            if placename == "provinces":
                for city in data[placename]:
                    # 列表里面的字典，得到以后再去获得经纬数据
                    cities = city['cities']
                    yield cities

            else:
                cities = data[placename]
                # 直辖市，和其他地区
            yield cities

    def placeinfodel(self, cities):
        for cityname in cities:
            print(cityname)
            self.getdata(cityname)

    def getdata(self, cityname):

        data = cityname["g"].split(",")
        # lon经度
        lon = float(data[0])
        # lat
        lat = float(data[1][:-3])
        print("经度%.10s,\t维度%.10s" % (lon, lat))
        print(lat)
        print(cityname["n"])


def placemain():
    Json = JsonDate()
    jd = Json.jsondeal()
    while True:
        try:
            Json.placeinfodel(jd.__next__())
        except StopIteration:
            break


if __name__ == '__main__':
    Json = JsonDate()
    jd = Json.jsondeal()
    while True:
        try:
            Json.placeinfodel(jd.__next__())
        except StopIteration as e:
            break
