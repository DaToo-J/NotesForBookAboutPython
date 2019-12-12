class MyStack:
    '''
    使用队列实现栈的下列操作：

    push(x) -- 元素 x 入栈
    pop() -- 移除栈顶元素
    top() -- 获取栈顶元素
    empty() -- 返回栈是否为空

    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.data:
            while len(self.data) > 1:
                self.helper.append(self.data.pop(0))
            res = self.data.pop()
            self.data = self.helper
            self.helper = []
            return res 

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.data:
            while len(self.data) > 1:
                self.helper.append(self.data.pop(0))
            res = self.data[-1]
            self.data = self.helper + self.data
            self.helper= []
            return res         

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if self.data:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()