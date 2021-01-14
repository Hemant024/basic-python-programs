def mysplit(string, delimiters=' \t\n'):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))




# def mysplit(strng):
#     list1=[]
#     tmp=""
#     for i in strng:
#         if i==" ":
#             list1.append(tmp)
#             tmp=""
#         else:
#             tmp=tmp+i
#     if tmp:
#         list1.append(tmp)
#     return list1
# print(mysplit("hgbvgfzxdfsfgv dgr "))