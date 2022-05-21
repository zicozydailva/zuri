# Calc to perform basic arithmetic operations

def calculator():
  print("Welcome to the calculator")
  print("Please select an operation")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Quit")
  try:
    operation = int(input("Choose Operation(Enter Either 1-6): "))
    if operation == 1:
      number1 = int(input("Provide first number: "))
      number2 = int(input("Provide second number: "))
      print("Result:",number1 + number2)
      calculator()
    elif operation == 2:
      number1 = int(input("Provide first number: "))
      number2 = int(input("Provide second number: "))
      print("Result:",number1 - number2)
      calculator()
    elif operation == 3:
      number1 = int(input("Provide first number: "))
      number2 = int(input("Provide second number: "))
      print("Result:",number1 * number2)
      calculator()
    elif operation == 4:
      number1 = int(input("Provide first number: "))
      number2 = int(input("Provide second number: "))
      print("Result:",number1 / number2)
      calculator()
    elif operation == 5:
      number1 = int(input("Provide first number: "))
      number2 = int(input("Provide second number: "))
      print("Result:",number1 % number2)
      calculator()
    elif operation == 6:
      print("Goodbye!!!")
      exit()
    else:
      print("Please Provide a valid number to match operation")
      calculator()
  except ValueError:
    print("Please enter only numbers")
    calculator()

calculator()