croAlphabetCount = 0
identifierList = ["c=","c-","dz=","d-","lj","nj","s=","z="]
string = input()
for i in range(8):
    croAlphabetCount += string.count(identifierList[i])
    string = string.replace(identifierList[i],' ')
    #print(string, croAlphabetCount)
string = string.replace(' ', '')
croAlphabetCount += len(string)
print(croAlphabetCount)