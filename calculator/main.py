from replit import clear
from art import logo
def add(n1,n2):
  return n1+n2
def subtract (n1,n2):
  return n1-n2
def multiply (n1,n2):
  return n1*n2
def division (n1,n2):
  return n1/n2
operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":division
}
operation_end=False
print(logo)
while not operation_end:
  n1=float(input("What's your first number?: "))
  n2=float(input("What's your second number?: "))
  for sign in operations:
    print(sign)
  operation_sign=(input("Pick a symbol from above to operate with the numbers: "))
  answer=operations[operation_sign](n1,n2)
  print(f"{n1} {operation_sign} {n2} = {answer}")
  choice=input("Keep calculating with the previous answer, press Y, star a new calculating press N, end the program press F: ").lower()
  if choice=="y":
    while choice == "y":
      previous_answer=answer
      operation_sign=input("Pick another symbol that operates with the last answer: ")
      n3=float(input("What's your new number?: "))
      answer=operations[operation_sign](previous_answer,n3)
      print(f"{previous_answer} {operation_sign} {n3} = {answer}")
      choice=input("Keep calculating with the previous answer, press Y, star a new calculating press N, end the program press F: ").lower()
  if choice == "n":
    clear()
    print (logo)
  if choice == "f":
    operation_end=True
    print("Bye!")
  
    
    
    
    
