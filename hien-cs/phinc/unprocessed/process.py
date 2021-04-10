import sys
import csv
import preprocessor

reader = csv.reader(sys.stdin)
next(reader)
for orig_tweet, eng_tweet in reader:
    print(preprocessor.clean(orig_tweet))