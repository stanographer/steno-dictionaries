from __future__ import print_function

import json
import sys
import re

try:
    with open(sys.argv[1]) as f:
        d = json.load(f, data)
except:
    with open(sys.argv[1]) as f:
        d = json.load(f, encoding='latin-1')

out = open(sys.argv[2], 'w')

header = """{\\rtf1\\ansi{\\*\\cxrev100}\\cxdict{\\*\\cxsystem Plover}{\\stylesheet{\\s0 Normal;}}"""
print(header, file=out)

for s, t in d.items():
    t = re.sub(r'{\.}', '{\\cxp. }', t)
    t = re.sub(r'{!}', '{\\cxp! }', t)
    t = re.sub(r'{\?}', '{\\cxp? }', t)
    t = re.sub(r'{\,}', '{\\cxp, }', t)
    t = re.sub(r'{:}', '{\\cxp: }', t)
    t = re.sub(r'{;}', '{\\cxp; }', t)
    t = re.sub(r'{\^}', '\\cxds ', t)
    t = re.sub(r'{\^([^^}]*)}', '\\cxds \\1', t)
    t = re.sub(r'{([^^}]*)\^}', '\\1\\cxds ', t)
    t = re.sub(r'{\^([^^}]*)\^}', '\\cxds \\1\\cxds ', t)
    t = re.sub(r'{-\|}', '\\cxfc ', t)
    t = re.sub(r'{ }', ' ', t)
    t = re.sub(r'{&([^}]+)}', '{\\cxfing \\1}', t)
    t = re.sub(r'{#([^}]+)}', '\\{#\\1\\}', t)
    t = re.sub(r'{PLOVER:([a-zA-Z]+)}', '\\{PLOVER:\\1\\}', t)
    t = re.sub(r'\\"', '"', t)

    entry = "{\\*\\cxs %s}%s\n" % (s, t)

    out.write(entry.encode('utf-8'))
    
print("}", file=out)
