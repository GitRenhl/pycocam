import math
import pyxel

import random
import pycocam

class App:
    points = ()
    c = pycocam.Pycocam(200, 150)

    def __init__(self):
        pyxel.init(200, 150, caption='Pyxel pycocam demo')

        # In order to have a better view for this demo
        self.c.z = -4.55

        for i in range(1, 100):
            self.points = self.points + ((random.randint(-2, 2),
                random.randint(-2, 2),
                random.randint(-2, 2)), )
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        for i in range(0, len(self.points)):
            self.c.point(self.points[i], (i % 15) + 1)
        
        for i in range(-20, 20, 3):
           self.c.line((1,  i/10,  1), (1,  i/10, -1), 7)
           self.c.line((1,  i/10, -1), (-1, i/10, -1), 7)
           self.c.line((-1, i/10, -1), (-1, i/10,  1), 7)
           self.c.line((-1, i/10,  1), (1,  i/10,  1), 7)

    def update(self):
        self.c.theta += 0.01

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

App()
