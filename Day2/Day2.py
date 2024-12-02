def is_safe(data: list):
    mono = 0
    
    if data[1] == data[0]:
        return False

    if data[1] < data[0]:
        mono = -1
        
    elif data[1] > data[0]: 
        mono = 1
    
    for i in range(len(data) - 1):
        
        r = (data[i + 1] * mono) - (data[i] * mono)
        
        if r == 0:
            return False
        
        if r < 1 or r >3:
            return False     
        
    return True


#Input
with open("Day2\Day2.in") as file:
    lines = file.readlines()
    
    data = []
    
    for line in lines:
        data.append(list(map(int, line.split())))


#Result
res = 0            
for line in data:
    if is_safe(line):
       res += 1
       
print(res)