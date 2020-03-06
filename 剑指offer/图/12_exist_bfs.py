'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        深度优先遍历
        '''
        def dfs(board, i, j, word):
            if len(word) == 0: return True  # 如果不加这句，会一直遍历下去，跳不出循环
            if not len(board)>i>=0 or not len(board[0])>j>=0 or board[i][j] != word[0]: return False # 判断边界和当前` board[i][j]==word[0]`
            tmp, board[i][j] = board[i][j], '/' # 避免` board[i][j]` 被重复遍历“记录在案”
            res = dfs(board,i+1,j,word[1:]) or dfs(board,i-1,j,word[1:]) or dfs(board,i,j+1,word[1:]) or dfs(board,i,j-1,word[1:])
            board[i][j] = tmp  # 回填 ` board[i][j]`
            return res


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, word):
                        return True

        return False