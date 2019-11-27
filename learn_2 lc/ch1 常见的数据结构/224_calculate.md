# LeetCode 224 基本计算器 python实现

## 0. [LeetCode 题解链接](https://leetcode-cn.com/problems/basic-calculator/solution/li-yong-zhan-de-si-xiang-de-pythonshi-xian-by-dato/)

## 1. 题目描述：
- 实现一个基本的计算器来计算一个简单的字符串表达式的值。
  字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

## 2. 示例 :
- 输入: "1 + 1"
输出: 2

- 输入: " 2-1 + 2 "
输出: 3

- 输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23



## 3. 思路：

- 利用栈的思想
	- `stack`: 保存之前的表达式（相对于`tmp`来说）
	- `tmp`: 保存当前遍历的表达式 或 计算结果
	- 说明：如果遍历到`4`，`stack = [(,1,+]``tmp = [(,4]`
- `for c in s:` 
	- `c == ‘(’`: 遇到 `(`，说明新的表达式出现了，需要用`tmp` 暂存。如果此时 `tmp` 不为空，则将 `tmp` 入栈，`tmp` 再清空，`append(c)`；如果此时`tmp`为空，直接`append (c)`。
	- `c == ‘)’`: 说明目前的表达式(存在`tmp`中的) 应该计算出结果，再视情况考虑是否 ’规约‘。
			- 计算子表达式 `tmpRes = cal_tmp(tmp)`
			- 如果此时`stack`不为空，`tmpRes`应该和`stack`最后一个元素归约
			- 如果此时`stack`为空，`tmpRes`应该赋值给`tmp`，因为`tmp`始终保存当前遍历的计算结果
	- `c`为数字或计算符：直接入`tmp`就好

```
def calculate(self, s: str) -> int:
    s = “”.join(s.split())
    stack, tmp = [], []
    for c in s:
        if c == “(“ :
            if tmp:
                stack.append(tmp)
                tmp = []
            tmp.append(c)
        elif c == “)”:
            tmpRes = cal_tmp(tmp)
            if stack:
                stack[-1].append(tmpRes)
                tmp = stack.pop()
            else:
                tmp = [tmpRes]
        else:
            tmp.append(c)

    return  cal_tmp(tmp)
```


- tmpRes = cal_tmp(tmp):  
  - 由于`tmp`中只有加减法，所以设3个中间变量，`n:累加数字，以防有多位数；op:记录计算符；res:记录结果`

```
def cal_tmp(tmp):
    res = 0
    n = 0
    op = 1
    for t in range(len(tmp)):
        if tmp[t] == “+”:
            res += n * op
            op = 1
            n = 0 
        elif tmp[t] == “-“:
            res += n * op
            op = -1
            n = 0
        elif tmp[t] != “(“:
            n = n * 10 + int(tmp[t])
    res += n * op
    return str(res)

```