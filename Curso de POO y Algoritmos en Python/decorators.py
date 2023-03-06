# Decorators = Functions that take other function as a parameter to modify or add a property to existent functions
# Without having to make changes in their original body

# Decorator to handle the ZeroDivisionError

def Div_by_zero(func):
  def inner(a,b):
    if b == 0:
      return "Error: Dividing by Zero is not allowed"
    return func(a, b)
  return inner

# @ is a decorator that adds the property defined by that decorator to the function that has it on top

@Div_by_zero
def Unitprice (Amount,Quantity):
  return Amount / Quantity

if __name__ == '__main__':
  print (Unitprice(500,0))
