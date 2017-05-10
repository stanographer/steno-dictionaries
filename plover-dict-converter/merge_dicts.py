from __future__ import print_function
import json
import sys

merged = {}

for file_name in sys.argv[1:]:
    f = open(file_name)
    s = f.read()
    d = json.loads(s)
    for k, v in d.items():
        if k in merged and merged[k] != v:
            print(k, 'is being overridden by', file_name, 'from', merged[k], 'to', v, file=sys.stderr)
        merged[k] = v

print(json.dumps(merged, sort_keys=True, indent=0, separators=(',', ': ')))
