chars = 'abcdefghijklmnopqrstuvwxyz1234567890'  # Easily changeable


def iterchar(item, pos):
    item_old = item
    item = list(item)
    char = item.pop(pos)
    newchar = chars[chars.index(char) + 1]
    item.insert(pos, newchar)
    item = ''.join(item)[:pos + 1]
    item += chars[0] * (len(item_old) - len(item))
    return item


def iter_str(prev):
    n = 0
    fullreplace = True
    for char in prev[::-1]:  # reversed
        if char != chars[len(chars) - 1]:  # if not last char
            fullreplace = False
            break
        else:
            n += 1
    if fullreplace:
        return chars[0] * (len(prev) + 1)  # ex: '000' --> 'aaaa'
    else:
        n = len(prev) - n - 1
        return iterchar(prev, n)


def brute_forcer(start=chars[0]):
    x = start
    while True:
        try:
            yield x
        finally:  # So that yield doesn't end the function
            x = iter_str(x)
