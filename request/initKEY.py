import os
import nos
import configparser


def getClient():
    conf = configparser.ConfigParser()
    conf.read(os.path.join(os.getcwd(), "access.ini"))
    access_key = conf.get('Access', 'accessKey')
    secret_key = conf.get('Access', 'secretKey')
    end_point = "nos-eastchina1.126.net"
    client = nos.Client(access_key, secret_key, end_point=end_point)
    return client
