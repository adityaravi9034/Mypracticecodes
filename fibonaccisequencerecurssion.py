def recurssion_feb(n):
    if n <= 1:
        return n
    else:
        return(recurssion_feb(n-1) + recurssion_feb(n-2) )

nterms = 10

if nterms <= 0:
    print("please enter a positive number")
else:
    print("fibonacci sequence:")
    for a in range(nterms):
        print(recurssion_feb(a))
