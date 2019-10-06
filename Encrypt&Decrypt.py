#Cyber security 

import random
#Generates random key using alphabet list
def randomKey(characterSets):
	#Converts String into list
	characterSets = list(characterSets)
	#Uses list built-in function shuffle
	random.shuffle(characterSets)
	#Convert list back into String using .join function
	return ''.join(characterSets)

#Encrypt using Substitution Cipher
def encrypt(plaintext, key, characterSets):
	#Create a list using list comprehension
	#for each character in plaintext
	#Convert the character to lower cases
	#Return the index position of that character from the characterSets list
    keyIndices = [characterSets.index(k.lower()) for k in plaintext]
    #Using the index position in characterSet
    #Find the new encrypted index position in key
    #Convert list back into String using .join function
    return ''.join(key[keyIndex] for keyIndex in keyIndices)
    
#Decrypt using Substitution Cipher
def decrypt(cipher, key, characterSets):
	#Create a list using list comprehension
	#for each character in cipher text
	#Return the index position of that character from the key list
    keyIndices = [key.index(k) for k in cipher]
    #Using the index position in key
    #Find the decrypted index position in characterSets
    #Convert list back into String using .join function
    return ''.join(characterSets[keyIndex] for keyIndex in keyIndices)

#List of digits, alphabet and wildcard characters I will be using
characterSets = 'abcdefghijklmnopqrstuvwxyz.,! @#$%^&*()_-+=1234567890/|`~'
#Key scrambled the order of the list of available alphabets
#Must be same length as list of alphabets
key = '^lfvyc3th|!+qs/0u&dg`*,7mn61r98 5w.#=a@z(-opje)bk2x%~_i$4'
#Text to be encrypted
#Get from user
#plaintext = "Ishtar, Ereshkigal and Yu Miaoyi are Bae!"
options = input("Choose from the following:\n1.Encrypt\n2.Decrypt\n")
if(options == "1"):
	#Ask user input
	plaintext = input("Enter text to be encrypted.\n")
	#Call encrypt function
	cipher = encrypt(plaintext, key, characterSets)
	#Print encrypted text
	print(cipher)
elif(options == "2"):
	#Ask user input
	cipher = input("Enter text to be decrypted.\n")
	#Call decrypt function
	plaintext = decrypt(cipher, key, characterSets)
	#Print decrypted text
	print(plaintext)
else:
	#All other options are invalid
	print("Invalid Input")
