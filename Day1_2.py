from sys import stdin

#Calculate similarity
def get_similarity(list1, list2):
    
    res = 0
    
    for id in list1:
        res += id * list2.count(id)
    
    return res

#Input to lists
with open("Day1.in") as file:
    lines = file.readlines()

    list1: list = []
    list2: list = []

    for line in lines:
        line = line.split("   ")

        list1.append(int(line[0]))
        list2.append(int(line[1]))

print(get_similarity(list1, list2))