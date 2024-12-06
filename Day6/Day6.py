from enum import Enum

class Dir(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    

class Guard:
    def __init__(self, position: list[int], direction: Dir, terrain) -> None:  
        self.row = position[0]
        self.col = position[1]
        self.direction = direction
        
        self.terrain = terrain 
    
    def __str__(self) -> str:
        return f"[{self.row}, {self.col}] , {self.direction}"
    
    def make_step(self):
        old_position = [self.row, self.col]
        
        can_step = False
        
        while not can_step:
            match self.direction:
                
                case Dir.UP:
                    if self.row == 0:
                        return "out"
                    
                    if self.terrain[self.row - 1][self.col] == "#":
                        self.direction = Dir.RIGHT
                    
                    else:
                        self.row -= 1
                        can_step = True

                case Dir.RIGHT:
                    if self.col == len(self.terrain[0]) - 1:
                        return "out"
                    
                    if self.terrain[self.row][self.col + 1] == "#":
                        self.direction = Dir.DOWN
                    
                    else:
                        self.col += 1
                        can_step = True

                case Dir.DOWN:
                    if self.row == len(self.terrain) - 1:
                        return "out"
                    
                    if self.terrain[self.row + 1][self.col] == "#":
                        self.direction = Dir.LEFT
                    
                    else:
                        self.row += 1
                        can_step = True
                
                case Dir.LEFT:
                    if self.col == 0:
                        return "out"
                    
                    if self.terrain[self.row][self.col - 1] == "#":
                        self.direction = Dir.UP
                    
                    else:
                        self.col -= 1
                        can_step = True                        
        
        return old_position


def get_guard_position(terrain: list[str]) -> list[int]:
    
    position = [-1, -1]
    
    for row in range(len(terrain)):        
        position[1] = terrain[row].find("^")
        
        if position[1] != -1:            
            position[0] = row            
            break
    
    return position
            

#Input
with open("Day6/Day6.in") as file:
    terrain = file.readlines()


#Result
lab_guard = Guard(get_guard_position(terrain), Dir.UP, terrain)

res_map = [[0 for col in range(len(terrain[0]) - 1)] for row in range(len(terrain) - 1)]

while True:
    step = lab_guard.make_step()
    
    if step == "out":
        res_map[lab_guard.row][lab_guard.col] = 1
        break
    
    res_map[step[0]][step[1]] = 1

print(sum(list(map(sum, res_map))))
