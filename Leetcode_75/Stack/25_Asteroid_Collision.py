from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]

                if top < -a:          # top is smaller -> top explodes
                    stack.pop()
                    continue
                elif top == -a:       # both explode
                    stack.pop()
                    alive = False
                else:                 # incoming is smaller -> incoming explodes
                    alive = False

            if alive:
                stack.append(a)

        return stack