import cv2
from env import *

class Animation:
    def __init__(self, env, speed=10, dim=(600, 600)):
        self.env = env
        self.speed = speed
        self.dim = dim
    def play(self):
        cv2.namedWindow("Hawk-Dove", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Hawk-Dove", self.dim[0], self.dim[1])
        while not self.env.done():
            self.env.step()
            cv2.imshow("Hawk-Dove", self.env.state)
            cv2.waitKey(self.speed)


if __name__ == "__main__":
    env = Env(size=(100, 100))
    ani = Animation(env)
    ani.play(10)