def is_pangram(pan):
    # pan -> the quick brown fox jumps over the lazy dog

    s = list(pan.lower())
    # ['t', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', ' ', 'b', 'r', 'o', 'w',
    # 'n', ' ', 'f', 'o', 'x', ' ', 'j', 'u', 'm', 'p', 's', ' ', 'o', 'v',
    # 'e', 'r', ' ', 't', 'h', 'e', ' ', 'l', 'a', 'z', 'y', ' ', 'd', 'o',
    # 'g']

    s.sort()
    # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', 'b', 'c', 'd', 'e', 'e',
    # 'e', 'f', 'g', 'h', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'o', 'o',
    # 'o', 'p', 'q', 'r', 'r', 's', 't', 't', 'u', 'u', 'v', 'w', 'x', 'y',
    # 'z']

    charArray = []
    for char in s:
        charArray.append(ord(char))

    # [32, 32, 32, 32, 32, 32, 32, 32, 97, 98, 99, 100, 101, 101, 101, 102,
    # 103, 104, 104, 105, 106, 107, 108, 109, 110, 111, 111, 111, 111, 112,
    # 113, 114, 114, 115, 116, 116, 117, 117, 118, 119, 120, 121, 122]

    for intAscii in range(97, 122):
        if not intAscii in charArray: # if ascii integer not found
            return False
    return True

#print(is_pangram("the quick brown fox jumps over the lazy dog"))
