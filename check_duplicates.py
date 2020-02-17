str_1 = "abcabcdefsadsdferffdg"
i = 0
new_dict = {}
while i < len(str_1):
    if str_1[i] in new_dict.keys():
        new_dict[str_1[i]] += 1
    else:
        new_dict[str_1[i]] = 1
    i += 1

print(new_dict)
uniq_list = [key for key in new_dict.keys() if new_dict[key] == 1 ]
print(*uniq_list)