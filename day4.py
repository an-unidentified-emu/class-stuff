with open('data.txt', 'r') as f:
    raw = f.read()
    f.close()
raw = raw.split('\n')
data = []
for i in raw:
    data.append(list(i))
out = 0
for i in range(len(data)-1):
    for j in range(len(data[i])-1):
        if data[i][j] == 'X':
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1
                        if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-2][j] == 'S': out +=1