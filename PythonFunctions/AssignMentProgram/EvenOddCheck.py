
def EvenCheck(number):
       if number%2 == 0  :return True
       else:  return False



print("Enter a Number :")
number = int(input())
result = EvenCheck(number)
if result is True : print(" Even Number ")
else: print(" Odd Number")