class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        obstacles = set(map(tuple,obstacles))
        # in 의 시간복잡도  list = O(n) set = O(1) 때문에 set으로 변환
        head = 0
        x,y=0,0
        distance=0
        for command in commands:
            if command == -1:
                head = (head+1)%4
            elif command == -2:
                head -=1
                if head<0:
                    head = 3
            else:
                for _ in range(command):
                    x=x+direction[head][0]
                    y=y+direction[head][1]
                    if (x,y) in obstacles:
                        x = x - direction[head][0]
                        y = y - direction[head][1]
                        break
                distance = max(distance,x**2+y**2)
        return distance
