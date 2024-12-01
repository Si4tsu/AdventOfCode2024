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

#Calculate similarity
def get_similarity(list1, list2):
    
    res = 0
    
    for id in list1:
        res += id * list2.count(id)
    
    return res

print(get_similarity(list1, list2))