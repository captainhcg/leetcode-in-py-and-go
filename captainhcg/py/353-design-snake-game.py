class SnakeGame(object):

    def __init__(self, width, height, food):
        from collections import deque
        self.width = width
        self.height = height
        self.food = food
        self.foodIdx = 0
        self.bodies = deque([(0, 0)])
        self.blocks = set([(0, 0)])

    def move(self, direction):
        y, x = self.bodies[0]
        if direction == "U":
            y -= 1
        elif direction == "D":
            y += 1
        elif direction == "L":
            x -= 1
        else:
            x += 1
        
        new_block = (y, x)
        if self.foodIdx < len(self.food) and tuple(self.food[self.foodIdx]) == new_block:
            self.bodies.appendleft(new_block)
            self.blocks.add(new_block)
            self.foodIdx += 1
        else:
            self.bodies.appendleft(new_block)
            to_remove = self.bodies.pop()
            self.blocks.remove(to_remove)
            if new_block in self.blocks:
                return -1
            elif y < 0 or x < 0 or y >= self.height or x >= self.width:
                return -1
            self.blocks.add(new_block)
            
        return self.foodIdx
