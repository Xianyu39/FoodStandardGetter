import bs4
import time
import httpx
import selenium.webdriver

class Downloader:
    def __init__(self,waitTime=3):
        self.waitTime = waitTime
        self.header={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/130.0.0.0",
            "cookie":"bc08_f0d8_saltkey=etL1njNv; bc08_f0d8_lastvisit=1730029396; think_language=zh-CN; PHPSESSID=d5igq1eut7vrio1oraovcnc935",
            "connection":"keep-alive",
            "host":"27602014.foodmate.net"
        }
        self.options=selenium.webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = selenium.webdriver.Chrome(options=self.options)


    def Download(self, url)->str:
        """使用浏览器下载页面，以字符串的形式返回"""
        self.driver.get(url)
        time.sleep(self.waitTime)
        res = self.driver.page_source
        
        return res
    

if __name__ == "__main__":
    downloader = Downloader()
    txt = downloader.Download("http://27602014.foodmate.net/index.php?m=additives&a=show&faid=250")
    with open("additivePage250.html", "w", encoding="utf-8") as f:
        f.write(txt)

    downloader.driver.quit()