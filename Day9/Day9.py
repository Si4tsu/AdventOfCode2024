def unpack(data: list[int]) -> list[int]:
    unpacked = []
    
    is_dgt = True
    dgt_index = 0
    
    for d in data:
        if is_dgt:
            for i in range(d):
                unpacked.append(dgt_index)
            
            dgt_index += 1
            is_dgt = False

        else:
            for i in range(d):
                unpacked.append(-1)
            
            is_dgt = True
    
    return unpacked

def pack_data(data: list[int]) -> list[int]:
    packed = data.copy()
    
    last_dgt = len(data) - 1
    
    for i in range(len(data)):
        if data[i] == -1:     
            while data[last_dgt] == -1:
                
                last_dgt -= 1
 
            if i >= last_dgt:
                return packed
            
            packed[i] = data[last_dgt]
            packed.pop(last_dgt)
            last_dgt -= 1


#Input
with open("Day9/Day9.in") as file:
    line = file.read()

data = list(map(int, line))


#Result
packed = pack_data(unpack(data)) 


print(sum(map(lambda x: x[0] * x[1] if x[0] > 0 else 0, zip(packed, range(len(packed))))))