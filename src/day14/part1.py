import re
from collections import defaultdict

inputf = "input.txt"
with open(inputf) as f:
    template = f.readline().strip()
    f.readline()
    rules = [re.findall(r'([A-Za-z]+) -> ([A-Za-z]+)', s)[0] for s in f.readlines()]
for i in range(10):
    next = ""
    next += template[0]
    for a,b in zip(template, template[1:]):
        for rule in rules:
            if a == rule[0][0] and b == rule[0][1]:
                next += rule[1]
                break
        next += b
    template = next
count = defaultdict(lambda: 0)
for c in template:
    count[c] += 1
values = count.values()
print(max(values) - min(values))