def Compound_Interest (p,r,t):
    ci=(p*(1+(r/100))**t)
    return ci
p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("enter the number of years"))
ci=Compound_Interest(p,r,t)
print("compound intest :{}".format(ci,'.2f'))

