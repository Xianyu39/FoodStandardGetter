from bs4 import BeautifulSoup
import re

class Parser:
    def __init__(self):
        pass

    def ParseAdditiveUrls(self,text)->list:
        """处理食品添加剂查询页面，筛选出所有的食品添加剂以及页面url，以列表形式[(url,添加剂名称)]返回"""
        bs = BeautifulSoup(text,'lxml')
        additiveTableTag = bs.find_all("table", {"cellspacing":"1","class":"beige1 layer_big"})[0]
        return [("http://27602014.foodmate.net"+a['href'], str(a.text)) for a in additiveTableTag.select("a")]
    
    def ParseAdditiveAttrs(self,text)->list:
        """处理食品添加剂页面，筛选出食品添加剂属性和食品添加剂在各个食品中可用的量等信息，以属性字典和列表的形式返回"""
        bs = BeautifulSoup(text,'lxml')
        additiveInfoLists=bs.find_all("table",{"class":"beige1"})
        attrs,foodadd = additiveInfoLists[0],additiveInfoLists[1]
        # 处理添加剂属性
        attrs = attrs.select("tr")
        attrNames,attrVals = [attr.select("th")[0] for attr in attrs],[attr.select("td")[0] for attr in attrs]
        attrNames = [n.text for n in attrNames]
        attrVals = [n.text for n in attrVals]
        additiveRow = dict(zip(attrNames,attrVals))
        # 处理可用于各种食品的剂量
        rows = foodadd.select("tr")
        rows = rows[1:] # 去除第一行表头
        additivefoods = []
        for row in rows:
            vals = [i.text for i in row.select("td")]
            additivefoods.append(vals)

        return additiveRow, additivefoods


if __name__ == "__main__":
    parser = Parser()
    with open("./originPages/16.html",'r') as f:
        with open("test.html","w") as f1:
            f1.write(str(parser.ParseAdditiveAttrs(f.read())))
