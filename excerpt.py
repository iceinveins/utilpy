#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from argparse import ArgumentParser


def core(lines, output, s, e):
        pos = 0
        while 1:
                begin = lines.find(s, pos)
                if begin == -1:
                        break
                end = lines.find(e, begin + len(s))
                output.write(lines[begin:end])
                pos = end

def main():
	parser = ArgumentParser()
	parser.add_argument('filepath',        type = str,         help = 'filepath')
	parser.add_argument('start',           type = str,         help = 'beginning of the paragraph')
	parser.add_argument('end',             type = str,         help = 'end of the paragraph')
	parser.add_argument('--out',           type = str,         help = 'outputDir',        				default = './excerpt.txt',   	dest = 'outputDir')

	args     	= parser.parse_args()
	filepath 	= args.filepath
	start 		= args.start
	end        	= args.end
	outputDir 	= args.outputDir

	f = open(filepath,'r')
        lines = f.read()
	output = open(outputDir, 'wa')
	output.seek(0)
	output.truncate()

	core(lines, output, start, end)
	f.close()

main()
