#COS792 Assignment 1
#Task 1
#References: https://www.geeksforgeeks.org/columnar-transposition-cipher/
#
#Ask user for options to encrypt or decrypt
#	Uses a random generated key for Substitution cipher
#	Ask user for key used in Transpositional cipher
#	Based on the Substituted cipher
#	Futher encrypt message using Transpositional cipher with key
#
#	Ask user for encrypted message and key used in Transpositional cipher
#	First reverse the Transpositional cipher using key
#	Then use the decrypted message and futher decrypt
#	Using Substitution cipher

import math
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
def encryptSubs(key,msg,characterSets):
	#Create a list using list comprehension
	#for each character in message
	#Convert the character to lower cases
	#Return the index position of that character from the characterSets list
    keyIndices = [characterSets.index(k.lower()) for k in msg]
    #Using the index position in characterSet
    #Find the new encrypted index position in key
    #Convert list back into String using .join function
    return ''.join(key[keyIndex] for keyIndex in keyIndices)
    
#Decrypt using Substitution Cipher
def decryptSubs(key,msg,characterSets):
	#Create a list using list comprehension
	#for each character in cipher text
	#Return the index position of that character from the key list
    keyIndices = [key.index(k) for k in msg]
    #Using the index position in key
    #Find the decrypted index position in characterSets
    #Convert list back into String using .join function
    return ''.join(characterSets[keyIndex] for keyIndex in keyIndices)

#Encrypt using Transpositional Cipher
def encryptTrans(key,msg): 
	#Create cipher variable
    cipher = "" 
    #K index use for tracking 
    k_indx = 0
    #Msg variable data
    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    #Convert key into list and use built in function to sort list
    key_lst = sorted(list(key)) 
  	#Length of col equals length of the key
    col = len(key) 
    #Use ceiling function to ensure enough rows
    #Message length divided key length to find how much rows
    row = int(math.ceil(msg_len / col))
    #Fill empty gaps with padding space
    #Or none alphabetically character, wild cards etc
    #"_"
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
    #Create matrix or 2D array  
    #Fill the message in the corresponding columns
    #From 0 to the last element of message
    #We jump every column
    #Assign that element into the index position + col no.
    matrix = [msg_lst[i: i + col]for i in range(0, len(msg_lst), col)] 
	#For each column 
    for _ in range(col): 
    	#Current get the element at k_index from each colunn
    	#Because we increment row column each iteration
        curr_idx = key.index(key_lst[k_indx]) 
        #Use list comprehension to join each row into String
        cipher += ''.join([row[curr_idx] for row in matrix]) 
        k_indx += 1
  
    return cipher 

def decryptTrans(key,cipher):
	#Create msg variable
    msg = "" 
    #K index use for tracking 
    k_indx = 0
	#Cipher text variable data
    msg_indx = 0
    msg_len = float(len(cipher)) 
    #Convert msg into list
    msg_lst = list(cipher) 
	#Length of col equals length of the key
    col = len(key) 
    #Use ceiling function to ensure enough rows
    #Cipher length divided key length to find how much rows
    row = int(math.ceil(msg_len / col)) 
    #Convert key into list and use built in functions to sort
    key_lst = sorted(list(key)) 
    #Create matrix
    dec_cipher = [] 
    for _ in range(row):
    	#Create row and add to matrix
        dec_cipher += [[None] * col] 
  
    #Arrange the matrix in column wise
	#For each column
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  		#For each row
        for j in range(row): 
        	#We add the message into the matrix
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            #Increment index use in row
            msg_indx += 1
           #Increment index to keep track of column
        k_indx += 1
  
    #Use list comprehension to join each row into String
    msg = ''.join(sum(dec_cipher, []))
    #Check if theres empty paddings 
    #Used as spaces or wild cards etc
    null_count = msg.count('_') 
  	#If theres empty padding
    if null_count > 0: 
    	#Remove the amount of empty paddings from the back of the original message
        return msg[: -null_count] 
    return msg 

#List of digits, alphabet and wildcard characters I will be using
characterSets = 'abcdefghijklmnopqrstuvwxyz.,! @#$%^&*()_-+=1234567890/|`~'
#Key scrambled the order of the list of available alphabets
#Must be same length as list of alphabets
#You maybe use randomKey to generate new key
key = '^lfvyc3th|!+qs/0u&dg`*,7mn61r98 5w.#=a@z(-opje)bk2x%~_i$4'
#Sample
#plaintext = "Ishtar, Ereshkigal and Yu Miaoyi are Bae!"
options = input("Choose from the following:\n1.Encrypt\n2.Decrypt\n")
if(options == "1"):
	#Ask user input
	plaintext = input("Enter text to be encrypted.\n")
	#Call dencrypt function for substitution cipher
	cipher = encryptSubs(key, plaintext, characterSets)
	#Ask for key
	keyTrans = input("Enter key used in transposition.\n")
	#Call encrypt function for transposition cipher
	cipher = encryptTrans(keyTrans,cipher)
	#Print encrypted text
	print(cipher)
elif(options == "2"):
	#Ask user input
	cipher = input("Enter text to be decrypted.\n")
	#Call decrypt function for substitution cipher
	msg = decryptSubs(key, cipher, characterSets)
	#Ask for key
	keyTrans = input("Enter key used in transposition.\n")
	#Call decrypt function for transposition cipher
	msg = decryptTrans(keyTrans,msg)
	#Print decrypted text
	print(msg)
else:
	#All other options are invalid
	print("Invalid Input")
