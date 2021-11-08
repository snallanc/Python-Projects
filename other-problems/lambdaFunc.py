"""
lambda keyword is used to define/return small anonymous functions.
lambda expressions are meant to have just one expression per definition.
"""

def power(x):
    return lambda y: x ** y

p=power(10)

print("Powers of 10:\n")
for i in range(1,10):
  print(p(i))
