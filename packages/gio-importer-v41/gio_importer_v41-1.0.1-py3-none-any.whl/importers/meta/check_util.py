import logging

from importers.meta.data_center import *
import re


def check_key(str):
    """
     校验标识符KEY，不能为空，长度小于50，只可以由字母数字下划线组成，且只能字母开头
    :param str: 字符串
    :return:
    """
    if (str == ''):
        logging.error("事件名不能为空")
        exit(-1)
    elif (len(str) > 100):
        logging.error("事件名<{}>长度超限".format(str))
        exit(-1)
    elif (str[0].isdigit() or is_chinese(str) or match(str)):
        logging.error("事件名<{}>不合法，只可以由字母数字下划线组成，且只能字母开头~".format(str))
        exit(-1)


def check_name(name, key):
    """
     校验name，长度小于50，当name为空，则默认与标识符一致
    :param name: 名称
    :param key: 标识符
    :return:
    """
    if name != "" and len(name) > 30:
        logging.error("显示名<{}>长度超限~".format(name))
        exit(-1)
    elif name == "":
        return key
    # elif isexsit_eventvar(name) or isexsit_usertvar(name):
    #     logging.error("名称<{}>已重复~".format(name))
    #     exit(-1)
    else:
        return name


def isexsit_eventvar(name):
    """
     校验事件属性名称是否存在
     :param name: 名称
     :return: True/False
     """
    event_variables = getdataCenterEventVariables()
    for var in event_variables:
        if var['name'] == name:
            return True
    return False


def isexsit_usertvar(name):
    """
     校验用户属性名称是否存在
     :param name: 名称
     :return: True/False
     """
    user_variables = getdataCenterUserVariables()
    for var in user_variables:
        if var['name'] == name:
            return True
    return False


def check_event_valuetype(tp):
    """
     校验事件数据类型
     :param tp: 数据类型
     :return:
     """
    if tp == '':
        logging.error("数据类型<{}>未设置".format(tp))
        exit(-1)
    elif tp not in ('string', 'int', 'double'):
        logging.error("数据类型<{}>不在可选值范围".format(tp))
        exit(-1)


def check_user_valuetype(tp):
    """
     校验用户数据类型
     :param tp: 数据类型
     :return:
     """
    if tp == '':
        logging.error("数据类型<{}>未设置".format(tp))
        exit(-1)
    elif tp not in ('string', 'int', 'date', 'double'):
        logging.error("数据类型<{}>不在可选值范围".format(tp))
        exit(-1)


def check_event_exsit(token, key):
    """
     校验事件标识符KEY是否存在
     :param token: 登录令牌
     :param key: 标识符
     :return:
     """
    custom_events = getdataCenterCustomEvents(token)
    for var in custom_events:
        if var['key'] == key:
            return True, var
    else:
        return False, ''


def check_event_attr_exsit(token, key):
    """
     校验事件标识符KEY是否存在
     :param token: 登录令牌
     :param key: 标识符
     :return:
     """
    custom_events = getdataCenterCustomEventsAndAttr(token)
    id_list = []
    for var in custom_events:
        if var['key'] == key:
            if len(var['attributes']) != 0:
                for a in var['attributes']:
                    id_list.append(a['id'])
                return True, var, id_list
            else:
                return True, var, id_list
    else:
        return False, '', []


def check_event_var_exsit(token, key):
    """
     校验事件属性标识符KEY是否存在
     :param token: 登录令牌
     :param key: 标识符
     :return:
     """
    event_variables = getdataCenterEventVariables(token)
    for var in event_variables:
        if var['key'] == key:
            return True, var
    else:
        return False, ''


def check_user_var_exsit(token, key):
    """
     校验用户属性标识符KEY是否存在
     :param token: 登录令牌
     :param key: 标识符
     :return:
     """
    user_variables = getdataCenterUserVariables(token)
    for var in user_variables:
        if var['key'] == key:
            return True, var
    else:
        return False, ''


def check_bind_event_exsit(token, key):
    """
     校验事件与事件属性
     :param token: 登录令牌
     :param key: 标识符
     :return:
     """
    custom_events = getdataCenterCustomEvents(token)
    for var in custom_events:
        if var['key'] == key:
            return True, var['id'], var['description']
    else:
        return False, '', ''


def check_key_name(var_list, key, name):
    """
     校验标识符、名称
     :param var_list: 变量列表
     :param key: 标识符
     :param name: 名称
     :return:
     """
    for var in var_list:
        if var['key'] == key:
            logging.error("标识符<{}>已存在~".format(key))
            exit(-1)
        elif var['name'] == name:
            logging.error("名称<{}>已存在~".format(name))
            exit(-1)


def is_chinese(string):
    """
     检测字符串是否存在汉字
     :param string: 字符串
     :return:True/False
     """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def match(str):
    """
     只可以由字母数字下划线组成，且只能字母开头
     :param str: 字符串
     :return:True/False
     """
    mh = re.match(r'[0-9a-zA-Z_]*', str)
    if len(mh.group()) != len(str):
        return True
    else:
        return False


def check_attr(token, attr):
    """
     校验事件与事件属性
     :param token: 登录令牌
     :param attr: 事件属性
     :return:id_list,key_list
     """
    attrs = str(attr).split(",")
    key_list = []
    id_list = []
    error_list = []
    event_variables = getdataCenterEventVariables(token)
    for a in attrs:
        for event in event_variables:
            if event['key'] == a:
                id_list.append(event['id'])
                key_list.append(event['key'])
                break
        else:
            error_list.append(a)
    if len(error_list) == len(attrs):
        logging.error("绑定事件属性失败，事件属性:{}不存在,请先创建事件属性~".format(error_list))
        exit(-1)
    elif len(error_list) != 0:
        logging.error("事件属性:{}不存在,请先创建事件属性~".format(error_list))
    return id_list, key_list
