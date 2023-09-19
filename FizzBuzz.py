# Simple FizzBuzz script
# Setting up the range
for n in range(1,101):
  if (n % 3 == 0) and (n % 5 == 0): # If the number is completely divisable by 3 and 5, say Fizzbuzz
    print("FizzBuzz")
  elif (n % 5 == 0): # If the number is completely divisable by 5, say Buzz
    print("Buzz")
  elif (n % 3 == 0): # If the number is completely divisable by 3, say Fizz
    print("Fizz") 
  else: # If the number is not divisble by 3 or 5, print the number
    print(n)