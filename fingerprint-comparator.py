#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import json
import tempfile

def printText():
    for fingerprintV in fingerprintDic:
        if len(fingerprintDic[fingerprintV])>=2:
            print "+%s" % (fingerprintV)
            for lineNumber in fingerprintDic[fingerprintV]:
                print "--%s" % (originalValues[lineNumber].replace('\n', ''))

def printJson():
    t = {}
    for hashV in fingerprintDic:
        if len(fingerprintDic[hashV])>=2:
            t[hashV] = []
            for lineNumber in fingerprintDic[hashV]:
                t[hashV].append(originalValues[lineNumber].replace('\n', ''))
    t = json.dumps(t, indent=4, ensure_ascii=False)
    print t


parser = argparse.ArgumentParser(description='create fingerprint for strings and compare them')

parser.add_argument('--input', metavar='inputFile', required=True,
                    help='input file which contains strings, each line for one string')
parser.add_argument('--remove-words', metavar='word1 word2 ...', nargs='+', default=[],
                    help='remove these words and then create fingerprints')
parser.add_argument("--output-type", choices=["text", "json"], default="text",
                    help="")

opts = parser.parse_args(sys.argv[1:])

inputFile = opts.input
stopWords = [x.lower() for x in opts.remove_words]
outputType = opts.output_type

tempFile=tempfile.mktemp()
cmd="cat %s | tr '[:upper:]' '[:lower:]' " % (inputFile)
for w in stopWords:
    cmd=cmd+" | sed 's/%s//g'" % (w)
cmd=cmd+" > %s" % (tempFile)
os.system(cmd)

cmd="""
LC_COLLATE=C sed 's/\.//g' %s| LC_COLLATE=C sed 's/[^ -~]/./g' | sed 's/ //g' |tr '[:upper:]' '[:lower:]'
""" % (tempFile)
hashValues = os.popen(cmd).read().split('\n')

fingerprintDic={}
for i in range(len(hashValues)-1):
    hashV = hashValues[i].strip()
    for w in stopWords:
        hashV = hashV.replace(w, "")

    if hashV in fingerprintDic:
        fingerprintDic[hashV].append(i)
    else:
        fingerprintDic[hashV]=[i]

originalValues = open(inputFile).readlines()

if outputType=="text":
    printText()
elif outputType=="json":
    printJson()

