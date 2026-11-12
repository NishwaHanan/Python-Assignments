
# TO CHECK UNIQUE CHARACTERS OF STRING
a=input("enter a string =")
def has_unique_chars(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                return False
    return True
print(has_unique_chars(a))