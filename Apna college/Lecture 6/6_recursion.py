# def show(n):
#     print(n)
# show(5)         # 5, but we want to print 5,4,3,2,1   So we will use recursion

def show(n):      # is function ka naam hai show aur isi function ke andr ye dobara se show ko call krra hai
    if(n == 0):   # but it needs a condition where it is to be stopped/called else recursion error..........
        return
    print(n)
    show(n-1)
    # show(n+1)
show(5)

print()

def show(n):      
    if(n == 0):  
        return
    print(n)
    show(n-1)
    print("END")  # jb 0 layer tak ka sara recursion complete ho jaayega tab ye print hoga jitne bhi layers hai utne hi baar ye print hoga.
show(5)

print()


# returns n!                      Recursive code for factorial
def fact(q):
    if(q == 0 or q == 1):       # Base case: 0! = 1 and 1! = 1
        return 1
    else:                       # n! = n * (n-1)!  # Recurrence relation
        return q * fact(q - 1)  # Recurrence relation
print(fact(5))


