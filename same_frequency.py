def same_frequency(num1, num2):
    dict_num_1 = {}
    dict_num_2 = {}
    num1 = str(num1)
    num2 = str(num2)
    for char in num1:
        try:
            if dict_num_1[char]:
                dict_num_1[char] += 1
        except:
            dict_num_1[char] = 1
    for char in num2:
        try:
            if dict_num_2[char]:
                dict_num_2[char] += 1
        except:
            dict_num_2[char] = 1
    if len(dict_num_1) != len(dict_num_2):
        return False
    for key in dict_num_1.keys():
        try:
            if dict_num_1[key] != dict_num_2[key]:
                return False
        except:
            return False
    return True


print(same_frequency(1222, 2221))
