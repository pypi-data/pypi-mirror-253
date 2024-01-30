#!/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2020 growingio.com, Inc.  All Rights Reserved

import ftplib
import time

from importers.common.config_util import FTPConfig

from collections import Counter

from importers.common.log_util import logger


def check_sv_header_col_value(attr_header_list):
    """
       校验CSV/TSV格式数据头-固定列数的值
    """
    error_list = []

    if attr_header_list[0] not in ['userId', 'anonymousId']:
        error_list.append('userId/anonymousId')

    if attr_header_list[1] != 'event':
        error_list.append('event')

    if attr_header_list[2] != 'timestamp':
        error_list.append('timestamp')

    return error_list


def check_sv_header_col_count(attr_header_list, data_header_list):
    """
       校验CSV/TSV格式数据头-列数
    """
    if len(attr_header_list) != len(data_header_list):
        return False


def check_sv_header_col_order(attr_header_list, data_header_list):
    """
       校验CSV/TSV格式数据头-不为''的顺序
    """
    try:
        for i in range(len(attr_header_list)):
            if attr_header_list[i] != '' and attr_header_list[i] != data_header_list[i]:
                return False
    except Exception:
        return False


def check_sv_col_duplicate(data_list):
    """
       校验CSV/TSV格式数据列名是否重复
    """
    for item in Counter([i for i in data_list if i != '']).items():
        if item[1] > 1:
            return item[0]


def mkd_file():
    """
    FTP创建目录
    :target_directory: 目标目录
    :return:
    """
    ftp = ftplib.FTP()
    ftp.connect(host=FTPConfig.host, port=int(FTPConfig.port))
    ftp.login(user=FTPConfig.user, passwd=FTPConfig.password)
    target_directory = ftp.mkd('/jobs/importer/' + str(int(round(time.time() * 1000))))
    ftp.close()
    return target_directory


def put_file(file_list, target_directory):
    """
    FTP上传文件
    :param file_list: 待上传文件列表
    :param target_directory: 目标目录
    :return:
    """
    ftp = ftplib.FTP()
    ftp.connect(host=FTPConfig.host, port=int(FTPConfig.port))
    ftp.login(user=FTPConfig.user, passwd=FTPConfig.password)
    for file in file_list:
        file_splits = file.split('/')
        simple_name = file_splits[len(file_splits) - 1]
        with open(file, 'rb') as fp:
            cmd = 'STOR %s/%s' % (target_directory, simple_name)
            ftp.storbinary(cmd, fp)
    ftp.close()


def delete_file(file_list, target_directory):
    ftp = ftplib.FTP()
    ftp.connect(host=FTPConfig.host, port=int(FTPConfig.port))
    ftp.login(user=FTPConfig.user, passwd=FTPConfig.password)
    for file in file_list:
        file_splits = file.split('/')
        simple_name = file_splits[len(file_splits) - 1]
        ftp.delete('%s/%s' % (target_directory, simple_name))
    ftp.close()
