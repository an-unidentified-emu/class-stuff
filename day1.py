with open('data.txt', 'r') as f:
    raw = f.read()
    f.close()

x = raw.split('\n')
x_mod = []
for i in range(len(x)):
    x_mod.append(x[i].split(' '))
y=[]

def safety(report):
    damper = False
    while i < range(len(report)):
        if i == 0:
            if report[i] > report[i+1]: increase = False
            else: increase = True
        if i == len(report)-1: return True
        if report[i] < report[i+1] and not increase: return False
        if report[i] > report[i+1] and increase: return False
        if abs(report[i]-report[i+1]) > 3 or abs(report[i]-report[i+1]) < 1: return False
        i+=1



for i in x_mod:
    k = []
    for j in i:
        try: k.append(int(j))
        except: print(j)
    y.append(k)
out = 0
print(y)
for report in y:
    #print(safety(report))
    if safety(report) == True: out +=1
print(out)
        
