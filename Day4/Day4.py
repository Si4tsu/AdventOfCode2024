def find_xmas(lines: list[str]):
    found = 0
    
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == "X":
                #right
                if col + 3 <= len(lines[row]) - 1:
                    if lines[row][col + 1]+lines[row][col + 2]+lines[row][col + 3] == "MAS":
                        found += 1
                
                #left
                if col - 3 >= 0:
                    if lines[row][col - 1]+lines[row][col - 2]+lines[row][col - 3] == "MAS":
                        found += 1
                
                #down
                if row + 3 <= len(lines) - 1:
                    if lines[row + 1][col]+lines[row + 2][col]+lines[row + 3][col] == "MAS":
                        found += 1
                #up
                if row - 3 >= 0:
                    if lines[row - 1][col]+lines[row - 2][col]+lines[row - 3][col] == "MAS":
                        found += 1
                        
                #right-down
                if (col + 3 <= len(lines[row]) - 1) and (row + 3 <= len(lines) - 1):
                    if lines[row + 1][col + 1]+lines[row + 2][col + 2]+lines[row + 3][col + 3] == "MAS":
                        found += 1
                
                #right-up
                if (col + 3 <= len(lines[row]) - 1) and (row - 3 >= 0):
                    if lines[row - 1][col + 1]+lines[row - 2][col + 2]+lines[row - 3][col + 3] == "MAS":
                        found += 1
                
                #left-down
                if (col - 3 >= 0) and (row + 3 <= len(lines) - 1):
                    if lines[row + 1][col - 1]+lines[row + 2][col - 2]+lines[row + 3][col - 3] == "MAS":
                        found += 1
                
                #left-up
                if (col - 3 >= 0) and (row - 3 >= 0):
                    if lines[row - 1][col - 1]+lines[row - 2][col - 2]+lines[row - 3][col - 3] == "MAS":
                        found += 1
    
    return found


#Input
with open("Day4/Day4.in") as file:
    lines = file.readlines()
    
#Result
print(find_xmas(lines))