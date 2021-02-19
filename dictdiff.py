
def dictdiff(a, b):
    """returns the difference between a and b dictionaries """
    # new dict to add data
    c ={}
    # make a set with unique keys
    for k in set([*a.keys(),*b.keys()]):
        # if both items are same, pass
        if a.get(k,None) == b.get(k,None):
            continue
        # else add to new dictionary
        else:
            c[k] = [a.get(k,None), b.get(k,None)]
    return c
            
    
if __name__ =="__main__":
    a = {"a":1, "b":2, "c":3}
    b = {"a":1, "b":3, "c":5, "d":4}
    print(dictdiff(a,b))
