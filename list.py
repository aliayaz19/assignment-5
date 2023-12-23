
my_lst = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 7]


unique_lst = []
for item in my_lst:
    if item not in unique_lst:
        unique_lst.append(item)


print("Original List:", my_lst)
print("List without Duplicates:", unique_lst)
