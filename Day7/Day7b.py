def can_make_value(value: int, nums: list[int], opt: str):
    val = nums[0]
    
    for i in range(1, len(nums)):
        if opt[i - 1] == "0":
            val *= nums[i]
        
        if opt[i - 1] == "1":
            val += nums[i]
        
        if opt[i - 1] == "2":
            val = int(str(val) + str(nums[i]))
    
    return val == value

def get_options(nums:list):
    first = "0" * (len(nums) - 1)
    last = "2" * (len(nums) - 1)
    
    opt = 0
    options = []   
    
    options.append(first)
    
    while tri(opt) != last:
        opt += 1
        bopt = tri(opt)
        options.append(("0" * (len(first) - len(bopt))) + bopt)
    
    return options

def tri(num: int) -> str:
    res = ""
    while num != 0:
        res = str(num % 3) + res
        num = num // 3
    
    return res


#Input
with open("Day7/Day7.in") as file:
    lines = file.readlines()

values = []
operations = []

for l in lines:
    l = l.split(":")
    values.append(int(l[0]))
    operations.append(list(map(int, l[1].split())))


#Result

#for i in range(len(values)):
#    print(str(values[i]) + " - " + str(operations[i]))

res = 0

for i in range(len(lines)):
    val = values[i]
    ops = operations[i]
    
    for option in get_options(ops):
        if can_make_value(val, ops, option):
            res += val
            break

print(res)