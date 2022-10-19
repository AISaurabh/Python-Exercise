#Example No. 6
import sys
class BaseError(Exception):
  pass  
class HighValueError(BaseError):
  pass  
class LowValueError(BaseError):
  pass 
x = 20
while True:
  try:
    a= int(input("Enter the number : "))
    if a > x:
      raise HighValueError
    elif a < x:
      raise LowValueError
    break
  except LowValueError:
    print("you give Very low number, give input again ")
    print()
  except HighValueError:
    print("you give Too high number, give input again ")
    print()
print("That's the Correct answer.")
