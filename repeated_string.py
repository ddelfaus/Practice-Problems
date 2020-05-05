def repeatedString(s,  n):
	num_as = count_as(s, len(s))
	multiples = n // len(s)
	remainder = n % len(s)
	
	if remainder > 0:
		return num_as * multiples + count_as(s, remainder)
	else:
		return num_as * multiples
	
def count_as(s, remainder):
	counter = 0
	slice = s[:remainder]
	
	for sl in slice:
		if sl == 'a':
			counter += 1
		
	return counter



print(repeatedString('aba', 10))