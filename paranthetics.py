"""Check a string to see if all the parantheses are closed."""


from que import Queue


def check_parens(str):
    """Push a string into a linked list and check if all the parens close."""
    paren_q = Queue()
    for char in str:
        paren_q.enqueue(char)
    try:
        curr = paren_q.dequeue()
    except IndexError:
        curr = None
    counter = 0
    while curr:
        if curr == '(' and counter >= 0:
            counter += 1
        elif curr == ')':
            counter -= 1
        try:
            curr = paren_q.dequeue()
        except IndexError:
            break
    counter = 1 if counter > 0 else -1 if counter < 0 else 0
    # if counter > 0:
    #     counter = 1
    # elif counter < 0:
    #     counter = -1
    return counter


if __name__ == '__main__':
    print(check_parens('((()))('))
