"""String Pyramid code kata."""


def watch_pyramid_from_the_side(characters):
    """Display the pyramid as viewed from the side."""
    if characters is None:
        return None
    elif characters == '':
        return ''
    ret_str = ''
    characters = characters[::-1]
    for i, char in enumerate(characters):
        count = len(characters) - i - 1
        spaces = ' ' * count
        ret_str += spaces + char * (i * 2 + 1) + spaces
        if not (i + 1) == len(characters):
            ret_str += '\n'
    return ret_str


def watch_pyramid_from_above(characters):
    """Display pyramid as viewed from the top."""
    if characters is None:
        return None
    elif characters == '':
        return ''
    ret_list = []
    used = []
    for i, char in enumerate(characters):
        used.append(char)
        add_str = ''
        for ctr, used_char in enumerate(used):
            if ctr == len(used) - 1:
                count = len(characters) - len(used)
                add_str += used_char * count
            else:
                add_str += used_char
        add_str = add_str + char + add_str[::-1]
        ret_list.append(add_str)
    mirror = ret_list[::-1]
    del mirror[0]
    ret_list.extend(mirror)
    ret_list = '\n'.join(ret_list)
    return ret_list


def count_visible_characters_of_the_pyramid(characters):
    """Return a count of the number of visible stones."""
    if not characters:
        return -1
    count = len(characters) * 2 - 1
    return count * count


def count_all_characters_of_the_pyramid(characters):
    """Return a count of the number of used stones."""
    if not characters:
        return -1
    ret_val = 0
    for i in range(len(characters)):
        ret_val += (2 * i + 1) * (2 * i + 1)
    return ret_val
