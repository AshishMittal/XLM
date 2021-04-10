import sys
import json

data = json.load(sys.stdin)

for eg in data:
    print(eg['inputText'])
    print(eg['normalizedText'])