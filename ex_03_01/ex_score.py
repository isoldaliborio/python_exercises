import sys
# grade to score between 0.0 e 1.0
score = input("Enter Score: ")
try:
    fs=float(score)
    fs>=0.0 and fs<=1.0
except:
      print('Erro: please input a number between 0 and 1')
      sys.exit()
if fs>=0.9 and fs<=1.0:
    print('A')
elif fs>=0.8 and fs<0.9:
    print('B')
elif fs>=0.7 and fs<0.8:
    print('C')
elif fs>=0.6 and fs<0.7:
    print('D')
elif fs>=0.0 and fs<0.6:
    print('F')
else:
    print('Erro: please input a number between 0 and 1')
