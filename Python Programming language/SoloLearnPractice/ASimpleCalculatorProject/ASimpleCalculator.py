while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input("Your decision: ")
   user_input = user_input.lower()

   if user_input == "quit":
      print("Ok, nessuna operazione verrà eseguita.")
      break
   elif user_input == "add" or user_input == "+":
       num1 = float(input("Enter a number: \n"))
       num2 = float(input("Enter another number: \n"))
       result = str(num1 + num2)
       print("The answer is " + result)
       break
   elif user_input == "subtract" or user_input == "-":
       num1 = float(input("Enter a number: \n"))
       num2 = float(input("Enter another number: \n"))
       result = str(num1 - num2)
       print("The answer is " + result)
       break
   elif user_input == "multiply" or user_input == "*":
       num1 = float(input("Enter a number: \n"))
       num2 = float(input("Enter another number: \n"))
       result = str(num1 * num2)
       print("The answer is " + result)
       break
   elif user_input == "divide" or user_input == "/":
       num1 = float(input("Enter a number: \n"))
       num2 = float(input("Enter another number: \n"))
       result = str(num1 / num2)
       print("The answer is " + result)
       break
   else:
      print("Unknown input, retry !")