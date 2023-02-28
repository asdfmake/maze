array = [
    [1, 2, 3],
    [4, "*", "S"],
    ["F", 8, 9]
]
#sfPos = start-finish Position
def sfPos():
    class Res:
        def __str__(self):
            return f"Start position='{self.s}', Finish position={self.f}"
        pass
    res = Res()
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            # Check if the current element matches the target element
            if array[i][j] == "S":
                # Print the position of the target element
                res.s = {"i": i, "j": j}
            elif array[i][j] == "F":    
                res.f = {"i": i, "j": j}
    return res
    
class Player:
    
    def __init__(self, i, j):
        self.i = i
        self.j = j
        print(f"Player is at: {i}, {j}")
    
    def moveUp(self, arg):
        arg.i = arg.i + 1
        arg.j = arg.j
        
    def moveDown(self, arg):
        arg.i = arg.i - 1
        arg.j = arg.j
        
    def moveRight(self, arg):
        arg.i = arg.i
        arg.j = arg.j + 1
    
    def moveLeft(self, arg):
        arg.i = arg.i
        arg.j = arg.j - 1
        
    def getPos(self):
        return {'i': self.i, 'j': self.j}
    
positions = sfPos()
player = Player(positions.s['i'], positions.s['j'])
print(sfPos())

moves = []

