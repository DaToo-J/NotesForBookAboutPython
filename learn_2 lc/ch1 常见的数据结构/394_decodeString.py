 #!/usr/bin/python
# -*- coding: utf-8 -*-
'''
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == "[":
                stack.append([multi, res])
                res, multi = "", 0 # res: 只记录当前的结果，只有字母的🍢
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res 
            else:
                res += c 
        return res 

