import datetime
a = datetime.datetime.now()
i=0
while(i<1000000):
	i = i+1

b = datetime.datetime.now()
print(b-a)

