
n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

def add(n1,n2):
   return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def div_integer(n1,n2):
    return n1//n2

a = add(n1,n2)
b = subtract(n1,n2)
c = multiply(n1,n2)
d = divide(n1,n2)
e = div_integer(n1,n2)

print(a)
print(b)
print(c)
print(d)
print(e)