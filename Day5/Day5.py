import re

def get_rules(order: list[int]) -> dict:
    rules = {}
    
    for o in order:
        is_o = False
        
        for r in rules:
            if r == o[1]:
                is_o = True
                break
        
        if is_o:
            rules[o[1]].append(o[0])
        
        else:
            rules.update({o[1]: [o[0]]})
    
    return rules

def is_ordered(line: list[int], rules: list) -> bool:
    for n in line:
        for r in rules:
            if n == r:
                return False
    
    return True
        
def get_correct_updates(updates: list, rules: dict) -> list:
    correct_updates = []

    for line in updates:
        
        is_correct = True
        
        for u in range(len(line)):
            is_key = False
            
            for r in rules:
                if r == line[u]:
                    is_key = True
                    break
            
            if not is_key:
                continue
                
            if not is_ordered(line[u + 1::], rules[line[u]]):
                is_correct = False
                break
        
        if is_correct:
            correct_updates.append(line)
    
    return correct_updates

#Input
with open("Day5/Day5.in") as file:
    lines = file.readlines()

    order = []

    updates = []

    for i in range(len(lines)):
        if re.findall(r"\|", lines[i]):
            order.append(list(map(int, lines[i].split("|"))))
        
        if re.findall(",", lines[i]):
            updates.append(list(map(int, lines[i].split(","))))

#Result

res = 0

for update in get_correct_updates(updates, get_rules(order)):
    res += update[(len(update) - 1)//2]

print(res)