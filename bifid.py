import random
#This is a scam but I cant find a way to code real TRNG
#It still follows the principals of  polybius cipher
#I choose the 8-9 position of the randomized alphabet list to loop over
#Its like I and J in the slides of from the algorithm 
#I will be using a 5x5 2D array, but more simply using a 1D array and treating it as 2D
#
#References: https://www.wikihow.com/Use-a-Polybius-Square
#References: https://www.geeksforgeeks.org/polybius-square-cipher/

#Generates a string of randomized alphabets from a to z
def genRanAlpha(alphabets):
	#converts list of alphabets from string to list
	alphaList = list(alphabets)
	#Use build in function for list to shuffle alphabet list
	random.shuffle(alphaList)
	#Convert list back to string using .join
	return ''.join(alphaList)

#Base on the randomized alphabets
#Reorder it from 0-25 as its index positions
def createTable(alphabets,ranAlphabets):
	#Create list
	ranAlphaSize = [(i+1) for i in range(len(ranAlphabets))]
	#Return the list with index positions
	return ranAlphaSize

def polybiusCipher(alphabets,ranAlphabets,ranAlphaSize,msg): 
	#For each character in message
	for char in msg:
		#If the character exist in the alphabet from a to z
		#All others are discard such as white space wildcard etc
		if char in ranAlphabets:
			#Finding index position in random Alphabet list
			#Then dividng by 5 to get row
			row = int((ranAlphaSize[ranAlphabets.index(char)] - ranAlphaSize[0]) / 5) + 1
			#Finding index position in random Alphabet list
			#Then dividng by 5 to get column
			col = ((ranAlphaSize[ranAlphabets.index(char)] - ranAlphaSize[0]) % 5) + 1
			#If character is the 11th character in the list
			if char == ranAlphabets[10]:
				#Move one row up
				row = row - 1
				#Move one right
				#5- to perform the wrap around
				col = 5 - col + 1
			#If character is greater than the 11th character in the list 
			elif ranAlphaSize[ranAlphabets.index(char)] >= ranAlphaSize[9]: 
				#If the column count for that character is the 2nd column or 1
				if col == 1:
					#Push it to the end
					col = 6
					#Move it 1 up
					row = row - 1
				#Reduce 1 till the end of the 2D array or array
				col = col - 1                          
			print(row, col, end =' ', sep ='') 

#Create normal alphabet list ranging from a to z
alphabets = "abcdefghijklmnopqrstuvwxyz"
#Shuffles the alphabet list
ranAlphabets = genRanAlpha(alphabets)
#Creates new ranking size for random Alphabets
ranAlphaSize = createTable(alphabets,ranAlphabets)
#Test sample
#plaintext = "Ishtar Ereshkigal and Yu Miaoyi are Bae!"
#Ask user input
plaintext = input("Enter text to be encrypted.\n")
#This cipher only checks if its lower case
#So I converted it to lower because passing to the function
polybiusCipher(alphabets,ranAlphabets,ranAlphaSize,plaintext.lower())
