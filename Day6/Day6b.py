##### ______ NIE DZIAŁĄ ______ ######

from enum import Enum

class Dir(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    

class Guard:
    def __init__(self, position: list[int], direction: Dir) -> None:  
        self.row = position[0]
        self.col = position[1]
        self.direction = direction
    
    def __str__(self) -> str:
        return f"[{self.row}, {self.col}] , {self.direction}"
    
    def place_obstackle(self, terrain: list[str]):
        obstackle = terrain.copy()
        
        match self.direction:
            case Dir.UP:
                c = self.col
                
                while c < len(terrain[0]):
                    if terrain[self.row][c] == "#":
                        obstackle[self.row - 1] = obstackle[self.row - 1][:self.col:] + "#" + obstackle[self.row - 1][self.col + 1::]
                        return obstackle
                    
                    c += 1
                
            case Dir.RIGHT:
                r = self.row
                
                while r < len(terrain):
                    if terrain[r][self.col] == "#":
                        obstackle[self.row] = obstackle[self.row][:self.col + 1:] + "#" + obstackle[self.row][self.col + 2::]
                        return obstackle
                    
                    r += 1
            
            case Dir.DOWN:
                c = self.col
                
                while c >= 0:
                    if terrain[self.row][c] == "#":
                        obstackle[self.row + 1] = obstackle[self.row + 1][:self.col:] + "#" + obstackle[self.row + 1][self.col + 1::]
                        return obstackle
                    
                    c -= 1
            
            case Dir.LEFT:
                r = self.row
                
                while r >= 0:
                    if terrain[r][self.col] == "#":
                        obstackle[self.row] = obstackle[self.row][:self.col - 1:] + "#" + obstackle[self.row][self.col::]
                        return obstackle
                    
                    r -= 1
        
        return []
        
    def make_step(self, terrain):
        old_position = [self.row, self.col]
        
        loop = 0
        can_step = False
        
        while not can_step:
            if loop >= 50:
                return "loop"
            
            match self.direction:
                
                case Dir.UP:
                    if self.row == 0:
                        return "out"
                    
                    if terrain[self.row - 1][self.col] == "X":
                        loop += 1
                    
                    if terrain[self.row - 1][self.col] == "#":
                        #terrain[self.row - 1] = terrain[self.row - 1][:self.col:] + "X" + terrain[self.row - 1][self.col + 1::]
                        self.direction = Dir.RIGHT
                    
                    else:
                        self.row -= 1
                        can_step = True

                case Dir.RIGHT:
                    if self.col == len(terrain[0]) - 1:
                        return "out"
                    
                    if terrain[self.row][self.col + 1] == "X":
                        loop += 1
                    
                    if terrain[self.row][self.col + 1] == "#":
                        #terrain[self.row] = terrain[self.row][:self.col + 1:] + "X" + terrain[self.row][self.col + 2::]
                        self.direction = Dir.DOWN
                    
                    else:
                        self.col += 1

                case Dir.DOWN:
                    if self.row == len(terrain) - 1:
                        return "out"
                    
                    if terrain[self.row + 1][self.col] == "X":
                        loop += 1
                    
                    if terrain[self.row + 1][self.col] == "#":
                        #terrain[self.row + 1] = terrain[self.row + 1][:self.col:] + "X" + terrain[self.row + 1][self.col + 1::]
                        self.direction = Dir.LEFT
                    
                    else:
                        self.row += 1
                
                case Dir.LEFT:
                    if self.col == 0:
                        return "out"
                    
                    if terrain[self.row][self.col - 1] == "X":
                        loop += 1
                    
                    if terrain[self.row][self.col - 1] == "#":
                        #terrain[self.row] = terrain[self.row][:self.col - 1:] + "X" + terrain[self.row][self.col::]
                        self.direction = Dir.UP
                    
                    else:
                        self.col -= 1
                        can_step = True                        
        
        return old_position
    
    #def place_obstackle(terrain):
    


def get_guard_position(terrain: list[str]) -> list[int]:
    
    position = [-1, -1]
    
    for row in range(len(terrain)):        
        position[1] = terrain[row].find("^")
        
        if position[1] != -1:            
            position[0] = row            
            break
    
    return position
            

#Input
with open("Day6/Day6.intest") as file:
    terrain = file.readlines()
    
    terrain = list(map(lambda s: s.strip(), terrain))


#Result
lab_guard = Guard(get_guard_position(terrain), Dir.UP)

options = []

res = 0

while True:
    if lab_guard.place_obstackle(terrain):
        options.append(lab_guard.place_obstackle(terrain))
    
    step = lab_guard.make_step(terrain)
    
    if step == "out":
        break

for opt in options:
    steps = 0
    while True:
        step = lab_guard.make_step(opt)
        
        steps += 1
        
        if steps >= 10000:
            res += 1
            break
        
        if step == "out":
            break

print(res)