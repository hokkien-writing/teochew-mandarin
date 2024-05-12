#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Entry:

    def __init__(self, line):
        splits = line.split(",")
        if len(splits) < 3:
            return
        self.mandarin = str(splits[0]).strip()
        self.han = str(splits[1]).strip()
        self.puj = str(splits[2]).strip().capitalize()
        self.level = "L0"
        self.ref = ""
        self.example = ""
        if len(splits) >= 4:
            self.level = str(splits[3]).strip()
        if len(splits) >= 5:
            self.ref = str(splits[4]).strip()
        if len(splits) >= 6:
            self.example = str(splits[5]).strip()

    def __str__(self):
        if len(self.example) == 0:
            return f"{self.mandarin}, {self.han}, {self.puj}, {self.level}, {self.ref}"
        return f"{self.mandarin}, {self.han}, {self.puj}, {self.level}, {self.ref}, {self.example}"

    def to_table_item(self):
        mandarin = self.mandarin.replace('|', ',')
        han = self.han.replace('|', ',')
        puj = self.puj.replace('|', ',')
        ref = self.ref.replace('|', ',')
        example = self.example.replace('|', ',')
        return f"| {mandarin} | {han} | {puj} | {ref} | {example} |"
