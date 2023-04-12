# string = ""
# while True:
#     string = input()
#     slist = []

#     if string == ".": break

#     for sentence in string:
#         for i in sentence:
#             if i == "(" or i == "[": slist.append(i)
#             elif len(slist) != 0 and i == ")" and slist[-1] != "(": slist.append(i)
#             elif len(slist) != 0 and i == "]" and slist[-1] != "[": slist.append(i)
#             elif len(slist) != 0 and i == ")" and slist[-1] == "(": slist.pop()
#             elif len(slist) != 0 and i == "]" and slist[-1] == "[": slist.pop()
#     if len(slist) == 0: print("yes")
#     else: print("no")

string=input()
while(string != '.'):
    lst = []

    for i in string:
        if i =='(' or i =='[':
            lst.append(i)
        elif i==')':
            if '(' not in lst:
                lst.append(i)
                break
            elif lst[-1] !='(':
                break
            else:
                lst.pop()
        elif i==']':
            if '[' not in lst:
                lst.append(i)
                break
            elif lst[-1] != '[':
                break
            else:
                lst.pop()


    print('yes' if len(lst) == 0 else 'no')
    string = input()