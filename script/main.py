#!/usr/bin/python
# -*- coding: UTF-8 -*-
from parse import search
import os

# 定義解析規則
# {普通話}, {潮州話漢字}, {潮州話白話字}, {分級}, {引用簡寫}, {示例}
pattern = "{mandarin}, {han}, {puj}, {level}, {ref}, {example}\n"


def parse_line(line):
    splits = line.split(",")
    result = {}
    if len(splits) < 3:
        return None
    result['mandarin'] = str(splits[0]).strip()
    result['han'] = str(splits[1]).strip()
    result['puj'] = str(splits[2]).strip().capitalize()
    result['level'] = "L0"
    result['example'] = "汕頭話讀本"
    if len(splits) >= 4:
        result['level'] = str(splits[3]).strip()
    if len(splits) >= 5:
        result['example'] = str(splits[4]).strip()
    return result


# 遍历每个文件，读取每行文本并解析
folder_path = "../doc"
folder_path_new = "../doc2"
for filename in os.listdir(folder_path):
    if not filename.endswith(".txt"):
        continue
    file_path = os.path.join(folder_path, filename)
    file_path_new = os.path.join(os.getcwd(), filename)
    word_list = []
    with open(file_path, "r", encoding="utf-8") as file:
        print(f"handle: {filename}")
        for line in file:
            parsed_data = parse_line(line)
            # 在这里你可以根据需要处理解析后的数据
            # print(parsed_data)
            if parsed_data is None:
                continue
            if parsed_data['example'] is None:
                word_list.append(f"{parsed_data['mandarin']}, "
                                 f"{parsed_data['han']}, "
                                 f"{parsed_data['puj']}, "
                                 f"{parsed_data['level']}")
            else:
                word_list.append(f"{parsed_data['mandarin']}, "
                                 f"{parsed_data['han']}, "
                                 f"{parsed_data['puj']}, "
                                 f"{parsed_data['level']}, "
                                 f"{parsed_data['example']}")
    with open(file_path_new, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(word_list))
