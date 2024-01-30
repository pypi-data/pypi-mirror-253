import csv
import json
import tempfile
import os
import requests

from importers.common.config_util import ApiConfig, get_temp_dir_from_config
from importers.common.http_util import get_token
from importers.data_import.data_model import ItemVariablesJson, ItemVariablesSv, DataItem
from importers.data_import.data_format_util import *
from importers.common.common_util import get_all_file, remove_file
from importers.common.log_util import logger
from importers.meta.check_util import check_item_var_key_data_exsit, check_item_var_exsit


def item_variables_import(args):
    """
     维度表导入，按数据格式处理
    """
    # Step one: 按数据格式处理
    f = str(args.get('format'))
    if 'JSON'.__eq__(f):
        item_variables_import_json(
            ItemVariablesJson(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                              itemKey=args.get('item_key'), jobName=args.get('jobName'),
                              clear=args.get('clear'))
        )
    elif 'CSV'.__eq__(f):
        separator = args.get("separator")
        separator = ',' if separator == '' else separator
        item_variables_import_sv(
            ItemVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            itemKey=args.get('item_key'), jobName=args.get('jobName'),
                            attributes=args.get('attributes'), separator=separator, skipHeader=args.get('skip_header'),
                            clear=args.get('clear'))
        )
    elif 'TSV'.__eq__(f):
        separator = args.get("separator")
        separator = '\t' if separator == '' else separator
        item_variables_import_sv(
            ItemVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            itemKey=args.get('item_key'), jobName=args.get('jobName'),
                            attributes=args.get('attributes'), separator=separator, skipHeader=args.get('skip_header'),
                            clear=args.get('clear'))
        )


def item_variables_import_sv(itemVariablesSv):
    """
       维度表导入，CSV,TSV格式数据处理
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
        for path in itemVariablesSv.path:
            json_file_abs_path = current_tmp_path + '/' + itemVariablesSv.itemKey + '.json'
            res = sv_import_prepare_process(attributes=itemVariablesSv.attributes,
                                            path=path,
                                            skip_header=itemVariablesSv.skipHeader,
                                            separator=itemVariablesSv.separator,
                                            qualifier=itemVariablesSv.qualifier,
                                            json_file_abs_path=json_file_abs_path)
            if res:
                n = n + 1
        # Step 3: 调用Json导入函数:item_variables_import_json
        if n == len(itemVariablesSv.path):
            item_variables_import_json(
                ItemVariablesJson(name='item_variables',
                                  path=get_all_file(current_tmp_path),
                                  debug=itemVariablesSv.debug,
                                  format='JSON',
                                  itemKey=itemVariablesSv.itemKey,
                                  jobName=itemVariablesSv.jobName,
                                  clear=itemVariablesSv.clear)
            )
    finally:
        # Step 4: 清理Json临时文件
        remove_file(current_tmp_path)


# SV格式(CSV、TSV)
def sv_import_prepare_process(attributes, path, skip_header, separator, qualifier, json_file_abs_path):
    """
      1.校验数据基本信息
      2.TSV格式数据转换为Json格式导入
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
                        logger.error(f"[-attr/--attributes]参数值列与导入文件[{path}]的列属性值或者顺序不一致")
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
                        if 'item_id'.__eq__(key) is False:
                            if col_value[key] != ' ' and col_value[key] != '\\N' and col_value[key] != '\\n':
                                attrs[key] = col_value[key]
                data_event = DataItem(item_id=col_value['item_id'], attrs=attrs)
                lines.append(json.dumps(data_event.__dict__, ensure_ascii=False) + '\n')
                if len(lines) > 1000:
                    wf.writelines(lines)
                    lines = []
                # wf.write(json.dumps(data_event.__dict__, ensure_ascii=False)+'\n')
            wf.writelines(lines)
            wf.flush()
    return True


def item_variables_import_json(itemVariablesJson):
    """
       维度表，Json格式数据处理
    """
    # Step 1: 执行Debug
    if itemVariablesJson.debug:
        if json_variables_debug_process(itemVariablesJson.path, itemVariablesJson.itemKey) is not True:
            logger.error("Debug校验未通过")
            return

    file = mkd_file()
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_path = os.path.join(temp_dir, str(int(round(time.time() * 1000))))
    if os.path.exists(current_tmp_path) is False:
        os.makedirs(current_tmp_path)
    logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")

    new_json = os.path.join(current_tmp_path, f"{itemVariablesJson.itemKey}.json")
    # 处理和合并JSON内容
    json_contents = []

    for path in itemVariablesJson.path:
        if os.path.isdir(path):
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)

                with open(file_path) as f:
                    lines = f.readlines()  # 逐行读取文件内容

                for line in lines:
                    try:
                        content = json.loads(line)  # 从每一行加载JSON内容
                        json_contents.append(content)
                    except json.JSONDecodeError as e:
                        print(f"JSON 解析错误: {str(e)}")
        elif os.path.isfile(path):
            file_path = path
            try:
                with open(file_path) as f:
                    lines = f.readlines()

                for line in lines:
                    try:
                        content = json.loads(line)
                        json_contents.append(content)
                    except json.JSONDecodeError as e:
                        print(f"JSON 解析错误: {str(e)}")
            except json.JSONDecodeError as e:
                print(f"JSON 解析错误: {str(e)}")
                continue
        else:
            print(f"{path}不是一个有效路径")

    # 将合并后的JSON内容写入新的JSON文件，逐行写入
    with open(new_json, 'w') as f:
        for content in json_contents:
            json.dump(content, f, ensure_ascii=False)
            f.write('\n')  # 在每个JSON对象后面添加换行符

    # 上传FTP
    put_file([new_json], file)
    # Step 4: 清理Json临时文件
    remove_file(current_tmp_path)
    last_json = file + '/' + f"{itemVariablesJson.itemKey}.json"
    importer_job(last_json, "json")

    if itemVariablesJson.clear:
        delete_file([new_json], file)


def importer_job(path, fileType):
    """
     创建任务
    """
    global instanceId
    job_time = str(int(round(time.time() * 1000)))
    body = {
        "pipelineDefinitionId": "ImportHistoryPipeline",
        "identity": "gio",
        "conf": {
            "$projectId": ApiConfig.project_id,
            "$jobId": job_time,
            "$jobType": "HISTORY_ITEM",
            "$fileType": fileType,
            "$ftpPath": path,
            "$beginTime": " ",
            "$endTime": " ",
            "$dataSourceId": " "
        }
    }
    url = "/data-server/scheduler/pipeline/running"
    headers = {'Content-Type': 'application/json', 'Authorization': get_token()}
    resp = requests.post(ApiConfig.oauth2_uri + url, headers=headers, data=json.dumps(body))
    if resp.status_code == 200:
        logger.info("导入维度表数据任务提交成功")
        url = "/data-server/scheduler/pipeline/instance-status"
        content = json.loads(resp.content)
        for contend in content:
            run_id_value = contend['runId']
            if isinstance(run_id_value, str):
                instanceId = run_id_value
        body = {
            "pipelineDefinitionId": "ImportHistoryPipeline",
            "identity": "gio",
            "projectId": ApiConfig.project_id,
            "instanceId": instanceId
        }
        logger.info("正在导入维度表数据....")
        while True:
            rests = requests.post(ApiConfig.oauth2_uri + url, headers=headers, data=json.dumps(body))
            content = json.loads(rests.content)
            status = content['status']
            if status == 'success':
                logger.info("维度表数据导入完成")
                break
            elif status == 'failed':
                logger.error("导入维度表数据执行失败")
                break
            time.sleep(5)
    else:
        logger.info("导入维度表数据任务提交失败,错误:" + resp.text)


def json_variables_debug_process(paths, itemKey):
    """
    维度表导入Debug
    1、校验有无itemKey
    2、校验维度表(条件:是否是平台内置和是否定义)
    """
    count = 0
    error_count = 0
    correct_count = 0  # 正确行数
    flag, var_id, var_name, var_desc = check_item_var_exsit(ApiConfig.token, itemKey)
    if flag:
        key_list = check_item_var_key_data_exsit(ApiConfig.token, var_id)
    else:
        logger.error(f"item_Key维度表标识符[{itemKey}]不存在，校验终止")
        return False  # 直接退出校验并返回 False
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_name = str(int(round(time.time() * 1000))) + "_error"
    current_tmp_path = os.path.join(temp_dir, current_tmp_name)
    if not os.path.exists(current_tmp_path):
        os.makedirs(current_tmp_path)
    for path in paths:
        # Define error file path
        error_file_name = 'item_' + str(int(round(time.time() * 1000))) + '_error.json'
        error_path = current_tmp_path + '/' + error_file_name

        with open(path, 'r', encoding='utf8') as f:
            with open(error_path, 'w', encoding='utf8') as f_error:
                lines_to_write = []  # Collect lines to write back to original file
                for line in f:
                    count = count + 1
                    line = line.replace('\n', '')
                    if not line == '':
                        normal = True
                        error_message = ""
                        try:
                            data_dictionary = json.loads(line)
                            # item_id
                            if 'item_id' not in data_dictionary:
                                normal = False
                                error_message += f"item_id不存在\n"
                            # 维度表
                            if 'attrs' in data_dictionary:
                                if not isinstance(data_dictionary['attrs'], dict):
                                    normal = False
                                    error_message += f"attrs数据格式不对\n"
                                for key in data_dictionary['attrs']:
                                    if key not in key_list:
                                        normal = False
                                        error_message += f"维度表字段[{key}]不存在\n"
                                    elif data_dictionary['attrs'][key] is None or data_dictionary['attrs'][key] == "":
                                        print(f"维度表[{data_dictionary['item_id']}]中字段[{key}]的值为空或为NULL,请检查原始数据\n")
                        except json.JSONDecodeError:
                            normal = False
                            error_message += f"文件[{path}]数据[{line}]非JSON格式\n"

                        if not normal:  # 异常
                            logger.error(f"第{count}行:文件[{path}]数据[{line}],\n"
                                         f"{error_message}")
                            error_count += 1
                            f_error.write(line + '\n')  # 写入异常数据到错误文件
                        else:  # 正常
                            lines_to_write.append(line)  # 添加到待写入的行列表
                            correct_count = correct_count + 1

                    else:
                        logger.warn(f"第{count}行为空，跳过该行")

                # Write valid lines back to the original file
                with open(path, 'w', encoding='utf8') as f_original:
                    for line in lines_to_write:
                        f_original.write(line + '\n')

        f_error.close()  # 关闭错误文件
        f.close()  # 关闭原始文件
        # 判断 若 异常文件空白 行数=0，则 删除 异常文件
        if error_count == 0:
            os.remove(error_path)
    if len(os.listdir(current_tmp_path)) == 0:
        os.removedirs(current_tmp_path)

    if error_count == 0:
        logger.info(f"本次共校验[{count}]行数据")
    else:
        logger.info(f"本次共校验[{count}]行数据,其中校验失败[{error_count}]行数据,异常数据已剪切到临时文件目录[{current_tmp_path}]")

    if correct_count == 0:
        logger.info(f"由于本次正确数据0条，故不生成导数任务。")
        return False
    else:
        return True
