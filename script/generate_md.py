#!/usr/bin/python
# -*- coding: UTF-8 -*-
import operator
import os
import zhconv

from script.core import Entry

title = "潮州話怎呢呾"
table_header = """| 普通話 | 潮州話 | 潮州白話字 | 來源       | 示例         |
| ------ | ------ | ---------- | ---------- | ------------ |"""

doc_path = "../doc"
files = os.listdir(doc_path)
files.sort()

hant_2_hans = {
    "簥": "茄",
    "畨": "番",
    "挿": "插",
    "骹": "脚",
    "𥐥": "矾",
}


def generate_md(locale='zh-hant'):
    line_list = []
    for filename in files:
        if not filename.endswith(".txt"):
            continue
        file_path = os.path.join(doc_path, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            print(f"handling: {filename}")
            splits = filename.split('_')
            index = splits[0]
            name = splits[1].rstrip('.txt').replace('-', '·')
            if index.endswith('0'):
                line_list.append(f"\n## {name}\n")
            else:
                line_list.append(f"\n### {name}\n")
            entry_list = []
            for line in file:
                entry = Entry(line)
                if entry is None:
                    continue
                entry_list.append(entry)
            if len(entry_list) > 0:
                line_list.append(table_header)
            entry_list.sort(key=operator.attrgetter("level"))
            for entry in entry_list:
                line_list.append(f"{entry.to_table_item()}")

    locale_title = zhconv.convert(title, locale=locale)
    dest = f"../{locale_title}.md"
    with open(dest, 'w', encoding='utf-8') as f:
        f.write(f"# {locale_title}\n")
        for line in line_list:
            if locale == 'zh-hant':
                f.write(line + "\n")
            else:
                for item in hant_2_hans:
                    line = line.replace(item, hant_2_hans[item])
                f.write(zhconv.convert(line, locale=locale) + "\n")


if __name__ == "__main__":
    generate_md(locale='zh-hant')
    generate_md(locale='zh-hans')
