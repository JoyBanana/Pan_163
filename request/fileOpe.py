import nos
from request.initKEY import getClient
from request.tools import *

bucket = "joybanana"
client = getClient()


def getFiles():
    fileList = []
    L = 0
    try:
        object_lists = client.list_objects(bucket)
        for object_list in object_lists["response"].findall("Contents"):
            d = {'Key': object_list.find("Key").text, 'Size': convertFuckSize(int(object_list.find("Size").text)),
                 'LastModified': convertFuckDate(object_list.find("LastModified").text)}
            fileList.append(d)
            L += int(object_list.find("Size").text)
        return fileList, L


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
