'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

        # 有个辅助栈，用空间换时间
        # 每次入栈时，都记录当前栈的min值
        self.minS = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.minS) == 0 or self.minS[-1] >= x:
            self.minS.append(x)
        else:
            self.minS.append(self.minS[-1])

    def pop(self) -> None:
        if self.data:
            self.minS.pop()
            return self.data.pop()
        

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        

    def getMin(self) -> int:
        if self.minS:
            return self.minS[-1]
        
