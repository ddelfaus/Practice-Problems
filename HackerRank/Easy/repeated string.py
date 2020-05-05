#plan 
#repeat the characters n times
#add the a's to a list
#do arr len  to get the # of a's


def repeatedString(s, n):
    #too slow
    # string_list = s * n
    # list_of_letters = []
    # count = 0
        
    # for letter in string_list:
    #     count += 1
    #     if count == n:
    #         if letter == "a":
    #             list_of_letters.append(letter)
    #             return len(list_of_letters)
            
    #         else:
    #             return len(list_of_letters)

    #     elif letter == "a":
    #         list_of_letters.append(letter)


    # print(string_list)
    # print(list_of_letters)

    #in class fast solultion
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



print(repeatedString('aba', 1000000000))

