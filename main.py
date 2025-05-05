# extracting data from the files
message = ""
with open("message1.txt", encoding="utf-8") as mesFile:  # encoding ensures we read the file with standard bytes ascii uses
    message = mesFile.readline()  # our file is only one line so our message is just that line

keys = []
with open("keys.txt") as keyFile:
    for line in keyFile:
        keys.append(line.strip())  # adding each line of the key file as a string element to the list of keys

def getKey(key):  # key will be an indexed version of keys (like keys[0])
    shift = []
    for ch in key:  # for each character in this one word string
        shift.append(ord(ch) - ord('A'))  # the shift is the ascii order of the number minus the capital since all keys are capslock
    return shift

def cypher(message, key, decrypt=True):
    decryptMessage = ""  # final decrypted message
    idx = 0  # initialising our index position in the message
    key = getKey(key)  # the key we're using put into its shifts 

    if decrypt:
        key = [-1*x for x in key]  # when descrypting we want to shift it back so we want negative shifts so just each num * -1

    for ch in message:
        if ch.isalpha():  # if we have a letter we want to decrypt it
            if ch.islower():  # checking the starting point of the alphabet for lower vs capital
                caseShift = ord('a')
            else:
                caseShift = ord('A')

            shift = key[idx % len(key)]  # so the actual key that applies just depends on how many letters we've gone over in the message so far
            ch = chr(((ord(ch) - caseShift + shift) % 26) + caseShift)  # converting character in message with shift 
            decryptMessage += ch  # constructing our new message
            idx = idx + 1  # whenever  we have a letter we want to make sure we're moving our index point by one
    
        else:  # if we don't have a letter we leave it as is
            decryptMessage += ch

    return decryptMessage

help = "PLEASE"
print(cypher("ewiaki rlpl ei pxidws x'x wo vsly fav jdc com mi'd rol ikpr fmrcj", help))

# ask to print 0 then 3