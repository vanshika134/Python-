i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

i5 = (1,4,9,16,25,36,49,64,81,100)
X = 36
i = 0    #initialization
while i < len(i5):
    if(i5[i] == X):
        print("Found at index ", i)
        break
    else:
        print("finding...")
    i+=1
print("----End of loop----")                           

j = 0
while j <= 5:
    if(j == 3):
        j += 1
        continue
    print(j)
    j += 1

print("-----Another loop-----")

k = 1
while k <= 10:
    if(k%2 == 0):
        k += 1
        continue
    print(k)
    k += 1



    