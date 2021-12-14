import re
from collections import defaultdict

inputf = "input.txt"
with open(inputf) as f:
    template = f.readline().strip()
    f.readline()
    rules = [re.findall(r'([A-Za-z]+) -> ([A-Za-z]+)', s)[0] for s in f.readlines()]
patterns = defaultdict(lambda: 0)
count = defaultdict(lambda: 0)
count[template[0]] += 1
for pair in zip(template, template[1:]):
    patterns[pair] += 1
    count[pair[1]] += 1
for i in range(40):
    nextpatterns = defaultdict(lambda: 0)
    for rule in rules:
        a = rule[0][0]
        b = rule[0][1]
        c = rule[1]
        nextpatterns[(a, c)] += patterns[(a, b)]
        nextpatterns[(c, b)] += patterns[(a, b)]
        count[c] += patterns[(a, b)]
    patterns = nextpatterns
values = count.values()
print(max(values) - min(values))