import json
import sys

digital = {}
character = {}
d = {}
c = {}
s = list(map(str, sys.stdin))
for elem in s:
    st = elem.split()
    if st[1].isdigit():
        d[st[0]] = st[1]
    else:
        c[st[0]] = st[1]
digital = d
character = c
sl = {}
sl['digital'] = digital
sl['character'] = character
print(sl)
with open('madness.json', 'w') as f:
    json.dump(sl, f)
