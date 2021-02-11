import sys
import json

data = list(map(str.strip, sys.stdin))
slov = dict()
damp = dict()
itog = dict()
for i in data:
    a, b = i.split(': ')
    if b == '-1' or b == 'done':
        slov[a] = b
    else:
        damp[a] = b
itog = {
    'correctly' : slov,
    'incorrectly' : damp
}
with open('ready.json', 'w') as file:
    json.dump(itog, file, ensure_ascii=False, indent=4)
