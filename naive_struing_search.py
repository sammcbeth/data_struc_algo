def naive_string(str1, str2):
    count = 0
    index = 0
    while index < len(str2):
        if str2[index] == str1[0]:
            index_sub = 0
            while index_sub < len(str1):
                if str1[index_sub] != str2[index]:
                    break
                index += 1
                index_sub += 1
                if index_sub == len(str1):
                    count += 1
        index += 1
    return count

print(naive_string('omg','omfgdfknomgfgosdfofmg'))
