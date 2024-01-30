import csv
import json
import os

from importers.common import http_util
from importers.common.config_util import ApiConfig, get_temp_dir_from_config
from importers.data_import.data_model import ItemVariablesJson, ItemVariablesSv, DataItem
from importers.data_import.data_format_util import *
from importers.common.common_util import get_all_file, remove_file
from importers.common.log_util import logger, my_logger
from importers.meta.check_util import check_item_var_key_data_exsit, check_item_var_exsit
from importers.meta.data_center import trigger_job, getImportJobStatus


def item_variables_import(args):
    """
     主体导入，按数据格式处理
    """
    ds = args.get('datasource_id')
    if 'HISTORY_ITEM' in ds[1]:
        args['datasource_id'] = ds[1]['HISTORY_ITEM']
    else:
        logger.error("数据源不属于主体数据类型")
        exit(-1)
    # Step one: 按数据格式处理
    f = str(args.get('format'))
    if 'JSON'.__eq__(f):
        item_variables_import_json(
            ItemVariablesJson(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                              datasourceId=args.get('datasource_id'), itemKey=args.get('item_key'), jobName=args.get('jobName'),
                              clear=args.get('clear'))
        )
    elif 'CSV'.__eq__(f):
        separator = args.get("separator")
        separator = ',' if separator == '' else separator
        item_variables_import_sv(
            ItemVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            datasourceId=args.get('datasource_id'), itemKey=args.get('item_key'), jobName=args.get('jobName'),
                            attributes=args.get('attributes'), separator=separator, skipHeader=args.get('skip_header'),
                            clear=args.get('clear'))
        )
    elif 'TSV'.__eq__(f):
        separator = args.get("separator")
        separator = '\t' if separator == '' else separator
        item_variables_import_sv(
            ItemVariablesSv(name=args.get('m'), path=args.get('path'), debug=args.get('debug'), format=f,
                            datasourceId=args.get('datasource_id'), itemKey=args.get('item_key'), jobName=args.get('jobName'),
                            attributes=args.get('attributes'), separator=separator, skipHeader=args.get('skip_header'),
                            clear=args.get('clear'))
        )


def item_variables_import_sv(itemVariablesSv):
    """
       主体导入，CSV,TSV格式数据处理
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
                                  datasourceId=itemVariablesSv.datasourceId,
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
        exit(-1)

    cols = str(attributes).split(',')
    duplicate_col = check_sv_col_duplicate(cols)
    if duplicate_col is not None:
        logger.error(f"[-attr/--attributes]出现重复列值[{duplicate_col}]")
        exit(-1)

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
                        logger.error(f"[-attr/--attributes]参数值列与导入文件[{path}]的列属性值或者顺序不一致")
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
       主体，Json格式数据处理
    """
    # Step 1: 执行Debug
    if itemVariablesJson.debug:
        if json_variables_debug_process(itemVariablesJson.path, itemVariablesJson.itemKey) is not True:
            logger.error("Debug校验未通过")
            exit(-1)
    # Step 2: 创建导入任务
    if len(str(itemVariablesJson.jobName)) == 0 or itemVariablesJson.jobName is None:
        jobName = f"Python_item_{time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))}"
    else:
        jobName = itemVariablesJson.jobName
    itemKey = itemVariablesJson.itemKey
    job_info = create_task(itemVariablesJson.datasourceId, jobName, itemKey)
    # 任务名重复时，获取不到job信息时，程序直接结束
    if job_info is None:
        logger.error("job_info为空，无法创建导入任务")
        exit(-1)
    else:
        my_logger.info(f"创建导入任务: {job_info}")
    direct = job_info['argument']['directory']
    # Step 3: 上传数据到FTP
    my_logger.info(f"文件开始上传至FTP")
    put_file(itemVariablesJson.path, direct)

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
                delete_file(itemVariablesJson.path, direct)
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


def create_task(ds, name, itemKey):
    """
           创建任务,允许用户自定义更改任务名称
        """
    if len(str(name)) == 0:
        body = '''{ "operationName": "createEventImportJob", "variables": { "fileType":"ftp", "timeRange":"", 
            "tunnelId": "%s", "itemModel":{ "key": "%s" }, "createType":"PYTHON" }, "query": "mutation 
            createEventImportJob($tunnelId: HashId!, $timeRange: String, $fileType: String, $itemModel: ItemModelIdInput, 
            $createType: String) { createEventImportJob(tunnelId: $tunnelId, timeRange: $timeRange,fileType: $fileType, 
            itemModel:$itemModel, createType: $createType) { id name argument { directory __typename } __typename } }" 
            }''' % (ds, itemKey)
    else:
        body = '''{ "operationName":"createEventImportJob", "variables":{ "fileType":"ftp", "tunnelId":"%s", 
            "timeRange":"", "name":"%s", "itemModel":{ "key": "%s" }, "createType":"PYTHON" }, "query":"mutation 
            createEventImportJob($name: String, $tunnelId: HashId!, $timeRange: String, $fileType: String, $itemModel: 
            ItemModelIdInput, $createType: String) { createEventImportJob(name: $name, tunnelId: $tunnelId, timeRange: 
            $timeRange, fileType: $fileType, itemModel:$itemModel, createType: $createType) { id name argument { 
            directory __typename } __typename } }" }''' % (ds, name, itemKey)
    resp = http_util.send_graphql_post(http_util.get_token(), body.encode('utf-8'))
    try:
        return resp['createEventImportJob']
    except TypeError:
        logger.error("自定义任务名称已存在！")


def json_variables_debug_process(paths, itemKey):
    """
    主体导入Debug
    1、校验有无itemKey
    2、校验主体(条件:是否是平台内置和是否定义)
    """
    count = 0
    error_count = 0
    correct_count = 0  # 正确行数
    flag, var_id, var_name, var_desc = check_item_var_exsit(ApiConfig.token, itemKey)
    if flag:
        key_list = check_item_var_key_data_exsit(ApiConfig.token, var_id)
    else:
        logger.error(f"item_Key主体标识符[{itemKey}]不存在，校验终止")
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
                            # 主体
                            if 'attrs' in data_dictionary:
                                if not isinstance(data_dictionary['attrs'], dict):
                                    normal = False
                                    error_message += f"attrs数据格式不对\n"
                                for key in data_dictionary['attrs']:
                                    if key not in key_list:
                                        normal = False
                                        error_message += f"主体字段[{key}]不存在\n"
                                    elif data_dictionary['attrs'][key] is None or data_dictionary['attrs'][key] == "":
                                        print(f"主体[{data_dictionary['item_id']}]中字段[{key}]的值为空或为NULL,请检查原始数据\n")
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
        my_logger.info(f"本次共校验[{count}]行数据")
    else:
        my_logger.info(f"本次共校验[{count}]行数据,其中校验失败[{error_count}]行数据,异常数据已剪切到临时文件目录[{current_tmp_path}]")

    if correct_count == 0:
        my_logger.info(f"由于本次正确数据0条，故不生成导数任务。")
        return False
    else:
        return True
