# FoodStandardGetter
> [!WARN]牢底坐穿警告
>> User-agent: *
>>
>> Disallow: /api/
>>
>> Disallow: /member/
>>
>> Disallow: /skin/
>>
>> Disallow: /template/
>>
> 这是网站的声明，意思是这三个目录的内容不允许爬取，写程序的时候注意一下。

Python 爬虫架构主要由五个部分组成，分别是调度器、URL管理器、网页下载器、网页解析器、应用程序（爬取的有价值数据）。

调度器：相当于一台电脑的CPU，主要负责调度URL管理器、下载器、解析器之间的协调工作。
- 调度器（Scheduler）：调度各个程序
- URL管理器（UrlManager）：包括待爬取的URL地址和已爬取的URL地址，防止重复抓取URL和循环抓取URL，实现URL管理器主要用三种方式，通过内存、数据库、缓存数据库来实现。
- 网页下载器（Downloader）：通过传入一个URL地址来下载网页，将网页转换成一个字符串，网页下载器有urllib2（Python官方基础模块）包括需要登录、代理、和cookie，requests(第三方包)
- 网页解析器（Parser）：将一个网页字符串进行解析，可以按照我们的要求来提取出我们有用的信息，也可以根据DOM树的解析方式来解析。网页解析器有正则表达式（直观，将网页转成字符串通过模糊匹配的方式来提取有价值的信息，当文档比较复杂的时候，该方法提取数据的时候就会非常的困难）、html.parser（Python自带的）、beautifulsoup（第三方插件，可以使用Python自带的html.parser进行解析，也可以使用lxml进行解析，相对于其他几种来说要强大一些）、lxml（第三方插件，可以解析 xml 和 HTML），html.parser 和 beautifulsoup 以及 lxml 都是以 DOM 树的方式进行解析的。
- 应用程序（）

根目录URL：http://27602014.foodmate.net/index.php?m=additives&a=category
# Scheduler
调度器是主程序，负责调度各个部分进行工作。调度器需要这样做：
1. 从网站根目录开始进行搜索，分两步：
    1. 按照添加剂查询，搜寻所有链接，放进UrlManager，建立添加剂表（包含中文名、英文名、功能、质量规格标准、CNS号、INS号*、备注），建立添加剂-食品表
    2. 按照食品名称查询，搜寻所有链接，建立食品表（包含食品分类号*、食品名称、食品名称描述）
2. 获取的信息存储到pandas表中
3. 

# UrlManager

