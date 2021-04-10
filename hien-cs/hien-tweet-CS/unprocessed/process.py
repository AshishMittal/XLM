import sys

s1 = []
s2 = []
for line in sys.stdin:
    split_line = line.strip().split('\t')
    if len(split_line) < 3:
        print(' '.join(s1))
        print(' '.join(s2))
        s1.clear()
        s2.clear()
    else:
        rom, type, orig = split_line
        s1.append(rom)
        s2.append(orig)