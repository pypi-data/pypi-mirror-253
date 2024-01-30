#!/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright (c) 2020 growingio.com, Inc.  All Rights Reserved

import json
import os

from importers.data_import.data_model import EventsCv, EventsJson, DataEvent
from importers.data_import.data_format_util import *
from importers.common import http_util, common_util
from json.decoder import JSONDecodeError
from importers.common.common_util import get_all_file, remove_file, time_str_to_timestamp_of_tz, getVariables, \
    time_format
from importers.common.log_util import logger, my_logger
from importers.common.config_util import BaseConfig, get_temp_dir_from_config
from importers.meta.data_center import getBindEvent, getdataCenterEventVariables, getImportJobStatus, trigger_job

ONE_DAY_MILLISECOND = 86400 * 1000  # 1天(24小时)毫秒值


def events_import(args):
    """
       用户行为导入，按数据格式处理
    """
    # Step one: 校验事件数据基础参数，并预处理
    # 1. 校验时间
    event_start = args.get('event_start')
    if event_start is None:
        logger.error("[-s/--event_start]参数值未指定")
        exit(-1)
    event_end = args.get('event_end')
    if event_end is None:
        logger.error("[-e/--event_end]参数值未指定")
        exit(-1)
    try:
        event_start = time_str_to_timestamp_of_tz(event_start, '%Y-%m-%d', BaseConfig.timezone) * 1000
        event_end = time_str_to_timestamp_of_tz(event_end, '%Y-%m-%d', BaseConfig.timezone) * 1000 + ONE_DAY_MILLISECOND
    except TypeError and ValueError:
        logger.error("[-s/--event_start]或[-e/--event_end]时间参数格式不对,格式为:YYYY-MM-DD")
        exit(-1)
    # 2. 数据源是否为事件
    ds = args.get('datasource_id')
    if 'HISTORY_EVENT' in ds[1]:
        args['datasource_id'] = ds[1]['HISTORY_EVENT']
    else:
        logger.error("数据源不属于用户行为类型")
        exit(-1)
    # Step one: 按数据格式处理
    f = str(args.get('format'))
    if 'JSON'.__eq__(f):
        events_import_json(
            EventsJson(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                       datasourceId=args.get('datasource_id'), eventStart=event_start, eventEnd=event_end,
                       jobName=args.get('jobName'), clear=args.get('clear'))
        )
    elif 'CSV'.__eq__(f):
        separator = args.get("separator")
        separator = ',' if separator == '' else separator
        events_import_sv(
            EventsCv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                     datasourceId=args.get('datasource_id'), attributes=args.get('attributes'),
                     separator=separator, skipHeader=args.get('skip_header'), eventStart=event_start,
                     eventEnd=event_end, jobName=args.get('jobName'), clear=args.get('clear'))
        )
    elif 'TSV'.__eq__(f):
        separator = args.get("separator")
        separator = '\t' if separator == '' else separator
        events_import_sv(
            EventsCv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                     datasourceId=args.get('datasource_id'), attributes=args.get('attributes'), separator=separator,
                     skipHeader=args.get('skip_header'), eventStart=event_start, eventEnd=event_end,
                     jobName=args.get('jobName'), clear=args.get('clear'))

        )


def events_import_sv(eventsCv):
    """
       用户行为导入，CSV/TSV格式数据处理
    """
    # Step 1: 创建临时文件夹，用于存储临时Json文件
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_path = os.path.join(temp_dir, str(int(round(time.time() * 1000))))
    if os.path.exists(current_tmp_path) is False:
        os.makedirs(current_tmp_path)
    my_logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")

    try:
        # Step 2: 校验SV数据，并转为Json格式
        n = 0
        for path in eventsCv.path:
            json_file_abs_path = current_tmp_path + '/' + os.path.basename(path).split('.')[0] + '.json'
            res = sv_import_prepare_process(attributes=eventsCv.attributes,
                                            path=path,
                                            skip_header=eventsCv.skipHeader,
                                            separator=eventsCv.separator,
                                            qualifier=eventsCv.qualifier,
                                            json_file_abs_path=json_file_abs_path)
            if res:
                n = n + 1
        # Step 3: 调用Json导入函数:events_import_json
        if n == len(eventsCv.path):
            events_import_json(
                EventsJson(name='events',
                           path=get_all_file(current_tmp_path),
                           debug=eventsCv.debug,
                           format='JSON',
                           eventStart=eventsCv.eventStart,
                           eventEnd=eventsCv.eventEnd,
                           datasourceId=eventsCv.datasourceId,
                           jobName=eventsCv.jobName,
                           clear=eventsCv.clear)
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

    commonlist = ['userId', 'event', 'timestamp', 'eventId', 'userKey', 'dataSourceId']
    cols = str(attributes).split(',')
    res = [i for i in cols if i not in commonlist]

    event = getBindEvent()
    cstm_keys = {}
    for i in event['dataCenterCustomEvents']:
        list = []
        for a in i['attributes']:
            list.append(a['key'])
        cstm_keys[i['key']] = list

    attr_all = BaseConfig.attr_all
    # Json文件临时存储
    count = 0
    error = 0
    # 获取已定义的事件和事件属性
    cstm_attr_keys = getVariables(getdataCenterEventVariables())
    with open(path, 'r', encoding='utf8') as f:
        with open(json_file_abs_path, 'w') as wf:
            for line in f:
                count += 1
                line = line.replace('\n', '').replace('\\t', '\t')
                if not line == '':
                    # Step 2: 校验数据header列是否一致，数量和顺序
                    if skip_header is True and count == 1:
                        header_normal = True

                        if check_sv_col_duplicate(cols) is not None:
                            header_normal = False
                            logger.error(f"[-attr/--attributes]出现重复列值[{check_sv_col_duplicate(cols)}]")

                        if check_sv_header_col_count(cols, line.split(separator)) is False:
                            logger.error(f"[-attr/--attributes]参数值列数和导入文件[{path}]的列数不一致")
                            header_normal = False

                        if check_sv_header_col_order(cols, line.split(separator)) is False:
                            logger.error(f"[-attr/--attributes]参数值列和导入文件[{path}]的列顺序不一致")
                            header_normal = False

                        if len(check_sv_header_col_value(cols)) > 0:
                            logger.error(f"[-attr/--attributes]参数值需指定{','.join(check_sv_header_col_value(cols))}")
                            header_normal = False
                        else:
                            error_key = []
                            for key in res:
                                if key not in cstm_attr_keys and key not in attr_all:
                                    error_key.append(key)
                            if len(error_key) > 0:
                                logger.error(f"[-attr/--attributes]参数值列:事件属性{error_key}在GIO平台未定义")
                                header_normal = False

                        if not header_normal:
                            logger.error(f"header校验失败！")
                            return
                        continue
                    else:
                        line_normal = True

                        if check_sv_header_col_count(cols, line.split(separator)) is False:
                            logger.error(f"第{count}行:导入文件[{path}]的列数和参数值列数不一致\n")
                            line_normal = False
                            error += 1

                        if not line_normal:
                            continue

                    # Step 3: 转换为JSON格式
                    values = common_util.split_str(line, separator, qualifier)
                    col_value = {}
                    attrs = {}

                    uid = 'anonymousId'
                    if 'userId' in cols:
                        uid = 'userId'

                    for col, value in tuple(zip(cols, values)):
                        if col != '':
                            col_value[col] = value

                    event = col_value['event']
                    if cstm_keys.get(event) is None:
                        logger.error(f"第{count}行:事件[{event}]未在GIO平台定义")
                        error += 1
                    else:
                        common_keys = ['event', 'userKey', 'timestamp', 'eventId', uid]
                        event_attrs = cstm_keys.get(event)
                        for key in col_value:
                            if key not in common_keys:
                                if key in event_attrs or str(key).startswith("$"):
                                    attrs[key] = str(col_value[key])

                        # 检查是否存在 userId 字段
                        if 'userId' not in col_value.keys():
                            userId = ''
                            # 如果不存在 userId，则检查 userKey 字段是否存在且值为 $notuser
                            if 'userKey' not in col_value or col_value['userKey'] != '$notuser':
                                logger.error("缺少userId需指定\n若传主体事件,则数据需字段userKey,且值为‘$notuser’")
                                error += 1
                        else:
                            userId = col_value[uid]

                        if 'userKey' not in col_value.keys():
                            userKey = ''
                        else:
                            userKey = col_value['userKey']

                        if 'eventId' not in col_value.keys():
                            eventId = None
                        else:
                            eventId = col_value["eventId"]

                        if 'dataSourceId' not in col_value.keys():
                            dataSourceId = None
                        else:
                            dataSourceId = col_value['dataSourceId']

                        data_event = DataEvent(userId=userId, event=event, userKey=userKey, eventId=eventId,
                                               timestamp=col_value['timestamp'], attrs=attrs, dataSourceId=dataSourceId)

                        wf.write(json.dumps(data_event.__dict__, ensure_ascii=False))
                        wf.write('\n')
                else:
                    logger.warn(f"第{count}行为空，跳过该行")
    if error > 0:
        logger.warn(f"导入失败，共发现[{error}]个校验错误")
        return False
    else:
        return True


def events_import_json(eventsJson):
    """
       用户行为导入，Json格式数据处理
    """
    # Step 1: 执行Debug
    if eventsJson.debug:
        if events_debug_process(eventsJson.path, eventsJson.eventStart, eventsJson.eventEnd) is not True:
            logger.error("Debug校验未通过")
            exit(-1)
    # Step 2: 创建导入任务
    if len(str(eventsJson.jobName)) == 0 or eventsJson.jobName is None:
        jobName = f"Python_events_{time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))}"
    else:
        jobName = eventsJson.jobName
    job_info = create_task(
        eventsJson.eventStart,
        eventsJson.eventEnd,
        eventsJson.datasourceId,
        jobName)
    # 任务名重复时，获取不到job信息时，程序直接结束
    if job_info is None:
        logger.error("job_info为空，无法创建导入任务")
        exit(-1)
    else:
        my_logger.info(f"创建导入任务: {job_info}")
    direct = job_info['argument']['directory']
    # Step 3: 上传数据到FTP
    my_logger.info(f"文件开始上传至FTP")
    put_file(eventsJson.path, direct)

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
                delete_file(eventsJson.path, direct)
                my_logger.info("执行导入任务耗时:%.3f秒" % cost_time)
                flag = False
            elif stage is not None and stage.__eq__("ERROR"):
                if error is not None:
                    message = error.get('message', 'No message available')
                else:
                    message = 'Error object is None'
                end_time = time.time()
                cost_time = end_time - start_time
                logger.error(f"导入失败,错误信息为[ {message} ] \n FTP文件路径: {direct}")
                my_logger.info("执行导入任务耗时:%.3f秒" % cost_time)
                exit(-1)
        if flag:
            my_logger.info(f"等待任务完成......")
            time.sleep(10)


def create_task(start, end, tid, name):
    """
       创建任务
    """
    if len(str(name)) == 0:
        body = '''{ "operationName":"createEventImportJob", "variables":{ "fileType":"ftp", "tunnelId":"%s", 
        "timeRange":"abs:%s,%s", "createType":"PYTHON" }, "query":"mutation createEventImportJob($tunnelId: HashId!, 
        $timeRange: String, $fileType: String, $createType: String) { createEventImportJob(tunnelId: $tunnelId, 
        timeRange: $timeRange, fileType: $fileType, createType: $createType) { id name argument { directory 
        __typename } __typename } }" }''' % (tid, start, end)
    else:
        body = '''{ "operationName":"createEventImportJob", "variables":{ "fileType":"ftp", "tunnelId":"%s", 
        "timeRange":"abs:%s,%s", "name":"%s", "createType":"PYTHON" }, "query":"mutation createEventImportJob($name: 
        String, $tunnelId: HashId!, $timeRange: String, $fileType: String, $createType: String) { 
        createEventImportJob(name: $name, tunnelId: $tunnelId, timeRange: $timeRange, fileType: $fileType, 
        createType: $createType) { id name argument { directory __typename } __typename } }" }''' % (tid, start, end, name)

    resp = http_util.send_graphql_post(http_util.get_token(), body.encode('utf-8'))
    try:
        return resp['createEventImportJob']
    except TypeError:
        logger.error("自定义任务名称已存在！")


def events_debug_process(paths, eventStart, eventEnd):
    """
       用户行为导入Debug
       1、校验文件的数据内容合法性, 是否缺失必要字段(userId,event,timestamp)
       2、校验文件的数据时间范围合法性
       3、校验自定义事件在GIO平台是否定义
    """
    bind_event = getBindEvent()
    cstm_keys = {}
    for i in bind_event['dataCenterCustomEvents']:
        list = []
        for a in i['attributes']:
            list.append(a['key'])
        cstm_keys[i['key']] = list
    cstm_attr_keys = getVariables(getdataCenterEventVariables())
    count = 0
    error_count = 0
    correct_count = 0  # 正确行数
    for path in paths:
        my_logger.info(f"start check file: {path}")

        # 1 重命名 文件名 加后缀 _tmp
        names = path.rsplit("/", 1)
        path_tmp = path + "_tmp"
        os.rename(path, path_tmp)  # 如果新文件名的文件 存在 则覆盖 ok的

        names2 = names[0].rsplit("/", 1)
        grandpa_path = names2[0]
        father_path = names2[-1]
        error_file_name = names[-1] + '_' + str(int(round(time.time() * 1000))) + "_error"

        # 错误空文件名
        dir_error = f"{grandpa_path}/{father_path}_error"
        path_error = f"{dir_error}/{error_file_name}"
        if not os.path.exists(dir_error):
            os.makedirs(dir_error)

        # 2 打开 每个文件， 加后缀 _tmp 文件
        with open(path_tmp, 'r', encoding='utf8') as f:

            # 打开正确空文件
            with open(path, 'w', encoding='utf8') as f_correct:

                # 打开错误空文件
                with open(path_error, 'w', encoding='utf8') as f_error:
                    current_file_error_lines = 0
                    for line in f:
                        count = count + 1
                        source_line = line  # 把原始行数据 保存到 source_line 变量中，后面判断 正常 异常 ，再写入到相应的文件中
                        line = line.replace('\n', '')
                        if not line == '':
                            try:
                                json_data = json.loads(line.strip())
                            except JSONDecodeError:
                                logger.error(f"第{count}行:文件[{path}]数据[{line}]:\n数据非JSON格式\n")
                                error_count += 1
                                current_file_error_lines += 1
                                f_error.write(source_line)  # 写入异常文件
                                continue

                            data_event, message = extract_and_validate_data(json_data)
                            if data_event is None:
                                logger.error(f"第{count}行:文件[{path}]数据[{line}]\n"
                                             f"{message}")
                                error_count += 1
                                current_file_error_lines += 1
                                f_error.write(source_line)  # 写入异常文件
                                continue

                            # 调用公共校验方法进行校验
                            is_valid, error_message = validate_data_event(data_event, eventStart, eventEnd, cstm_keys,
                                                                          cstm_attr_keys)
                            if not is_valid:  # 异常
                                logger.error(f"第{count}行:文件[{path}]数据[{line}]:\n"
                                             f"{error_message}")
                                error_count += 1
                                current_file_error_lines += 1
                                f_error.write(source_line)  # 写入异常文件
                            else:  # 正常
                                f_correct.write(source_line)  # 写入正常文件
                                correct_count = correct_count + 1
                        else:
                            logger.warn(f"第{count}行为空，跳过该行")
                f_error.close()  # 关闭 异常文件
            f_correct.close()  # 关闭 正常文件
        f.close()  # 关闭 带有后缀 _tmp的文件

        # 删除 带有后缀 _tmp的文件
        os.remove(path_tmp)
        # 判断 若 异常文件空白 行数=0，则 删除 异常文件
        if current_file_error_lines == 0:
            os.remove(path_error)

    # 判断 若 异常 文件夹 空白，则 删除 该文件夹
    if len(os.listdir(dir_error)) == 0:
        os.removedirs(dir_error)

    if error_count == 0:
        my_logger.info(f"本次共校验[{count}]行数据")
    else:
        my_logger.info(f"本次共校验[{count}]行数据,其中校验失败[{error_count}]行数据,异常数据已剪切到如下目录中 {dir_error}")

    if correct_count == 0:
        my_logger.info(f"由于本次正确数据0条，故不生成导数任务。")
        return False
    else:
        return True
