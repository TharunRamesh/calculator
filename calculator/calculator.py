#calculator
from art import logo
print(logo)
#add
def add(n1,n2):
  return n1+n2

#subtract
def sub(n1,n2):
  return n1-n2

#multiply
def mul(n1,n2):
  return n1*n2

#division
def div(n1,n2):
  return n1/n2

operation = {
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}
def calculator():
  num1=float(input("what is the first number? "))
  
  for symbol in operation:
    print(symbol)
  operation_symbol=input("the operation you want to do: ")
  
  num2= float(input("enter the second number: "))
  
  cal_function=operation[operation_symbol]
  answer=cal_function(num1,num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  check= True
  while check:
    check= input(f"type 'y' if you want to contiue calculating with {answer}, or type 'n' to countinue new calculation: \n ").lower()
    if check!='y' and check!= 'n':
      print("wrong input enter the right one")
      e= input("or type 'exit' if you want to exit\n").lower()
      if e== 'exit':
        check=False
    if check=='y':
      operation_symbol=input("the operation you want to do: ")
      num3= float(input("enter the second number: "))
      num1= answer
      num2=num3
      cal_function=operation[operation_symbol]
      print(f"{num1} {operation_symbol} {num2} = {answer}")
      
    if check=='n':
      calculator()
calculator()