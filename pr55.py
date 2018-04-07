from string import ascii_lowercase as asc_lower
def checks(s):
  return set (asc_lower)-set(s.lower())==set([])
str1=input("enter string:")
if(check(str)==true):
  print("the string is a program")
else:
  print("the string isn't a pangram")
