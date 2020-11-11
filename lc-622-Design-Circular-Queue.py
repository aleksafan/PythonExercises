# https://leetcode.com/problems/design-circular-queue/

"""Design your implementation of the circular queue. 
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) 
principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not."""

class MyCircularQueue:

    def __init__(self, k: int):
        self.ring = [-1]*k
        self.busy = 0
        self.len = k
        self.head = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.len <=self.busy:
            return False
        self.ring[(self.busy+self.head)%self.len] = value
        self.busy+=1
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.busy<1:
            return False
        self.ring[self.head] = -1
        self.head = (self.head+1)%self.len
        self.busy-=1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.ring[self.head] 

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.ring[(self.busy + self.head - 1)%self.len]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return True if self.busy == 0 else False
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return True if self.len == self.busy else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()