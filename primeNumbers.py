x = 100
for x in range(2,x+1):
	if x > 1:
		for y in range(2,x):
			if (x%y)==0:
				break
			else:
				print(x)
