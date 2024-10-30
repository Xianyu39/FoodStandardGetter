import os
import pandas as pd
from Downloader import Downloader
from Parser import Parser

ROOT_FOOD = "http://27602014.foodmate.net/index.php?m=additives&a=category"
ROOT_ADDITIVE = "http://27602014.foodmate.net/index.php?m=additives&a=index"

class Scheduler:
    def __init__(self) -> None:
        
        self.foodTb = pd.DataFrame(
            columns=["食品分类号", "食品名称", "食品描述",]
        )
        self.foodAdditiveTb = pd.DataFrame(
            columns=["食品分类号","INS"]
        )

    def run(self):
        downloader = Downloader()
        parser = Parser()

        addUrlList = parser.ParseAdditiveUrls(downloader.Download(ROOT_ADDITIVE))
        print("下载添加剂表成功")
        print("添加剂表处理完成")
        self.additiveTb = pd.DataFrame(
            columns=["INS号", "CNS号", "中文名称","英文名称","功能","质量规格标准","JECFA规格资料","备注"],
            index=addUrlList,
        )
        # self.additiveTb.loc[:,"url"]=addUrlList

        for i,(addUrl,addName) in enumerate(addUrlList):
            print(f"{i}.下载{addName}的资料")
            page = downloader.Download(addUrl)
            print(f"{i}.{addName}的资料下载成功")
            with open(f"./originPages/{i}.html", "w") as f:
                f.write(page)

            # addRow,addRel = parser.ParseAdditiveAttrs(page)
            # for key,value in addRow.items():
            #     self.additiveTb.loc[addUrl, key]=value

            # addFoodTb=pd.DataFrame(data=addRel)
            # addFoodTb.columns=["食品分类号","食品名称","最大使用量（g/kg）","备注"]
            # addFoodTb.to_excel(f"./food/{addName[:30]}.xlsx")
            # print(f"添加剂{addName}处理完成")


        # self.additiveTb.to_excel("AdditiveTable.xlsx")
        # self.foodTb.to_excel("FoodTable.xlsx")
        downloader.driver.quit()


if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()

        