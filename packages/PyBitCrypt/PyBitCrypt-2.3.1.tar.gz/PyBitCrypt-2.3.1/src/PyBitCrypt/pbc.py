CharList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            ' ', '`', '~', '1', '!', '2', '@', '3', '#', '4', '$', '5', '%',
            '6', '^', '7', '&', '8', '*', '9', '(', '0', ')', '-', '_', '=',
            '+', '[', '{', ']', '}', '\\', '|', ';', ':', "'", '"', ',', '<',
            '.', '>', '/', '?', '\n']

def encrypt(key:str, text:str):
    KeyList = []
    for w in key:
        num = CharList.index(w)
        KeyList.append(num)

    TextList = []
    for e in text:
        num = CharList.index(e)
        TextList.append(num)

    OutList = []
    count = 0
    for r in TextList:
        t = KeyList[count%len(KeyList)]
        OutList.append(r+t)
        count += 1

    output = ''
    for y in OutList:
        u = y%len(CharList)
        output = output + CharList[u]
        
    return output

def decrypt(key:str, text:str):
    KeyList = []
    for w in key:
        num = CharList.index(w)
        KeyList.append(num)

    TextList = []
    for e in text:
        num = CharList.index(e)
        TextList.append(num)

    OutList = []
    count = 0
    for r in TextList:
        t = KeyList[count%len(KeyList)]
        OutList.append(r-t)
        count += 1

    output = ''
    for y in OutList:
        u = y%len(CharList)
        output = output + CharList[u]

    return output
