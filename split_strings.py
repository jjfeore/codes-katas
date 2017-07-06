"""Kata: Split Strings.

Split a string into character pairs and add an '_' to a trailing odd character

#1 Best Practices Solution by mstrfx

def solution(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]
"""


def solution(s):
    """."""
    if s:
        cat_str = ''
        ret_list = []
        for letter in s:
            cat_str += letter
            if len(cat_str) == 2:
                ret_list.append(cat_str)
                cat_str = ''
        if len(cat_str) == 1:
            ret_list.append(cat_str + '_')
        return ret_list
    else:
        return []
