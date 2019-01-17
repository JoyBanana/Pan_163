# Pan_163

![](https://img.shields.io/github/last-commit/JoyBanana/Pan_163.svg?style=flat-square)
![](https://img.shields.io/badge/Python-3.0%2B-orange.svg?style=flat-square)
![](https://img.shields.io/github/commit-activity/y/JoyBanana/Pan_163.svg?style=flat-square)


---
:banana: 基于[网易云对象存储](https://www.163yun.com/product/nos) 、`flask` 、`Python3` 做的一个小Demo,适用于小文件的下载、分发。

### Why do this?

:speak_no_evil: 做这个的初衷是能够提升自己的编码能力,了解后端开发。

### How to ues?

#### Step 1. 添加配置文件
:video_game: 您可以 `clone` 此项目，并在根目录创建配置文件 `access.ini` 内容为:
```ini
[Access]
accessKey = your_accessKey
secretKey = your_secretKey
```
您的 `Key` 以在网易云存储 [Access Key](https://c.163yun.com/dashboard#/m/account/accesskey/) 页面可见。

#### Step 2. 安装依赖 & 启动

:coffee: 您可以创建使用虚拟 `Python` 环境来安装运行，如 `virtualenv` ，这里不多赘述。
```python3
pip3 install -r requirement.txt
python3 app.py
```
