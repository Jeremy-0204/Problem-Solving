import os
 
path_dir = 'C:/Users/parkk/Desktop/새 폴더/PPS CAMP/4주차/박경륜_20230118'
 
file_list = os.listdir(path_dir)

l = list(map(lambda x: x.split('_')[0],file_list))
k = []
for name in l:
    if name!= 'fillename.py':
        k.append(name)
# print(k)
for i in range(len(k)):
    for j in range(i+1,len(k)):
        if(k[i]>k[j]):
            temp = k[i]
            k[i] = k[j]
            k[j] = temp
            
print(len(k))
print(",".join(k))