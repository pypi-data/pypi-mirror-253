#!/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2020 growingio.com, Inc.  All Rights Reserved
import csv
import json
import os

from importers.common.config_util import get_temp_dir_from_config
from importers.data_import.data_model import UserVariablesSv, UserVariablesJson, DataUser
from importers.data_import.data_format_util import *
from importers.common import http_util
from importers.common.common_util import get_all_file, remove_file, getVariables
from importers.common.log_util import logger, my_logger
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
        exit(-1)
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
    my_logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")
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
        exit(-1)

    cols = str(attributes).split(',')
    duplicate_col = check_sv_col_duplicate(cols)
    if duplicate_col is not None:
        logger.error(f"[-attr/--attributes]出现重复列值[{duplicate_col}]")
        exit(-1)

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
                        exit(-1)
                    if check_sv_header_col_order(cols, line) is False:
                        logger.error(f"[-attr/--attributes]参数值列与导入文件[{path}]的列顺序不一致")
                        exit(-1)
                    skip_header = False
                    continue
                # Step 3: 校验数据列是否一致
                values = line
                if len(cols) != len(values):
                    logger.error(f"文件[{path}]数据[{line}]列数与文件头部列数不一致")
                    exit(-1)
                # Step 4: 转换为JSON格式
                col_value = {}
                for col, value in tuple(zip(cols, values)):
                    if col != '':
                        col_value[col] = str(value)

                # 新增的处理userKey逻辑
                user_key = col_value.get('userKey', '')
                if 'userKey' in cols:
                    if user_key == '$notuser':
                        logger.error(f"文件[{path}]数据[{line}]中的userKey值不合法，用户属性导入不支持用户身份为‘$notuser’")
                        exit(-1)

                attrs = {}
                for key, value in col_value.items():
                    if len(str(value)) != 0:
                        if key not in ['userKey', 'userId']:
                            if key.startswith('$') is False and key not in keys:
                                logger.error(f"文件[{path}]数据[{line}]用户属性[{key}]在GIO平台未定义")
                                exit(-1)
                            elif 'userId'.__eq__(key) is False:
                                if col_value[key] != ' ' and col_value[key] != '\\N' and col_value[key] != '\\n':
                                    attrs[key] = col_value[key]
                    # 更新DataUser对象，考虑userKey字段
                data_event = DataUser(userId=col_value['userId'], userKey=user_key, attrs=attrs)
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
            exit(-1)
    # Step 2: 创建导入任务
    if len(str(userVariablesJson.jobName)) == 0 or userVariablesJson.jobName is None:
        jobName = f"Python_user_{time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))}"
    else:
        jobName = userVariablesJson.jobName
    job_info = create_task(userVariablesJson.datasourceId, jobName)
    # 任务名重复时，获取不到job信息时，程序直接结束
    if job_info is None:
        logger.error("job_info为空，无法创建导入任务")
        exit(-1)
    else:
        my_logger.info(f"创建导入任务: {job_info}")
    direct = job_info['argument']['directory']
    # Step 3: 上传数据到FTP
    my_logger.info(f"文件开始上传至FTP")
    put_file(userVariablesJson.path, direct)

    # Step 4: 启动导入任务
    start_time = time.time()
    trigger_job(job_info['id'])
    my_logger.info(f"开始执行导入任务")
    flag = True
    while flag:
        eventImportJob = getImportJobStatus(job_info['id'])
        if eventImportJob is not None:
            stage = eventImportJob['stage']
            error = eventImportJob['error']
            if stage is not None and stage.__eq__("FINISH"):
                end_time = time.time()
                cost_time = end_time - start_time
                my_logger.info("导入成功")
                delete_file(userVariablesJson.path, direct)
                my_logger.info("执行导入任务耗时:%.3f秒" % cost_time)
                flag = False
            elif stage is not None and stage.__eq__("ERROR"):
                end_time = time.time()
                cost_time = end_time - start_time
                if error is not None:
                    message = error.get('message', 'No message available')
                else:
                    message = 'Error object is None'
                logger.error(f"导入失败,错误信息为[ {message} ] \n FTP文件路径: {direct}")
                my_logger.info("执行导入任务耗时:%.3f秒" % cost_time)
                exit(-1)
        if flag:
            my_logger.info(f"等待任务完成......")
            time.sleep(10)


def create_task(ds, name):
    """
           创建任务,允许用户自定义更改任务名称
        """
    if len(str(name)) == 0:
        body = '''{ "operationName": "createEventImportJob", "variables": { "fileType":"ftp", "timeRange":"", 
        "tunnelId": "%s", "createType":"PYTHON" }, "query": "mutation createEventImportJob($tunnelId: HashId!, 
        $timeRange: String, $fileType: String, $createType: String) { createEventImportJob(tunnelId: $tunnelId, 
        timeRange: $timeRange,fileType: $fileType, createType: $createType) { id name argument { directory __typename 
        } __typename } }" }''' % ds
    else:
        body = '''{ "operationName":"createEventImportJob", "variables":{ "fileType":"ftp", "tunnelId":"%s", 
        "timeRange":"", "name":"%s", "createType":"PYTHON" }, "query":"mutation createEventImportJob($name: String, 
        $tunnelId: HashId!, $timeRange: String, $fileType: String, $createType: String) { createEventImportJob(name: 
        $name, tunnelId: $tunnelId, timeRange: $timeRange, fileType: $fileType, createType: $createType) { id name 
        argument { directory __typename } __typename } }" }''' % (ds, name)
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

                        if 'userKey' in data_dictionary:
                            if data_dictionary['userKey'] == '$notuser':
                                normal = False
                                error_message += f"用户属性导入不支持用户身份为‘$notuser’\n"

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
        my_logger.info(f"本次共校验[{count}]行数据")
        return True
    else:
        my_logger.info(f"本次共校验失败[{error_count}]行数据")
        return False
