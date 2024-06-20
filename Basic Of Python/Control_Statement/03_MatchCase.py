n = int(input("Enter the number of day (0-6) : "))

match(n):
    case 0 : print('Sunday')
    case 1 : print('Monday')
    case 2 : print('Tuesday')
    case 3 : print('Wednesday')
    case 4 : print('Thursday')
    case 5 : print('Friday')
    case 6 : print('Saturday')
    case _ : print("Invalid Day!!!")


role = input("Enter your role : ")
match(role):
    case 'CEO'|'Owner'|'Admin' : print("Full access to System")
    case 'Employee' : print("Limited Access")
    case 'None' : print("No access")



def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))




#Match with if-else
def intr(details):
   match details:
      case [amt, duration] if amt<10000:
         return amt*10*duration/100
      case [amt, duration] if amt>=10000:
         return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))