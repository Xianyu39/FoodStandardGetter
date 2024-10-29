import bs4
import os
import httpx

class Downloader:
    def __init__(self):
        pass

    def Download(self, url)->str:
        """"""
        res = httpx.get(url)
        if res.status_code != 200:
            raise httpx.HTTPError(f"{url} 下载失败，返回代码{res.status_code}")
        
        return res.content