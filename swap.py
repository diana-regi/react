l = [12, 18, 7, 4, 27, 23]
print(l)
n = len(l)

#Swapping
temp = l[0]
l[0] = l[n - 1]
l[n - 1] = temp

print("Swapped list: ",l)