"""."""


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
