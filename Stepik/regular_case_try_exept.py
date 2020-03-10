import sys
import re

pattern = r'\\'

for line in sys.stdin:
    line = line.rstrip()
    try:
        match_obj = re.search(pattern, line)
        if match_obj.group(0):
            print(line)
                 
    except AttributeError:
        continue