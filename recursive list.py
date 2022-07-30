



l = [2,3,6,7,9,9,2,1,6]

def listro(l):
    if len(l) == 0:
        return[]
    else:
        return[l.pop()]+ listro(l)

print (listro(l))
