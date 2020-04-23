def multiple_letter_count(a):
    b = {a[i]:a.count(a[i]) for i in range(0,len(a))}
    return b
    # return b


j = input(" Enter the string : ")
print(multiple_letter_count(j))
