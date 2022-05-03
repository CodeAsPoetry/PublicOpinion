# APP 爬虫

## 0. 原理及技术路线

获取目标内容，相对 Web 爬虫，移动互联网时代的 APP 爬虫更为重要。尽管一些 APP 都有对应的 Web 网站和官方给出的 API 接口，但相对来自 APP 自身内容来说，还是要少一些的。而目前 APP 绝大多数采用 Restful API 接口服务规范，前后端数据传输为 json 格式，相对于利用 xpath 之类的工具解析 html 文档来获取的结果更为直接高效，甚至一步到位，直接存储到 mongodb 数据库中。

APP 爬虫原理图

![APP 爬虫原理](https://github.com/CodeAsPoetry/PublicOpinion/blob/master/images/app_scrapy_steam.png)

代替人滑动、点击等操作，来驱动模拟器，类似 web 爬虫的 selenium，是 appium，其中 Appium Server GUI 是提供图形化界面的服务器，Appium Inspector 便于用户分析 APP 页面元素和操作步骤，和 Appium Server GUI  建立会话，下达驱动指令的

手机模拟器，可以是真实物理机，也可以是移动端模拟器，推荐夜神模拟器，在上面可以下载目标 APP

发送网络请求到 APP 服务，接受其返回数据，并做清洗，推荐 mitmproxy (mitmdump + mitmweb) ，开源，支持 Python 脚本

保存数据到数据库，推荐可以高效存取 json 数据的 mongodb 数据库

## 1. APP 爬虫环境和工具搭建



