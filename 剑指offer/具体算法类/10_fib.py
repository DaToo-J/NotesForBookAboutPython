'''

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入：n = 2
输出：1
'''
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        n0 = 0
        n1 = 1

        for i in range(n-1):
            n2 = n0 + n1
            n0, n1 = n1, n2

        return n2 % 1000000007
