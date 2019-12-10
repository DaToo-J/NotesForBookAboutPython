class MyQueue:
    '''
    使用栈实现队列的下列操作：

    push(x) -- 将一个元素放入队列的尾部。
    pop() -- 从队列首部移除元素。
    peek() -- 返回队列首部的元素。
    empty() -- 返回队列是否为空。
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.helper:
            return self.helper.pop()
        if self.data:
            while self.data:
                self.helper.append(self.data.pop())
            return self.helper.pop()
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.helper:
            return self.helper[-1]
        if self.data:
            while self.data:
                self.helper.append(self.data.pop())
            return self.helper[-1]
          

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.helper or self.data:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()