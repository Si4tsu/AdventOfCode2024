def is_safe(data: list):
    data = list(map(int, data))
    
    mono = 0

    if data[1] - data[0] < 0:
        mono = -1
    elif data[1] - data[0] > 0: 
        mono = 1
    else:
        return False
    
    for i in range(len(data) - 1):
        
        r = (data[i + 1] * mono) - (data[i] * mono)
        
        if r == 0:
            if not is_safe(data.pop(i)):
                return False
        
        else:
            if r < 1 or r >3:
                if not is_safe(data.pop(i)) or not is_safe(data.pop(i + 1)):
                    return False 
        
        
    return True

def get_options(data: list):
    mono = 0
    
    opt = []

    for d in data:
        opt.append(data.pop(d))

    '''if data[1] - data[0] < 0:
        mono = -1
    elif data[1] - data[0] > 0: 
        mono = 1
    else:
        opt.append(data.pop(0))'''
        
    return opt



#Input
with open("Day2.in") as file:
    lines = file.readlines()
    
for l in range(len(lines)):
    lines[l] = lines[l].split()


res = 0            
for line in lines:
    if is_safe(line):
       res += 1
    else:
        
        
        pass
       
print(res)