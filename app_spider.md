# APP 爬虫

## 0. 原理及技术路线

获取目标内容，相对 Web 爬虫，移动互联网时代的 APP 爬虫更为重要。尽管一些 APP 都有对应的 Web 网站和官方给出的 API 接口，但相对来自 APP 自身内容来说，还是要少一些的。而目前 APP 绝大多数采用 Restful API 接口服务规范，前后端数据传输为 json 格式，相对于利用 xpath 之类的工具解析 html 文档来获取的结果更为直接高效，甚至一步到位，直接存储到 mongodb 数据库中。

APP 爬虫原理图

![APP 爬虫原理](https://raw.githubusercontent.com/CodeAsPoetry/PublicOpinion/master/images/app_scrapy_steam.png)

代替人滑动、点击等操作，来驱动模拟器，类似 web 爬虫的 selenium，是 appium，其中 Appium Server GUI 是提供图形化界面的服务器，Appium Inspector 便于用户分析 APP 页面元素和操作步骤，和 Appium Server GUI  建立会话，下达驱动指令的

手机模拟器，可以是真实物理机，也可以是移动端模拟器，推荐夜神模拟器，在上面可以下载目标 APP

发送网络请求到 APP 服务，接受其返回数据，并做清洗，推荐 mitmproxy (mitmdump + mitmweb) ，开源，支持 Python 脚本

保存数据到数据库，推荐可以高效存取 json 数据的 mongodb 数据库

## 1. APP 爬虫环境和工具搭建

* 由于这几个工具较大，且都和系统环境打交道，安装过程且稍微有些故障，again 就各种报错，为了一步到位，建议留 10 个G以上的磁盘空间，本人 Mac 开发机，磁盘不大够，腾磁盘空间时，发现“其他”类型占了接近 40 G，推荐一个工具 OmniDiskSweeper，确定其中系统备份占用 20 个 G，删掉它，删掉教程：https://blog.csdn.net/kaixinjiaoluo/article/details/124521994,  mac 开机长按 Command + R，出现白条松开，进入恢复模式，打开终端，执行 csrutil disable ，关闭系统完整性保护(SIP)，重启 reboot。注意，关闭之后最后不要再开，否则后边夜神模拟器会卡在 99% 起不来。

* 下载安装夜神模拟器 (Android)，启动模拟器，发现其 Android 版本为 7.1.2，顺手开启 USB 调试，如果没有这个开关，点击版本号5次开启，教程 https://blog.csdn.net/weixin_38801014/article/details/122983109， 夜神模拟器，Mac 下有个毛病，就是卡在 99% 不动，网上给出的一大堆原因都无法拯救我，后来发现没有正常退出或者删了重装都会很大概率出现，猜测是缓存机制，于是每次重装前，都要到 /Users/xxx/Library/Application\ Support/ 下边把 NoxAppPlayer 和 NoxInstaller 连根拔掉

* 安装 Android Studio，通过 Android Studio 下载 Android SDK 7.0/7.1.1 ，vim .bash_profile 配置环境变量，教程 https://blog.csdn.net/weixin_41271167/article/details/122253261

  ```bash
  export ANDROID_HOME=/Users/xxx/Library/Android/sdk
  export PATH=$PATH:$ANDROID_HOME/tools
  export PATH=$PATH:$ANDROID_HOME/platform-tools
  ```

* 下载安装 Appium Server GUI (https://github.com/appium/appium-desktop) 和 Appium Inspector (https://github.com/appium/appium-inspector)， 启动 Appium Server GUI 时，编辑配置 ANDROID_HOME 和 JAVA_HOME，ANDROID_HOME上述已配置，拷贝下来，mac 已安装 Java 的查看安装路径，教程 https://blog.csdn.net/weixin_42566557/article/details/124377206， 没安装 Java 的，自行安装(应在安装 Android Studio 前就先行安装 Java)

  ```bash
  cd /usr/libexec
  ./java_home
  ```

* Mac 安装Appium Inspector 后(移动到 Applications 目录)前，执行 xattr -cr "/Applications/Appium Inspector.app"，启动报脚本错误，则执行 codesign --deep --sign - /Applications/Appium\ Inspector.app ，教程：https://github.com/appium/appium-desktop#installing-on-macos，重启打开后， Remote Path 配置 /wd/hub，新建会话的四个参数 platformName，appium:deviceName，appium:appPackage， appium:appActivity ，参数值的获取需要 adb 工具，mac 安装 adb 教程：https://www.jianshu.com/p/744fc5946627， 推荐 brew 安装，如果慢的话，换个镜像，亲测不换镜像也挺快的。

  执行：

  ```
  # 连接夜神模拟器
  adb connect 127.0.0.1:62001
  # connected to 127.0.0.1:62001
  # 获取 platformName 和 appium:deviceName 的参数值
  adb devices -l
  # List of devices attached
  # 127.0.0.1:62001        device product:dream2ltexx model:SM_N950N device:dream2lte transport_id:1
  # SM_N950N
  ```

  然后在夜神模拟器上打开目标 APP，执行 adb shell dumpsys window ，找到 mCurrentFocus 对应的信息，确定 appium:appPackage 和 appium:appActivity 参数值，教程： https://blog.csdn.net/wo26466/article/details/118489930 ，以下例子是微信入口：

  ```json
  {
    "platformName": "Android",
    "appium:deviceName": "SM_G930L",
    "appium:appPackage": "com.tencent.mm",
    "appium:appActivity": "com.tencent.mm.plugin.account.ui.WelcomeActivity"
  }
  ```

* 安装 mitmproxy ，直接 pip install ，自动会将 mitmdump + mitmweb 全部安装好，为夜神模拟器添加 Mitmproxy 证书，教程： https://blog.csdn.net/u010132177/article/details/117199579， 不添加证书，夜神模拟器浏览器提醒无证书，无法使用。

  ```bash
  adb devices -l #显示所有已连接的设备详细信息：127.0.0.1：62001
  # 未连接则运行如下命令连接
  adb connect 127.0.0.1:62001 #默认端口 
  
  #PEM或者DER格式均可
  
  # 在.mitmproxy目录下运行
  #如果是PEM格式：
  In: openssl x509 -inform PEM -subject_hash_old -in mitmproxy-ca-cert.pem -noout
  out: c8750f0d
  # 如果是DER格式：
  In: openssl x509 -inform PEM -subject_hash_old -in mitmproxy-ca-cert.cer -noout
  out: c8750f0d
  
  # 重命名，推送手机
  # window重命名 为符合android规范名称
  ren mitmproxy-ca-cert.pem c8750f0d.0
  # 或 linux重命名
  cp mitmproxy-ca-cert.pem c8750f0d.0
  #传入手机
  adb push c8750f0d.0 /sdcard
  
  #获取手机的root权限
  adb shell
  su
  #挂载系统目录为可写
  mount -o rw,remount /
  mv /sdcard/c8750f0d.0 /system/etc/security/cacerts
  #修改证书权限
  chmod 644 /system/etc/security/cacerts/c8750f0d.0
  ```

  * 上述流程走完，Appium Inspector 建立的会话已经通过 Appium Server GUI 将夜游模拟器连接上了，还需将 Mitmproxy 和也神模拟器连接，执行 ifconfig ，获取 Mac 电脑的局域网 IP，即 192.168.x.x 开头，将夜神模拟器配置代理为此 IP，这样，所以通过手机的网络请求和返回的数据都通过 Mitmproxy，Mitmproxy 提供 Python 接口供发送网络请求、接收返回数据、存入数据库中。
  * MongoDB 数据库的安装，下载，配置

  

  ## 2. APP Demo 代码 

  ### Appium Server GUI

  pass

  ### Appium Inspector

  pass

  ### Mitmproxy

  pass

  ### 

  

