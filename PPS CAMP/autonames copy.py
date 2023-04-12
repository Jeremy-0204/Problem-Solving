k = "A007, A008, A017, A018, A020, A029, A030, A032, A035, A045, A046, A047, A053, A070, A082, A104, A106, A107, A108, A111, A112, A124, A125, A126, A127, A128, A129, A131, A139, B065, B075"
k = list(k.split(","))
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if(k[i]>k[j]):
            temp = k[i]
            k[i] = k[j]
            k[j] = temp
            
print(len(k))
print(",".join(k))