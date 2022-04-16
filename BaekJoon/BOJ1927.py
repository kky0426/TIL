from sys import stdin

N = int(stdin.readline())

class Heap():
    def __init__(self):
        self.arr = [0]

    def heapify(self,idx):
        left = idx*2
        right = idx*2+1

        smallest = idx
        if right<len(self.arr) and self.arr[right] < self.arr[smallest]:
            smallest = right
        if left<len(self.arr) and self.arr[left] < self.arr[smallest]:
            smallest = left

        if smallest != idx:
            self.arr[idx],self.arr[smallest] = self.arr[smallest],self.arr[idx]
            self.heapify(smallest)

    def push(self,num):
        self.arr.append(num)
        idx = len(self.arr)-1

        while idx>1:
            parent = idx//2
            if self.arr[idx]<self.arr[parent]:
                self.arr[idx],self.arr[parent] = self.arr[parent],self.arr[idx]
                idx = parent
            else:
                break

    def pop(self):
        if len(self.arr)>1:
            self.arr[1],self.arr[-1] = self.arr[-1],self.arr[1]
            num = self.arr.pop()
            self.heapify(1)
            return num
        else:
            return 0

heap = Heap()

for _ in range(N):
    command = int(stdin.readline())
    if command == 0:
        print(heap.pop())
    else:
        heap.push(command)



