def is_safe(data):
    mono = 0
    
    data = list(map(int, data))
    

    if data[1] - data[0] < 0:
        mono = -1
    elif data[1] - data[0] > 0: 
        mono = 1
    else:
        return False
    
    for i in range(len(data) - 1):
        
        r = (data[i + 1] * mono) - (data[i] * mono)
        
        if r == 0:
            return False
        
        else:
            if r < 1 or r >3:
                return False 
        
        
    return True

#Input
with open("Day2.in") as file:
    lines = file.readlines()
    
for l in range(len(lines)):
    lines[l] = lines[l].split()


res = 0            
for line in lines:
    print(is_safe(line))
    if is_safe(line):
       res += 1
       
print(res)