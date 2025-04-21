import math
t=int(input())
limits=[input().split(' ') for i in range(t)]
for lim in  limits:
	upper=math.floor(math.sqrt(int(lim[1])))
	lower=math.ceil(math.sqrt(int(lim[0])))
	res=upper-lower+1
	print(res)