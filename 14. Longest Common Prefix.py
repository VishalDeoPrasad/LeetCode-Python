def commonStr(str):
    if len(str) == 0: return "" 
    min_str = min([len(s)] for s in str)[0]
    common_str = ""
    for i in range(min_str):
        temp = str[0][i]
        for j in range(1, len(str)):
            if str[j][i] != temp:
                return common_str
           
        common_str += temp
    return common_str

str = ["flower","flow","flight"]
print(commonStr(str))