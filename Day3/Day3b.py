import re

def find_muls(line: str) -> list:
    
    muls = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)",line)    
    
    return muls

def fixed_muls(muls: list[str]) -> list:
    
    do = True
    
    fixed = []
    
    for mul in muls:
        if mul == "do()":
            do = True
            continue
        
        if mul == "don't()":
            do = False
            continue

        if do:
            mul = mul[4:-1].split(",")
            mul = list(map(int, mul))
            fixed.append(mul)

    return fixed

#Input    
with open("Day3/Day3.in") as file:
    memory = file.read()

#Result
res = sum(map(lambda x: x[0] * x[1], fixed_muls(find_muls(memory))))

print(res)