import random
from replit import clear
from game_data import data
from art import logo
from art import vs

def randomifier():
  return random.choice(data)
streak=True
points=0
while streak:
  print(logo)
  if points != 0:
    print(f"You're right! Current score: {points}")
  random_famous_A=randomifier()
  random_famous_B=randomifier()
  while random_famous_A == random_famous_B:
    random_famous_A=randomifier()
  if random_famous_A["follower_count"] > random_famous_B["follower_count"]:
    answer="a"
  else:
    answer="b"
  print(f"Compare A: {random_famous_A['name']}, a {random_famous_A['description']}, from {random_famous_A['country']}")
  print(vs)
  print(f"Against B: {random_famous_B['name']}, a {random_famous_B['description']}, from {random_famous_B['country']}")
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  if guess == answer:
    streak=True
    points+=1
    clear()
  else:
    streak=False
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {points}")
    
    
  
  
  
  
  


