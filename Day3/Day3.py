import re

def find_muls(line: str) -> list:
    
    muls = re.findall(r"mul\([0-9]+,[0-9]+\)",line)    
    
    for i in range(len(muls)):
        muls[i] = muls[i][4:-1].split(",")
        muls[i] = list(map(int, muls[i]))
    
    return muls

#Input
with open("Day3/Day3.in") as file:
    memory = file.read()

#Result
res = 0
for m in find_muls(memory):
    res += m[0] * m[1]

print(res)
        
    
