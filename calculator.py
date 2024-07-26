print("1. ADD \n2. SUBRACT\n3. MULTIPLY\n4. DIVIDE")
def result():
  choice=int(input("Select an operation from 1-4: "))
  num1=float(input("Enter the first number: "))
  num2=float(input("Enter the second number: "))

  if choice==1:
    print(f"The Sum is: {num1+num2}")
  elif choice==2:
    print(f"The Difference is: {num1-num2}")
  elif choice==3:
    print(f"The Product is: {num1*num2}")
  elif choice==4:
    print(f"The Result is: {num1/num2}")
  else:
    print("INVALID INPUT")

while True:
    result()
    choice = input("Do you want calculate again (y/n): ").lower()
    if choice != 'y':
        print("Thank you!")
        break