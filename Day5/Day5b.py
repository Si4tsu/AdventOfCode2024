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

def get_impostor(line: list[int], rules: list) -> int:
    for n in line:
        for r in rules:
            if n == r:
                return n
    
    return -1
        
def is_key(rules, x):
            
    for r in rules:
        if r == x:
            return True
    
    return False

def get_incorrect_updates(updates: list[list], rules: dict) -> list:
    incorrect_updates = []

    impostor = 0

    for line in updates:
        
        is_correct = True
        
        for u in range(len(line)):
            #Check index
            
            if not is_key(rules, line[u]):
                continue
            
            #Check correction
            
            impostor = get_impostor(line[u + 1::], rules[line[u]])
            
            if impostor == -1:
                continue
            
            while impostor != -1:
                imp_index = line.index(impostor)
                
                line.pop(imp_index)
                line.insert(u, impostor)
                
                if not is_key(rules, line[u]):
                    break
                #FUCKKKKKKKKKK
                impostor = get_impostor(line[u + 1::], rules[line[u]])
                
            is_correct = False
            break
        
        if  not is_correct:
            print(line)
            incorrect_updates.append(line)
    
    
    return incorrect_updates

    


#Input
with open("Day5/Day5.intest") as file:
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

for update in get_incorrect_updates(updates, get_rules(order)):
    res += update[(len(update) - 1)//2]

#print(res)
#print(get_incorrect_updates(updates, get_rules(order)))