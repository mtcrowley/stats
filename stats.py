import math



def feqToLis(feq):
    temp = []
    for n in feq:
        for m in range(n[0]):
            temp.append(n[1])
    return temp


def mean(lis):
    return float(sum(lis))/float(len(lis))

def median(lis):

    if len(lis) % 2 is 1:

        i = int(math.floor(len(lis)/2))

        return lis[i]

    else:

        i = [int(len(lis)/2)-1, int(len(lis)/2)]

        return mean([lis[i[0]],lis[i[1]]])

def quartiles(lis):

    if len(lis) % 2 is 1:

        i = int(math.floor(len(lis)/2))

        Q1 = median(lis[0:i+1])

        Q2 = lis[i]

        Q3 = median(lis[i:len(lis)])

    else:

        i = [int(len(lis)/2)-1, int(len(lis)/2)]

        Q1 = median(lis[0:i[1]])

        Q2 = mean([lis[i[0]],lis[i[1]]])

        Q3 = median(lis[i[1]:len(lis)])

    return[Q1, Q2, Q3]


def mode(lis):

    table = []

    for n in lis:
        n = int(n*10)
        while len(table) <= n:
            table.append(0)
        table[n] = table[n] + 1
    
    m = max(table)

    if m is 1:
        print None
    else:
        for n in range(0,len(table)):
            if int(m) is table[n]:
                print float(n)/10

def trim(percent, lis):

    n = int(len(lis) * percent)

    return mean(lis[(0+n):(len(lis)-n)])

def standDev(lis):

    xbar = mean(lis)

    n = len(lis)

    summation = 0

    for x in lis:
        temp = math.pow(x - xbar, 2)
        summation = summation + temp

    return math.sqrt(summation/(n - 1))

def compDev(lis):
    n = len(lis)

    sum1 = 0

    for x in lis:
        temp = math.pow(x, 2)
        sum1 = sum1 + temp

    sum2 = 0

    for x in lis:
        temp = x
        sum2 = sum2 + temp

    return math.sqrt((sum1 - (math.pow(sum2,2)/n))/(n - 1))

def spread(lis):
    return max(lis) - min(lis)

#   Print   # 
def myPrint(lis):
    print "count: \t %f" %float(len(lis))

    print "sum: \t %f" % float(sum(lis))

    print "mean: \t %f" % mean(lis)

    print ".05 trim:%f" % trim(.05, lis)

    print ".1 trim: %f" % trim(.10, lis)

    print "standDev:%f" % standDev(lis)

    print "compDev: %f" % compDev(lis)

    print "range: \t %f" % spread(lis) 

    print "quartiles:"
    print quartiles(lis)

    print "IQR: \t %f" % spread(quartiles(lis))

    print "min: \t %f" % float(min(lis))

    print "max: \t %f" % float(max(lis))

    print "mode:\t" 
    mode(lis)

    print lis

def b0(x,y,slope):
    return mean(y) - (slope * mean(x))

def b1(x,y):

    def pSum(x,y):
        s = 0
        for n in range(len(x)):
            s = s + x[n]*y[n]
        return s

    def S(x,y):
        return float(pSum(x,y)) - (float(sum(x)*sum(y))/float(len(x))) 

    return float(S(x,y))/float(S(x,x))

def SST(y):
    av = mean(y)
    s = 0
    for n in range(len(y)):
        s = s + math.pow(y[n] - av, 2)
    return s

def SSR(x,y):
    average = mean(y)
    slope = b1(x,y)
    intercept = b0(x,y,slope)
    s = 0
    for n in range(len(y)):
        s = s + math.pow((slope*x[n] + intercept) - average, 2)
    return s
