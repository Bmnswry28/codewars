class Walker:
    def __init__(self):
        self.xcord = 0
        self.ycord = 0
    def walk(self,path):
        for direction in path:
            if direction == 'e':
                self.xcord += 1
            elif direction == 'w':
                self.xcord -= 1
            elif direction == 'n':
                self.ycord += 1
            elif direction == 's':
                self.ycord -= 1
    def coords(self):
        return (self.xcord, self.ycord)