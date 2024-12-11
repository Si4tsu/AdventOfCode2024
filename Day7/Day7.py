def can_make_value(value: int, nums: list[int], opt: str):
    val = nums[0]
    
    for i in range(1, len(nums)):
        if opt[i - 1] == "0":
            val *= nums[i]
        
        if opt[i - 1] == "1":
            val += nums[i]
    
    return val == value

def get_options(nums:list):
    first = "0" * (len(nums) - 1)
    last = "1" * (len(nums) - 1)
    
    opt = 0
    options = []   
    
    options.append(first)
    
    while bin(opt).lstrip("0b") != last:
        opt += 1
        bopt = bin(opt).lstrip("0b")
        options.append(("0" * (len(first) - len(bopt))) + bopt)

    return options

#Input
with open("Day7/Day7.in") as file:
    lines = file.readlines()

values = []
operations = []

for l in lines:
    l = l.split(":")
    values.append(int(l[0]))
    operations.append(list(map(int, l[1].split())))

print(values)
print(operations)

#Result

res = 0

for i in range(len(lines)):
    val = values[i]
    ops = operations[i]
    
    for option in get_options(ops):
        if can_make_value(val, ops, option):
            res += val
            break

print(res)