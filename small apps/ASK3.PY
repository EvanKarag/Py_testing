
a =[]
def AMfunc(list,a):
    last_digit = len(a)
    if a.index(0) != a.index(last_digit):
        return 0;
    else:
        return 1;

A = 1048315
AMfunc(A)