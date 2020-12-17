#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
import re
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('--filePath',           type = str,         help = 'file path',           default = './excerpt.txt',              dest = 'filePath')
    args     	= parser.parse_args()
    filePath 	= args.filePath

    counter = 0
    result = commands.getoutput('less ' + filePath + ' | grep -e ".*[:=] [0-9]\+"')
    elems = commands.getoutput('less ' + filePath + ' | grep -e ".*[:=]" -o | sort | uniq')
    dict ={}

    for line in result.splitlines():
        for elem in elems.splitlines():
            if line.find(elem) != -1:
                num = re.search(r"\d+", line)
                if int(num.group()) != 0:
                    if not dict.has_key(elem):
                        dict[elem] = 0
                    dict[elem] += int(num.group())
    for key,value in dict.items():
        print(key, value)

main()
