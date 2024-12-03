import re

def find_muls(line: str) -> list:
    
    muls = re.findall(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)",line)    
    
    return muls

def fixed_muls(muls: list):
    
    do = 0
    
    fixed = []
    
    for mul in muls:
        if mul == "do()":
            do = 1
            continue
        
        if mul == "don't()":
            do = -1
            continue
        
        if do != -1:
            mul = mul[4:-1].split(",")
            mul = list(map(int, mul))
            fixed.append(mul)
            
    return fixed

#Input    
with open("Day3/Day3.in") as file:
    memory = file.read()

#Result
res = 0

for m in fixed_muls(find_muls(memory)):
    res += m[0] * m[1]

print(res)