#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
from argparse import ArgumentParser


def doExcerpt(inputPath, outputPath, beginning, end):
    cmd = '/home/ezaiuhx/utilpy/excerpt.py ' + inputPath + ' "' + beginning + '" "' + end + '" '
    cmd += '--out="' + outputPath +'"'
    os.system(cmd)

def doStatistic(inputPath):
    cmd = '/home/ezaiuhx/utilpy/statistic.py --filePath=' + inputPath
    os.system(cmd)

def main():
    excerpt_procedure_path   = '/home/ezaiuhx/utilpy/istatsHelper_excerpt_procedure.txt'
    excerpt_cause_path       = '/home/ezaiuhx/utilpy/istatsHelper_excerpt_cause.txt'

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
