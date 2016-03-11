def getHammingDistance(str1, str2):
   	distance = 0

	if len(str1) == len(str2):					
		for indx in range(len(str1)):				#until how long first string is
			if ord(str1[indx]) != ord(str2[indx]):	#compares ascii value of each letter
 				distance = distance + 1			#increments hamming distance
		return distance
	else:
		return None

def countSubstrPattern(str1, str2):
	cnt = 0
	indx = 0

	if len(str2) < len(str1):								#won't be a substring if greater
		while indx < len(str1):								
			if str1.find(str2, indx, indx + len(str2)) != -1:		#checks per character if equal 
				cnt = cnt + 1
			indx = indx + 1
		return cnt
	else :
		return None

def isValidString(str1, str2):
	check = 0

	for indx1 in range(len(str1)):				
		ch = str1[indx1]							#saves first string
		for indx2 in range(len(str2)):
			if ord(str1[indx1]) == ord(str2[indx2]):	#checks per letter if same
				check = check + 1
	if check == len(str1):							#if every letter of first word is same
		return True
	else :
		return False

def getSkew(str1,n):
	indx = 0
	g = 0
	c = 0

	while indx < n:						
		if ord(str1[indx]) == ord('G'):		#counts number of g's and c's
			g = g + 1
		if ord(str1[indx]) == ord('C'):
			c = c + 1
		indx = indx + 1

	return g-c

def getMaxSkew(str1,n):
	max = getSkew(str1, n)					#gets the skew of string as maximum value

	if n > 0:
		for indx in range(n):
			if max < getSkew(str1,n-index):	#gets every skew and changes if there is a greater value
				max = getSkew(str1,n-index)
	return max

def getMinSkew(str1,n):
	min = getSkew(str1,n)					#gets the skew of string as minimum value

	if n > 0:
		for indx in range(n):
			if min > getSkew(str1,n-index):	#gets every skew and changes if there is a greater value
				min = getSkew(str1,n-index)
	return min

def printMenu():							#prints menu
	print "********MENU************"
	print "[1] Get Hamming Distance"
	print "[2] Count Substring Pattern"
	print "[3] Check String Validity"
	print "[4] Get Skew"
	print "[5] Get Max Skew"
	print "[6] Get Min Skew"
	print "[7] Exit"

	return input("CHOICE: ")


#MAIN FUNCTION
ch = 0
n = 0
while ch != 7:
    ch = printMenu()
    if ch == 1:
        str1 = raw_input("Str 1: ")
        str2 = raw_input("Str 2: ")
        ans = getHammingDistance(str1,str2)
        if ans != None:
            print "\n\nHamming Distance: %d\n\n" % ans
        else :
            print "\nInvalid! (String lengths mismatch)\n"
    elif ch == 2:
        str1 = raw_input("String: ")
        str2 = raw_input("Substring: ")
        ans = countSubstrPattern(str1,str2)
        if ans != None:
            print "\n\nSubstrings: %d\n\n" % ans
        else :
            print "\n\nInvalid! (Longer substring)\n\n"
    elif ch == 3:
        str1 = raw_input("Str 1: ")
        str2 = raw_input("Str 2: ")
        ans = isValidString(str1, str2)
        if ans == True:
            print "VALID"
        else:
            print "Invalid! (String 2 not in string 1)"
    elif ch == 4:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Starting at 1!"
            if n > len(str1):
                print "Invalid! (larger index than the length of string)"
        ans = getSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
    elif ch == 5:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Starting at 1!"
            if n > len(str1):
                print "Invalid! (larger index than the length of string)"
        ans = getMaxSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
    elif ch == 6:
        str1 = raw_input("String: ")
        while n <= 0 or n > len(str1):
            n = int(raw_input("Starting index: "))
            if n <= 0:
                print "Starting at 1!"
            if n > len(str1):
                print "Invalid! (larger index than the length of string)"
        ans = getMinSkew(str1,n)
        n = 0
        print "\n\nSkew: %d\n\n" % ans
