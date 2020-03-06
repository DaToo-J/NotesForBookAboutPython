'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 1：

输入：m = 3, n = 1, k = 0
输出：1

'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumOfIndex(i,j):
            Sum = 0
            while i:
                Sum += i % 10
                i = int(i / 10)
            while j:
                Sum += j % 10
                j = int(j / 10)
            return Sum

        '''
        BFS 广度优先
        1. 利用队列的思想，每次遍历队列的头，遍历完头之后，将其相邻元素也加入队列`tmp`
        2. 如果当前元素的坐标和小于等于`k`，则将其添加到集合`res`中，这一步可以去重
        '''
        res = set()
        tmp = [(0,0)]
        while tmp:
            x, y = tmp.pop(0)
            if (x,y) not in res and sumOfIndex(x,y)<=k:
                res.add((x,y))
                for dx,dy in [(1,0),(0,1)]:
                    if 0<=x+dx<m and 0<=y+dy<n:
                        tmp.append((x+dx, y+dy))
        return len(res)
