# pan_163
基于163对象存储、`flask` 、`Python3` 做的一个小Demo

### Why do this?

做这个的初衷是能够提升自己的编码能力,了解后端开发。

### How to ues?

#### Step 1. 添加配置文件
您可以 `clone` 此项目，并在根目录创建配置文件 `access.ini` 内容为:
```ini
[Access]
accessKey = your_accessKey
secretKey = your_secretKey
```
您的 `Key` 以在网易云存储 <a href="https://c.163yun.com/dashboard#/m/account/accesskey/">Access Key</a> 页面可见。

#### Step 2. 安装依赖 & 启动

您可以创建使用虚拟 `Python` 环境来安装运行，如 `virtualenv` ，这里不多赘述。
```python3
pip3 install -r requirement.txt
python3 app.py
```
