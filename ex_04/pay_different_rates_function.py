#Calculating different rates with function
def computepay (h,r):
    payreg=h*r
    pay40=40.0*r
    payplus=pay40+(h-40.0)*1.5*r
    pay=0
    if float(h)<=40.00:
        pay=payreg
    else:
        pay=payplus
    print("Pay", pay)
    return pay
#
hours=input('Enter hours: ')
rate=input('Enter rate: ')
fh=float(hours)
fr=float(rate)
#
computepay(fh, fr)
