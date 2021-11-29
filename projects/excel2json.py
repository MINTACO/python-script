#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from openpyxl import load_workbook
from utils.os_utils import get_all_file_path
import os
import json


def read_xlsx(entry, output, is_format=True):
    # 加载文件
    book = load_workbook(entry)
    # 获取sheet列表
    sheets = book.sheetnames
    # 返回dict
    result = {}
    # 循环去除sheet数据
    for sheet_name in sheets:
        # sheet name获取sheet：
        sheet = book[sheet_name]
        # 获取总行数
        rows = sheet.max_row
        # 获取总列数
        cols = sheet.max_column
        # 获取表头
        head = [row for row in sheet.iter_rows(min_row=1, max_row=1, values_only=True)][0]
        # 数据组装
        sheet_data = []
        for row in sheet.iter_rows(min_row=2, max_row=rows + 1, values_only=True):
            data = dict(zip(head, row))
            sheet_data.append(data)
        result[sheet_name] = sheet_data
    # return result
    (filename) = is_legal(entry)
    output_dir = os.path.join(output, filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for key in result:
        output = os.path.join(output_dir, key + '.json')
        with open(output, 'w', encoding='UTF-8') as fileobject:
            if is_format:
                fileobject.write(json.dumps(result[key], indent=4, ensure_ascii=False))
            else:
                fileobject.write(json.dumps(result[key], ensure_ascii=False))
    print('All Done!')


def is_legal(file):
    (filename, ext) = os.path.splitext(file)
    if ext == '':
        print(1)
        return False
    if ext != '.xlsx' and ext != '.xls':
        return False
    return filename, ext


def excel2json(entry, output='./output', is_format=True):
    if os.path.isfile(entry):
        # 输入文件
        if not is_legal(entry):
            raise ValueError('请输入合法excel文件')
        (filename, ext) = is_legal(entry)
        if ext == '.xlsx':
            read_xlsx(entry, output, is_format)

    # files = get_all_file_path(entry)
    # for key in files:
    #     # print(key)
    #     name_ext_list = key.split('.')
    #     # 无后缀名跳过
    #     if len(name_ext_list) <= 1:
    #         continue
    #     # 跳过非excel文件
    #     ext = name_ext_list[len(name_ext_list) - 1]
    #     if ext != 'xlsx' and ext != 'xls':
    #         continue
    #     # 忽略临时文件
    #     if key[0] == '~' or key[0] == '!':
    #         continue
    #     print(key)
