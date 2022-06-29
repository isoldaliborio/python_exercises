#Calculating different rates
hours=input('Enter hours: ')
rate=input('Enter rate: ')
fh=float(hours)
fr=float(rate)
#
pay=fh*fr
pay40=40.0*fr
payplus=pay40+(fh-40.0)*1.5*fr
if float(hours)<=40.00:
    print(pay)
else:
    print(payplus)
