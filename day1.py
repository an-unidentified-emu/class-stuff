with open('data.txt', 'r') as f:
    raw = f.read()
    f.close()

#raw = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
nums = ['0','1','2','3','4','5','6','7','8','9']
validChars = ['0','1','2','3','4','5','6','7','8','9',',',')']
def go(raw):
    total = 0
    on = True
    while 'mul(' in raw:
        mul = 1
        do = raw.find('do()')
        dont = raw.find("don't()")
        start = raw.find('mul(')
        if do == -1: do = 2147483647
        if dont == -1: dont = 2147483647
        #if start < do and start < dont: pass
        if do < start and do < dont: on = True
        elif dont < start and dont < do: on = False
        if on:
            data = raw[start:]
            if isValid(data):
                temp = data[data.find('(')+1:data.find(')')]
                temp = temp.split(',')
                for i in temp:
                    mul *= int(i)
                print(mul)
            else:
                mul = 0
            total += mul
        raw = raw[start + 1:]  # Continue processing the rest of the string
    return total


def isValid(data):
    spot = 0
    for i in range(4,12):
        try:
            if data[i]: pass
        except:
            return False
        if data[i] in nums and spot == 0:
            spot +=1
        if data[i] == ',' and spot == 1:
            spot +=1
        if data[i] in nums and spot == 2:
            spot +=1
        if data[i] == ')' and spot == 3: 
            spot +=1
        if data[i] not in validChars: return False
        if i == 6 and spot < 1: return False
        if i == 7 and spot < 2: return False
        if i == 11 and spot < 3: return False
        if i == 12 and spot < 4: return False
        if spot == 4: return True

print(go(raw))
