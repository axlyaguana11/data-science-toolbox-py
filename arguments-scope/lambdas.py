#Here you'll see how to use lambdas 

lambda a, b: a * b #Syntax: lambda args: expression

#Lambdas come in handy while using functions into another function 

def powered(n):
  return lambda a:  a ** n


cube = powered(3)
print(cube(2))