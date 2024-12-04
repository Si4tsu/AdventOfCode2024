# ------ WIP -------

import re

def find_muls(line: str) -> list:

    # to ma działać a nie działa
    muls = re.findall(r"(?:(?<=do\(\))|.*?).*?(?<!don't\(\)).*?mul\((\d+),(\d+)\)",line)

    return muls

#Input    
with open("Day3/Day3.in") as file:
    memory = file.read()

#Result
res = 0

for m in find_muls(memory):
    res += int(m[0]) * int(m[1])

print(res)