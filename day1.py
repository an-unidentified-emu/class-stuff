with open('data.txt', 'r') as f:
    raw = f.read()
    f.close()

x = raw.split('\n')
x_mod = []
for i in range(len(x)):
    x_mod.append(x[i].split(' '))
y=[]
def damper2(report2, problem):
    succ = True
    report = report2[1:]
    i=0
    while i < len(report)-1:
        if i == 0:
            if report[i+1] > report[i+2]: increase = False
            else: increase = True
        if report[i] < report[i+1] and not increase: succ = False
        if report[i] > report[i+1] and increase: succ = False
        if abs(report[i]-report[i+1]) > 3 or abs(report[i]-report[i+1]) < 1: succ = False
        i+=1 
    if succ == True: return True
    else: 
        i=0
        succ = True
        report = report2[:problem] + report2[problem+1:]
        while i < len(report)-1:
            if i == 0:
                if report[i] > report[i+1]: increase = False
                else: increase = True
            if report[i] < report[i+1] and not increase: succ = False
            if report[i] > report[i+1] and increase: succ = False
            if abs(report[i]-report[i+1]) > 3 or abs(report[i]-report[i+1]) < 1: succ = False
            i+=1
    return succ 
   
def safety(report):
    damper = False
    i=0
    while i < len(report)-1:
        if i == 0:
            if report[i] > report[i+1]: increase = False
            else: increase = True
        if report[i] < report[i+1] and not increase: damper = True
        if report[i] > report[i+1] and increase: damper = True
        if abs(report[i]-report[i+1]) > 3 or abs(report[i]-report[i+1]) < 1: damper = True
        if damper == True:
            return damper2(report, i)
        i+=1
    if damper == False: return True



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
        
