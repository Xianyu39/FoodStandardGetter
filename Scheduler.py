import os
import pandas as pd
from Downloader import Downloader

ROOT_FOOD = "http://27602014.foodmate.net/index.php?m=additives&a=category"
ROOT_ADDITIVE = "http://27602014.foodmate.net/index.php?m=additives&a=index"

class Scheduler:
    def __init__(self) -> None:
        self.additiveTb = pd.DataFrame(
            columns=["INS", "CNS", "中文名","英文名","功能","质量规格标准","JECFA","备注"]
        )
        self.foodTb = pd.DataFrame(
            columns=["食品分类号", "食品名称", "食品描述",]
        )
        self.foodAdditiveTb = pd.DataFrame(
            columns=["食品分类号","INS"]
        )

    def BuildAdditiveTb():
        dld = Downloader()
        