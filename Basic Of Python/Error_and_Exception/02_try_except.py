def divide_numbers(a, b):
    try:
        result = a / b
        print('a/b : ',result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers.")
        return None
    else:
        return result
    finally:
        print("Execution of try-except block is complete.")

# Example usage
num1 = 10
num2 = 0

divide_numbers(num1,num2)

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print ("Error: can\'t find file or read data")
   fh.close()
