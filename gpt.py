
with open('data.txt', 'r') as f:
    data = f.read()
    f.close()

acceptance = [1,2,3]
safe_list = 0
for i in data.splitlines():
    i = i.split()
    list_len = (len(i))
    asc = 0
    desc = 0
    #mistake_handler = 0
    for itrr in range(0, list_len-1):
        first = int(i[itrr])
        second = int(i[itrr+1])
        if (first > second and abs(first -second) in acceptance):
            asc += 1
            
        if (first < second and abs(first - second) in acceptance):
            desc += 1

    if asc == list_len-1 or desc == list_len-1:
        safe_list += 1
            
print(safe_list)

def asc_trend(i):
    acceptance = [1,2,3]
    asc = 0
    list_len = (len(i))
    for itrr in range(list_len-1):
        first = int(i[itrr])
        second = int(i[itrr+1])

        if (first > second and abs(first -second) in acceptance):
            asc += 1
        else:
            return itrr
        
    if asc == list_len-1:
        return 'cool'

def desc_trend(i):
    acceptance = [1,2,3]
    desc = 0
    list_len = (len(i))
    for itrr in range(list_len-1):
        first = int(i[itrr])
        second = int(i[itrr+1])

        if (first < second and abs(first -second) in acceptance):
            desc += 1
        else:
            return itrr
    if desc == list_len-1:
        return 'cool'
    
good = 0
for i in data.splitlines():
    i1 = i.split()
    i2 = i1.copy()
    i3 = i1.copy()
    x = asc_trend(i1)

    if x == 'cool':
        good += 1 
        #print(i1)
    else:
        x = int(x)
        i2.pop(x)
        #print(i1, x+1)
        i3.pop(x+1)
        if asc_trend(i2) == 'cool':
            good += 1
        elif asc_trend(i3) == 'cool':
            good += 1

    i2 = i1.copy()
    i3 = i1.copy()
    
    x2 = desc_trend(i1)
    if x2 == 'cool':
        good += 1 
    else:
        x2 = int(x2)
        i2.pop(x2)
        i3.pop(x2+1)
        if desc_trend(i2) == 'cool':
            good += 1
        elif desc_trend(i3) == 'cool':
            good += 1 

print(good)