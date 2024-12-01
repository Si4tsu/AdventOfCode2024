from sys import stdin

#Calculate distance
def get_distance(list1, list2):
    list1.sort()
    list2.sort()
    
    res = 0
    
    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])
    
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

print(get_distance(list1, list2))