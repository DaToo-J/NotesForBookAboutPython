 #!/usr/bin/python
# -*- coding: utf-8 -*-
def isAnagram( s, t):
    '''
        题242:
        判断字符串s 和 t 是否是异位词
    '''
    # 判断长度
    if len(s) != len(t):
        return False

    # 26个字母计数
    latter = [0] * 26

    # 法1: 遍历s、t
    for i in s:
        # 字符i的index
        index_i = ord(i) - ord('a')
        latter[index_i] += 1
    for i in t:
        index_i = ord(i) - ord('a')
        latter[index_i] -= 1

    # 法2: 同时遍历s、t
    # for i in range(len(s)):
    #     latter[ord(s[i]) - ord('a')] += 1
    #     latter[ord(t[i]) - ord('a')] -= 1

    if latter == [0]*26:
        return True
    else:
        return False

def main():
    s = "anagram"
    t = "nagaram"
    res = isAnagram(s,t)
    print(res)



if __name__ == '__main__':
    main()