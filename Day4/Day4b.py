def find_xmas(lines: list[str]):
    found = 0
    
    for row in range(len(lines)):
        if row == 0 or row == len(lines) - 1:
            continue
        
        for col in range(len(lines[row])):
            if col == 0 or col == len(lines[row]) - 1:
                continue
            
            
            if lines[row][col] == "A":
                
                #right-up & left-down
                rt = False
                
                if lines[row + 1][col + 1] == "M" and lines[row - 1][col - 1] == "S":
                    rt = True
                
                if lines[row + 1][col + 1] == "S" and lines[row - 1][col - 1] == "M":
                    rt = True
                
                #left-up & right-down
                lt = False
                
                if lines[row + 1][col - 1] == "M" and lines[row - 1][col + 1] == "S":
                    lt = True
                
                if lines[row + 1][col - 1] == "S" and lines[row - 1][col + 1] == "M":
                    lt = True
                
                if rt and lt:
                    found += 1
                
    return found


#Input
with open("Day4/Day4.in") as file:
    lines = file.readlines()
    
#Result
print(find_xmas(lines))