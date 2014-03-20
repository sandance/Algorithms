import sys
import os

subs = set()

for line in sys.stdin:
    line = line.strip().split(',')
    if line[0] == "sub1":
        continue
    if len(line) <5:
        continue
    subscriber_id = line[5]
    subs.add(subscriber_id)
print len(subs)
