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
