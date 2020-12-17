#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import commands
from argparse import ArgumentParser

def main():
    global eid
    eid = commands.getoutput('whoami')

    scope = ['all', 'py', 'ttcn']
    action = {'all' : start_all, 'py': start_py, 'ttcn': start_ttcn}

    parser = ArgumentParser()
    parser.add_argument('buildid',      type = str,         help = 'build binary')
    parser.add_argument('--testid',     type = str,         help = 'test binary, default = buildid',      default = '',           dest = 'testid')
    parser.add_argument('--scope',      type = str,         help = 'test scope,  default = all',          default = 'all',        dest = 'scope',    choices = scope)

    args     = parser.parse_args()
    buildid  = args.buildid
    testid   = args.testid
    scope    = args.scope

    if testid == '':
        testid = buildid

    action[scope](buildid, testid)


def start_all(buildid, testid):
    start_py(buildid, testid)
    start_ttcn(buildid, testid)

def start_py(buildid, testid):
    global eid
    cmds=[
'''
queue_run.py --ett-specification standard --replace 1 --node-type EVRTD --suites-order LongestSuiteFirst \
--build-id %BUILDID% --test-type TTCN --days-to-wait 6 --label TTCN-SMF_BASIC-EVRTD_standard \
--priority normal+ --split-count 1 --username %EID% --test-scope SMF_BASIC --test-binary-id %TESTID% --official --max-rerun-ratio 0.1
'''
,
'''
queue_run.py --ett-specification standard --replace 1 --node-type EVRTD --suites-order LongestSuiteFirst \
--build_id %BUILDID% --test-type TTCN --days-to-wait 6 --label TTCN-SMF_EXTENDED-EVRTD_standard \
--priority normal+ --split-count 3 --username %EID%  --test-scope SMF_EXTENDED --test-binary-id %TESTID% --official --max-rerun-ratio 0.1 
'''
    ]
    for cmd in cmds:
        cmd = cmd.replace('%BUILDID%', buildid).replace('%TESTID%', testid).replace('%EID%', eid)
        os.system(cmd)

def start_ttcn(buildid, testid):
    cmds=[
'''
queue_run.py --ett-specification cups_small --replace 1 --node-type EVRTD --suites-order LongestSuiteFirst \
--build-id %BUILDID% --test-type TTCN --days-to-wait 6 --label TTCN-SMF_CUPS_INT-EVRTD_cups_small \
--priority high+ --custom-arguments '--filter-tags \!PYTHON&&SMF_CUPS_INT' --split-count 1 --username %EID% --test-scope SMF_CUPS_INT \
--test-binary-id %TESTID% --official --max-rerun-ratio 0.1
'''
,
'''
queue_run.py --ett-specification standard --node-type EVRTD --suites-order LongestSuiteFirst \
--build-id %BUILDID% --test-type TTCN --days-to-wait 6 --label TTCN-SMF_SA-EVRTD_standard \
--priority high+ --split-count 1 --username %EID% --test-scope SMF_SA --test-binary-id %TESTID% --official --max-rerun-ratio 0.1
'''
,
'''
queue_run.py --ett-specification pccsm_ft --replace 1 --node-type CEPG --suites-order LongestSuiteFirst \
--build-id %BUILDID% --test-type TTCN --days-to-wait 6 --label TTCN-SMF_SA-CEPG_pccsm_ft --priority high \
--custom-arguments ' --filter-tags SMF_SA&&\!NOT_READY_PCC --extra-timeout 240' --split-count 1 --username %EID% --test-scope SMF_SA \
--test-binary-id %TESTID% --official --max-rerun-ratio 0.1
'''
    ]
    for cmd in cmds:
        cmd = cmd.replace('%BUILDID%', buildid).replace('%TESTID%', testid).replace('%EID%', eid)
        os.system(cmd)

main()