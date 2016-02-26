import stats

def choose(n,k):
	if  k > n: 
		return False
	if k is 0:
		return 1
	if k > (n/2.0):
		return choose(n,(n-k))
	return n * choose(n-1,k-1) / float(k)


def drawExact(x, ice, nonIce, hand):

	return(choose(ice,x)*choose(nonIce,hand-x)/float(choose(ice+nonIce,hand)))


def orMore(x, ice, nonIce, hand):

	hand = 5

	if x > hand:
		return 0

	val = drawExact(x, ice, nonIce, hand) + orMore(x+1, ice, nonIce, hand)

	return val

def orMoreMullian(x, ice, nonIce, hand):

	return orMore(x, ice, nonIce, hand) + (1-orMore(x, ice, nonIce, hand)) * orMore(x, ice, nonIce, hand)


print "21 Ice - 2 orMore"

print orMoreMullian(2, 21, 28, 5)

print "21 Ice - 3 orMore"

print orMoreMullian(3, 21, 28, 5)

lis = []

dif = []

for i in range(50):

	lis.append(orMoreMullian(3, i, 49 - i, 5))

	if i > 0:
		dif.append(lis[i] - lis[i-1])

print lis[20:29]

print dif[20:29]

print stats.standDev(lis[20:29])