import configparser
import os
import nos

# 从配置文件中获取到key
conf = configparser.ConfigParser()
conf.read(os.path.join(os.path.dirname(os.getcwd()), 'access.ini'))
access_key = conf.get('Access', 'accessKey')
secret_key = conf.get('Access', 'secretKey')
end_point = "nos-eastchina1.126.net"
bucket = "joybanana"

client = nos.Client(access_key, secret_key, end_point=end_point)


def getFiles():
    fileList = []
    try:
        object_lists = client.list_objects(bucket)
        for object_list in object_lists["response"].findall("Contents"):
            fileList.append(object_list.find("Key").text)
        return fileList


    except nos.exceptions.ServiceException as e:
        print(
            "status_code: %s\n"
            "error_type: %s\n"
            "error_code: %s\n"
            "request_id: %s\n"
            "message: %s\n"
        ) % (
            e,
            e.status_code,  # 错误http状态码
            e.error_type,  # NOS服务器定义错误类型
            e.error_code,  # NOS服务器定义错误码
            e.request_id,  # 请求ID，有利于nos开发人员跟踪异常请求的错误原因
            e.message  # 错误描述信息
        )
    except nos.exceptions.ClientException as e:
        print(
            "ClientException: %s\n"
            "message: %s\n"
        ) % (
            e,
            e.message  # 客户端错误信息
        )


def deleteFile(filename):
    try:
        client.delete_object(bucket, filename)
    except nos.exceptions.ServiceException as e:
        print(
            "ServiceException: %s\n"
            "status_code: %s\n"
            "error_type: %s\n"
            "error_code: %s\n"
            "request_id: %s\n"
            "message: %s\n"
        ) % (
            e,
            e.status_code,  # 错误http状态码
            e.error_type,  # NOS服务器定义错误类型
            e.error_code,  # NOS服务器定义错误码
            e.request_id,  # 请求ID，有利于nos开发人员跟踪异常请求的错误原因
            e.message  # 错误描述信息
        )
    except nos.exceptions.ClientException as e:
        print(
            "ClientException: %s\n"
            "message: %s\n"
        ) % (
            e,
            e.message  # 客户端错误信息
        )
