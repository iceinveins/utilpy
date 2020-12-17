#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import commands
from argparse import ArgumentParser


def doExcerpt(inputPath, outputPath, beginning, end):
    global root_path
    cmd = root_path + '/excerpt.py ' + inputPath + ' "' + beginning + '" "' + end + '" '
    cmd += '--out="' + outputPath +'"'
    os.system(cmd)

def doStatistic(inputPath):
    global root_path
    cmd = root_path + '/statistic.py --filePath=' + inputPath
    os.system(cmd)

def main():
    global root_path
    root_path              = sys.path[0]
    excerpt_procedure_path = root_path + '/istatsHelper_excerpt_procedure.txt'

    parser = ArgumentParser()
    parser.add_argument('logpath',      type = str,         help = 'file path of the istats')
    args       = parser.parse_args()
    logpath    = args.logpath

    #excerpt istats by Procedure
    print  "which procedure do you need ? (case sensitive)"
    procedure = raw_input()
    doExcerpt(logpath, excerpt_procedure_path, 'Procedure: ' + procedure, 'Procedure:')
    doStatistic(excerpt_procedure_path)

main()
