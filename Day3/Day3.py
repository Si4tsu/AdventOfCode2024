import re

def find_muls(line: str) -> list:
    
    muls = re.findall(r"mul\((\d+),(\d+)\)",line)
    
    return list(map(lambda x: list(map(int, x)), muls))

#Input
with open("Day3/Day3.in") as file:
    memory = file.read()

#Result
res = sum(map(lambda x: x[0] * x[1], find_muls(memory)))

print(res)