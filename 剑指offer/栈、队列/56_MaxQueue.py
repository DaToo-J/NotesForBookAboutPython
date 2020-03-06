class MaxQueue:
    '''
    请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的时间复杂度都是O(1)。

    若队列为空，pop_front 和 max_value 需要返回 -1

    示例 1：
    输入: 
    ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
    [[],[1],[2],[],[],[]]
    输出: [null,null,null,2,1,2]


    思路：双队列、辅助栈
        利用 self.helper 记录当前 self.queue 的最大值
        当 push 的值 > self.helper[-1], 则循环将 self.helper的尾巴跳出
        然后，再将value append进去

    '''

    def __init__(self):
        self.queue = []
        self.helper = []

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return self.helper[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.helper and self.helper[-1] < value:
            self.helper.pop(-1)
        self.helper.append(value) 
        return None

    def pop_front(self) -> int:
        if not self.queue:
            return -1

        if self.helper and self.helper[0] == self.queue[0]:
            self.helper.pop(0)

        return self.queue.pop(0)


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()