import json
import os
import time

from pymysql import OperationalError, MySQLError
from importers.common.common_util import mysql_connect, get_all_file, remove_file, getVariables
from importers.common.config_util import get_temp_dir_from_config
from importers.common.log_util import logger
from importers.data_import.data_events import events_import_json
from importers.data_import.data_model import EventsJson, DataEvent, DataUser, UserVariablesJson
from importers.data_import.data_user_variable import user_variables_import_json
from importers.meta.data_center import getBindEvent, getdataCenterUserVariables


def event_mysql_import(args, start, end):
    """
       行为数据导入 ，MYSQL数据源
    """
    try:
        conn = mysql_connect(user=args.get('user'), password=args.get('password'), host=args.get('host'),
                             port=int(args.get('port')))
    except MySQLError and OperationalError:
        logger.error(" MYSQL连接失败。")
        exit(-1)
    cursor = conn.cursor()
    try:
        sql = args.get('sql')
        cursor.execute(sql)
        logger.info(sql)
    except SyntaxError or MySQLError or OperationalError:
        logger.error("请检查SQL语句")
        exit(-1)
    desc = cursor.description
    desc_list = []
    for d in desc:
        desc_list.append(d[0])
    if 'userId' not in desc_list or 'event' not in desc_list or 'timestamp' not in desc_list:
        logger.error("userId或event或timestamp字段不存在")
        exit(-1)
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_path = os.path.join(temp_dir, str(int(round(time.time() * 1000))))
    if os.path.exists(current_tmp_path) is False:
        os.makedirs(current_tmp_path)
    logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")
    json_file_abs_path = current_tmp_path + '/' + 'tmp_events.json'
    event = getBindEvent()
    res = {}
    for i in event['dataCenterCustomEvents']:
        list = []
        for a in i['attributes']:
            list.append(a['key'])
        res[i['key']] = list
    try:
        start_time = time.time()
        wf = open(json_file_abs_path, 'w')
        cnt = 0
        count = 0
        while True:
            batch = cursor.fetchmany(size=args.get('batch'))
            cnt += 1
            if len(batch) == 0 and cnt == 1:
                logger.error("数据为空")
                exit(-1)
            elif len(batch) == 0 and cnt > 1:
                logger.info(f"临时文件总共写入{count}条数据")
                end_time = time.time()
                cost_time = end_time - start_time
                logger.info("读取SQL数据,写入临时文件耗时:%.3f秒" % cost_time)
                if len(str(args.get('jobName'))) == 0 or args.get('jobName') is None:
                    job_name = f"Python_events_{time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))}"
                else:
                    job_name = args.get('jobName')
                events_import_json(
                    EventsJson(name='events',
                               path=get_all_file(current_tmp_path),
                               format='JSON',
                               debug=False,
                               eventStart=start,
                               eventEnd=end,
                               datasourceId=args.get('datasource_id'),
                               jobName=job_name,
                               clear=False)
                )
                break
            else:
                for row in batch:
                    tmp = {}
                    var = {}
                    for a in range(len(row)):
                        if desc_list[a] == 'userId' or desc_list[a] == 'event' or desc_list[a] == 'timestamp':
                            tmp[desc_list[a]] = row[a]
                        elif desc_list[a] == 'eventId' and row[a] != '':
                            tmp['eventId'] = row[a]
                        elif desc_list[a] == 'userKey' and row[a] != '':
                            tmp['userKey'] = row[a]
                        else:
                            var[desc_list[a]] = row[a]
                    tmp['attrs'] = var
                    if tmp['event'] in res:
                        for key in tmp['attrs']:
                            if key not in res[tmp['event']]:
                                logger.error(f"自定义事件属性[{key}]在GIO平台未定义或未绑定事件属性")
                                exit(-1)
                    else:
                        logger.error(f"事件[{tmp['event']}]在GIO平台未定义或者未绑定属性")
                        exit(-1)
                    if 'eventId' in tmp:
                        eventId = tmp['eventId']
                    else:
                        eventId = None
                    if 'userKey' in tmp:
                        userKey = tmp['userKey']
                    else:
                        userKey = ''
                    data_event = DataEvent(userId=tmp['userId'], event=tmp['event'], timestamp=tmp['timestamp'],
                                           attrs=tmp['attrs'], userKey=userKey, eventId=eventId)
                    wf.write(json.dumps(data_event.__dict__, ensure_ascii=False))
                    wf.write('\n')
                    count += 1
                    if count % 2000000 == 0:
                        logger.info(f"已经写入{count}条数据进临时文件......")
                wf.flush()
    finally:
        remove_file(current_tmp_path)


def user_mysql_import(args):
    """
       用户属性导入，MYSQL数据源
    """
    try:
        conn = mysql_connect(user=args.get('user'), password=args.get('password'), host=args.get('host'),
                             port=int(args.get('port')))
    except MySQLError and OperationalError:
        logger.error("MYSQL连接失败。")
        exit(-1)
    cursor = conn.cursor()
    try:
        sql = args.get('sql')
        cursor.execute(sql)
        logger.info(sql)
    except SyntaxError or MySQLError or OperationalError:
        logger.error("请检查SQL语句")
        exit(-1)
    desc = cursor.description
    desc_list = []
    for d in desc:
        desc_list.append(d[0])
    if 'userId' not in desc_list:
        logger.error("userId字段不存在")
        exit(-1)
    temp_dir = get_temp_dir_from_config()  # 从配置中获取临时存储目录
    current_tmp_path = os.path.join(temp_dir, str(int(round(time.time() * 1000))))
    if os.path.exists(current_tmp_path) is False:
        os.makedirs(current_tmp_path)
    logger.info(f"临时存储Json文件目录：[{current_tmp_path}]")
    keys = getVariables(getdataCenterUserVariables())
    json_file_abs_path = current_tmp_path + '/' + 'tmp_user.json'
    try:
        start_time = time.time()
        wf = open(json_file_abs_path, 'w')
        cnt = 0
        count = 0
        while True:
            batch = cursor.fetchmany(size=args.get('batch'))
            cnt += 1
            if len(batch) == 0 and cnt == 1:
                logger.error("数据为空")
                exit(-1)
            elif len(batch) == 0 and cnt > 1:
                logger.info(f"临时文件总共写入{count}条数据")
                end_time = time.time()
                cost_time = end_time - start_time
                logger.info("读取SQL数据,写入临时文件耗时:%.3f秒" % cost_time)
                if len(str(args.get('jobName'))) == 0 or args.get('jobName') is None:
                    job_name = f"Python_user_{time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))}"
                else:
                    job_name = args.get('jobName')
                user_variables_import_json(
                    UserVariablesJson(name='user_variables',
                                      path=get_all_file(current_tmp_path),
                                      debug=False,
                                      format='JSON',
                                      datasourceId=args.get('datasource_id'),
                                      jobName=job_name,
                                      clear=False)
                )
                break
            else:
                json_list = []
                for row in batch:
                    res = {}
                    var = {}
                    for a in range(len(row)):
                        if desc_list[a] == 'userId':
                            res[desc_list[a]] = row[a]
                        elif desc_list[a] == 'userKey' and row[a] != '':
                            res['userKey'] = row[a]
                        else:
                            var[desc_list[a]] = row[a]
                    res['attrs'] = var
                    json_list.append(res)

                for json_str in json_list:
                    for key in json_str['attrs']:
                        if key not in keys and key.startswith("$") is False:
                            logger.error("用户属性{}在GIO平台未定义".format(key))
                            exit(-1)
                    if 'userKey' in json_str:
                        userKey = json_str['userKey']
                    else:
                        userKey = ''
                    data_event = DataUser(userId=json_str['userId'], userKey=userKey, attrs=json_str['attrs'])
                    wf.write(json.dumps(data_event.__dict__, ensure_ascii=False))
                    wf.write('\n')
                    count += 1
                    if count % 2000000 == 0:
                        logger.info(f"已经写入{count}条数据进临时文件......")
                wf.flush()
    finally:
        remove_file(current_tmp_path)
