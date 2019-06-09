# -*-  coding:utf-8 -*-
import yaml
import inspect


def data_analyze(key):
    # 动态获取filename
    file_name = inspect.stack()[1].filename
    start_file_name = file_name.rfind("_")
    end_file_name = file_name.rfind(".")
    file_name = file_name[start_file_name +1:end_file_name] + "_data"
    # 从文件中获取参数
    with open("./data/"+ file_name +".yml", "r") as f:
        analyze_data = yaml.load(f)[key]
        data_list = list()
        for i in analyze_data.values():
            data_list.append(i)
        return data_list