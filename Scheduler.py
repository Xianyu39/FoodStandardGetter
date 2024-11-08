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
        if os.listdir("originPages").count("additivePage.html") == 0:
            print("下载添加剂表成功")
            additivePage = downloader.Download(ROOT_ADDITIVE)
            with open("./originPages/additivePage.html", "w") as f:
                f.write(additivePage)

        parser = Parser()
        with open("additivePage.html", "r") as f:
            addUrlList = parser.ParseAdditiveUrls(f.read())

        print("添加剂表处理完成")
        self.additiveTb = pd.DataFrame(
            columns=["INS号", "CNS号", "中文名称","英文名称","功能","质量规格标准","JECFA规格资料","备注"],
            index=[i[0] for i in addUrlList],
        )

        # 下载所需要的页面
        fileNames = os.listdir("originPages")
        if len(fileNames)==0:
            for i,(addUrl,addName) in enumerate(addUrlList):
                print(f"{i}.下载{addName}的资料")
                page = downloader.Download(addUrl)
                print(f"{i}.{addName}的资料下载成功")
                with open(f"./originPages/{i}.html", "w") as f:
                    f.write(page)

            downloader.driver.quit()

        # 筛选信息
        failAdds=[]
        for i,(addUrl,addName) in enumerate(addUrlList):
            with open(f"./originPages/{i}.html", "r") as f:
                page = f.read()
                try:
                    addRow,addRel = parser.ParseAdditiveAttrs(page)
                    for key,value in addRow.items():
                        self.additiveTb.loc[addUrl, key]=value

                    addFoodTb=pd.DataFrame(data=addRel)
                    addFoodTb.columns=["食品分类号","食品名称","最大使用量（g/kg）","备注"]
                    addFoodTb.to_excel(f"./food/{addName[:30]}.xlsx")
                    print(f"添加剂{addName}处理完成")

                except Exception as e:
                    print(e)
                    print(f"{addName}({addUrl})信息处理失败")
                    failAdds.append(f"{addName}({addUrl})")


        self.additiveTb.to_excel("AdditiveTable.xlsx")
        self.foodTb.to_excel("FoodTable.xlsx")

        print(f"处理完毕，{len(failAdds)}个处理失败：")
        with open("failed.txt", "w") as f:
            f.writelines([i+"\n" for i in failAdds])

        print("处理失败的添加剂信息写入到failed.txt中")



if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.run()
    import numpy as np
    print(scheduler.additiveTb.iloc[:,-1].count())

        