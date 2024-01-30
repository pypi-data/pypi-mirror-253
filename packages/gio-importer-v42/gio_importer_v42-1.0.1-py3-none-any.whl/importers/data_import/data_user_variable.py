#!/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2020 growingio.com, Inc.  All Rights Reserved
import csv
import time
import json
import tempfile
import os

from importers.common.config_util import get_temp_dir_from_config
from importers.common.http_util import put_file_ftp, put_file_hdfs
from importers.data_import.data_model import UserVariablesSv, UserVariablesJson, DataUser
from importers.data_import.data_format_util import *
from importers.common import http_util, common_util
from importers.common.common_util import get_all_file, remove_file, getVariables
from importers.common.log_util import logger
from json.decoder import JSONDecodeError
from importers.meta.data_center import getdataCenterUserVariables, getImportJobStatus, trigger_job


def user_variables_import(args):
    """
       用户属性导入，按数据格式处理
    """
    # Step one: 校验事件数据基础参数，并预处理
    # 1. 数据源是否为属性
    ds = args.get('datasource_id')
    if 'USER_PROPERTY' in ds[1]:
        args['datasource_id'] = ds[1]['USER_PROPERTY']
    else:
        logger.error("数据源不属于用户属性类型")
        return
    # Step one: 按数据格式处理
    f = str(args.get('format'))
    if 'JSON'.__eq__(f):
        user_variables_import_json(
            UserVariablesJson(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                              datasourceId=args.get('datasource_id'), jobName=args.get('jobName'),
                              clear=args.get('clear'))
        )
    elif 'CSV'.__eq__(f):
        separator = args.get("separator")
        separator = ',' if separator == '' else separator
        user_variables_import_sv(
            UserVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            datasourceId=args.get('datasource_id'), jobName=args.get('jobName')
                            , attributes=args.get('attributes'), separator=separator,
                            skipHeader=args.get('skip_header'), clear=args.get('clear'))
        )
    elif 'TSV'.__eq__(f):
        separator = args.get("separator")
        separator = '\t' if separator == '' else separator
        user_variables_import_sv(
            UserVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            datasourceId=args.get('datasource_id'), jobName=args.get('jobName'),
                            attributes=args.get('attributes'), separator=separator, skipHeader=args.get('skip_header'),
                            clear=args.get('clear'))
        )


def user_variables_import_sv(userVariablesSv):
    """
       用户属性导入，CSV/TSV格式数据处理
    """
    # Step 1: 创建临时文件夹，用于存储临时Json文件
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_path = os.path.join(temp_dir, str(int(round(time.time() * 1000))))
    if os.path.exists(current_tmp_path) is False:
        os.makedirs(current_tmp_path)
    logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")
    try:
        # Step 2: 校验SV数据，并转为为Json个数
        n = 0
        for path in userVariablesSv.path:
            json_file_abs_path = current_tmp_path + '/' + os.path.basename(path).split('.')[0] + '.json'
            res = sv_import_prepare_process(attributes=userVariablesSv.attributes,
                                            path=path,
                                            skip_header=userVariablesSv.skipHeader,
                                            separator=userVariablesSv.separator,
                                            qualifier=userVariablesSv.qualifier,
                                            json_file_abs_path=json_file_abs_path)
            if res:
                n = n + 1
        # Step 3: 调用Json导入函数:user_variables_import_json
        if n == len(userVariablesSv.path):
            user_variables_import_json(
                UserVariablesJson(name='user_variables',
                                  path=get_all_file(current_tmp_path),
                                  debug=userVariablesSv.debug,
                                  format='JSON',
                                  datasourceId=userVariablesSv.datasourceId,
                                  jobName=userVariablesSv.jobName,
                                  clear=userVariablesSv.clear)
            )
    finally:
        # Step 4: 清理Json临时文件
        remove_file(current_tmp_path)


# SV格式(CSV、TSV)
def sv_import_prepare_process(attributes, path, skip_header, separator, qualifier, json_file_abs_path):
    """
      1.校验数据基本信息
      2.SV格式数据转换为Json格式导入
    """
    # Step 1: 校验有无attributes,有无重复列名
    if attributes is None:
        logger.error(f"[-attr/--attributes]参数值不存在")
        return

    cols = str(attributes).split(',')
    duplicate_col = check_sv_col_duplicate(cols)
    if duplicate_col is not None:
        logger.error(f"[-attr/--attributes]出现重复列值[{duplicate_col}]")
        return

    keys = getVariables(getdataCenterUserVariables())
    with open(path, 'r', encoding='utf8') as f:
        with open(json_file_abs_path, 'w') as wf:
            csv_reader = csv.reader(f, delimiter=separator, quotechar=qualifier)
            lines = []
            for line in csv_reader:
                # Step 2: 校验数据header列是否一致，数量和顺序
                if skip_header is True:
                    if check_sv_header_col_count(cols, line) is False:
                        logger.error(f"[-attr/--attributes]参数值列与导入文件[{path}]的列数不一致")
                        return
                    if check_sv_header_col_order(cols, line) is False:
                        logger.error(f"[-attr/--attributes]参数值列与导入文件[{path}]的列顺序不一致")
                        return
                    skip_header = False
                    continue
                # Step 3: 校验数据列是否一致
                values = line
                if len(cols) != len(values):
                    logger.error(f"文件[{path}]数据[{line}]列数与文件头部列数不一致")
                    return
                # Step 4: 转换为JSON格式
                col_value = {}
                for col, value in tuple(zip(cols, values)):
                    if col != '':
                        col_value[col] = str(value)
                attrs = {}
                for key, value in col_value.items():
                    if len(str(value)) != 0:
                        if key.startswith('$') is False and key not in keys \
                                and 'userId'.__eq__(key) is False:
                            logger.error(f"文件[{path}]数据[{line}]用户属性[{key}]在GIO平台未定义")
                            return
                        elif 'userId'.__eq__(key) is False:
                            if col_value[key] != ' ' and col_value[key] != '\\N' and col_value[key] != '\\n':
                                attrs[key] = col_value[key]
                data_event = DataUser(userId=col_value['userId'], userKey='', attrs=attrs)
                lines.append(json.dumps(data_event.__dict__, ensure_ascii=False) + '\n')
                if len(lines) > 1000:
                    wf.writelines(lines)
                    lines = []
                # wf.write(json.dumps(data_event.__dict__, ensure_ascii=False)+'\n')
            wf.writelines(lines)
            wf.flush()
    return True


def user_variables_import_json(userVariablesJson):
    """
       用户属性导入，Json格式数据处理
    """
    # Step 1: 执行Debug
    if userVariablesJson.debug:
        if user_variables_debug_process(userVariablesJson.path) is not True:
            logger.error("Debug校验未通过")
            return
    # Step 2: 创建导入任务
    job_info = create_task(userVariablesJson.datasourceId, userVariablesJson.jobName)
    # 任务名重复时，获取不到job信息时，程序直接结束
    if job_info is None:
        return
    logger.info(f"创建导入任务: {job_info}")
    # Step 3: 上传数据到FTP
    put_file(userVariablesJson.path, job_info['argument']['directory'])
    # ftp_path = job_info['argument']['directory'] + '/'
    # put_file_ftp(userVariablesJson.path, ftp_path)
    # ftp_path = FTPConfig.namespace + job_info['argument']['directory']
    # put_file_hdfs(userVariablesJson.path, ftp_path)
    # Step 4: 启动导入任务
    trigger_job(job_info['id'])
    flag = True
    while flag:
        if getImportJobStatus(job_info['id']):
            flag = False
        else:
            logger.info(f"等待任务完成......")
            time.sleep(30)


def create_task(ds, name):
    """
           创建任务,允许用户自定义更改任务名称
        """
    if len(str(name)) == 0:
        body = '''{
              "operationName": "createEventImportJob",
              "variables": {
                "fileType":"ftp",
                "timeRange":"",
                "tunnelId": "%s"
              },
              "query": "mutation createEventImportJob($tunnelId: HashId!, $timeRange: String, $fileType: String) {
                createEventImportJob(tunnelId: $tunnelId, timeRange: $timeRange,fileType: $fileType) {
                  id
                  name
                  argument {
                    directory
                    __typename
                  }
                  __typename
                }
              }"
            }''' % ds
    else:
        body = '''{
                "operationName":"createEventImportJob",
                "variables":{
                    "fileType":"ftp",
                    "tunnelId":"%s",
                    "timeRange":"",
                    "name":"%s"
                    },
                    "query":"mutation createEventImportJob($name: String, $tunnelId: HashId!, $timeRange: String, $fileType: String) {
                  createEventImportJob(name: $name, tunnelId: $tunnelId, timeRange: $timeRange, fileType: $fileType) {
                    id
                    name
                    argument {
                        directory
                        __typename
                    }
                    __typename
                }
            }"
        }''' % (ds, name)
    resp = http_util.send_graphql_post(http_util.get_token(), body.encode('utf-8'))
    try:
        return resp['createEventImportJob']
    except TypeError:
        logger.error("自定义任务名称已存在！")


def user_variables_debug_process(paths):
    """
       用户属性导入Debug
       1、校验有无userId
       2、校验用户属性(条件:是否是平台内置和是否定义)
    """
    keys = getVariables(getdataCenterUserVariables())
    count = 0
    error_count = 0
    for path in paths:
        with open(path, 'r', encoding='utf8') as f:
            for line in f:
                count = count + 1
                line = line.replace('\n', '')
                if not line == '':
                    normal = True
                    error_message = ""
                    try:
                        data_dictionary = json.loads(line)
                        # userId或anonymousId
                        if 'userId' not in data_dictionary:
                            normal = False
                            error_message += f"userId不存在\n"

                        # 用户属性
                        if 'attrs' in data_dictionary:
                            if not isinstance(data_dictionary['attrs'], dict):
                                normal = False
                                error_message += f"attrs数据格式不对\n"

                            for key in data_dictionary['attrs']:
                                if data_dictionary['attrs'][key] is None:
                                    normal = False
                                    error_message += f"用户属性[{key}]的值为NULL,请检查原始数据\n"

                                if key not in keys:
                                    normal = False
                                    error_message += f"用户属性[{key}]在GIO平台未定义\n"

                    except JSONDecodeError:
                        normal = False
                        error_message += f"非JSON格式\n"

                    if not normal:
                        logger.error(f"第{count}行:文件[{path}]数据[{line}],\n"
                                     f"{error_message}")
                        error_count += 1
                else:
                    logger.warn(f"第{count}行为空，跳过该行")
        f.close()

    if error_count == 0:
        logger.info(f"本次共校验[{count}]行数据")
        return True
    else:
        logger.info(f"本次共校验失败[{error_count}]行数据")
        return False
