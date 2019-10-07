#Cyber security 
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
    #
    k_indx = 0

    msg_len = float(len(msg)) 
    msg_lst = list(msg) 
    key_lst = sorted(list(key)) 
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # add the padding character '_' in empty 
    # the empty cell of the matix  
    fill_null = int((row * col) - msg_len) 
    msg_lst.extend('_' * fill_null) 
  
    # create Matrix and insert message and  
    # padding characters row-wise  
    matrix = [msg_lst[i: i + col]for i in range(0, len(msg_lst), col)] 
  
    # read matrix column-wise using key 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
        cipher += ''.join([row[curr_idx] for row in matrix]) 
        k_indx += 1
  
    return cipher 

def decryptTrans(key,cipher): 
    msg = "" 
  
    # track key indices 
    k_indx = 0
  
    # track msg indices 
    msg_indx = 0
    msg_len = float(len(cipher)) 
    msg_lst = list(cipher) 
  
    # calculate column of the matrix 
    col = len(key) 
      
    # calculate maximum row of the matrix 
    row = int(math.ceil(msg_len / col)) 
  
    # convert key into list and sort  
    # alphabetically so we can access  
    # each character by its alphabetical position. 
    key_lst = sorted(list(key)) 
  
    # create an empty matrix to  
    # store deciphered message 
    dec_cipher = [] 
    for _ in range(row): 
        dec_cipher += [[None] * col] 
  
    # Arrange the matrix column wise according  
    # to permutation order by adding into new matrix 
    for _ in range(col): 
        curr_idx = key.index(key_lst[k_indx]) 
  
        for j in range(row): 
            dec_cipher[j][curr_idx] = msg_lst[msg_indx] 
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string 
    msg = ''.join(sum(dec_cipher, [])) 
    null_count = msg.count('_') 
  
    if null_count > 0: 
        return msg[: -null_count] 
  
    return msg 

#List of digits, alphabet and wildcard characters I will be using
characterSets = 'abcdefghijklmnopqrstuvwxyz.,! @#$%^&*()_-+=1234567890/|`~'
#Key scrambled the order of the list of available alphabets
#Must be same length as list of alphabets
#You maybe use randomKey to generate new key
key = '^lfvyc3th|!+qs/0u&dg`*,7mn61r98 5w.#=a@z(-opje)bk2x%~_i$4'
#Text to be encrypted
#Get from user
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
