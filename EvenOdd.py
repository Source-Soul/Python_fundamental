def is_even(numbers):
    if numbers%2 == 0:
        return True
    else:
         return False


starting = 0
while starting < 100:
     if is_even(starting):
         print(f"{starting} is even")
     else:
         print(f"{starting} is odd")

     starting = starting+1