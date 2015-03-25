import sys
import os

subs = set()

for line in sys.stdin:
    line = line.strip().split(',')
    if len(line) < 11:
        continue
    if line[0] == "sub1":
        continue
    subscriber_id = line[0]
    subs.add(subscriber_id)
print len(subs)
