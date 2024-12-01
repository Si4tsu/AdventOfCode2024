from sys import stdin

#Test input
'''
3   4
4   3
2   5
1   3
3   9
3   3
'''

#Input to lists
lines = stdin.readlines()

list1: list = []
list2: list = []

for line in lines:
    line = line.split("   ")

    list1.append(int(line[0]))
    list2.append(int(line[1]))

#Calculate distance
def get_distance(list1, list2):
    list1.sort()
    list2.sort()
    
    res = 0
    
    for i in range(len(list1)):
        res += abs(list1[i] - list2[i])
    
    return res

print(get_distance(list1, list2))