#Reversing a string

def rev(str):
  if type(str)!=type('abc') or len(str)==0:
    print('Invalid Input')
  else:
    strrev = str[::-1]
    print(strrev)
  return 

rev('ahmedabad mechanical engineering') 