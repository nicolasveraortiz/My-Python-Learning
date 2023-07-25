import random
from replit import clear
restart=True

def play_game():
  choice=input("Do you wanna keep playing? press 'y' if you want, or press 'n' if not: ").lower()
  if choice=="y":
    return True
  else:
    return False
def deal_card():
#11 is the Ace.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  chosen_card=random.choice(cards)
  return chosen_card

def calculate_score(cards):
  """Take a list of cards and calculate the score"""
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if computer_score == 0 and user_score == 0:
    print("It's a draw!")
  elif user_score == 0:
    print("You won!")
  elif computer_score == 0:
    print("Computer won!")
  elif user_score > 21:
    print("Computer won!")
  elif user_score > computer_score:
    print("You won!")
  elif user_score < computer_score and computer_score < 21:
    print("Computer won!")
  elif user_score < computer_score and computer_score > 21:
    print("You won!")
  elif user_score == computer_score:
    print("It's a draw!")
  if user_score==0 and computer_score==0:
    print("Both of you got a blackjack!")
  elif user_score==0:
    print(f"The computer's score is {computer_score}, and your score is a blackjack!")
  elif computer_score==0:
    print(f"The computer's score is a blackjack, and your score is {user_score}")
  else:
    print(f"The computer's score is {computer_score}, and your score is {user_score}!")
    
while restart==True:
  clear()
  user_cards = []
  computer_cards = []
  is_game_over=False
  for n in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
  print (user_cards)
  user_score=calculate_score(user_cards)
  computer_score=calculate_score(computer_cards)
  print(f"This is your score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over=True
  
  while not is_game_over:
    pa=input("Do you want to pass ('p') or add another card('a')?").lower()
    if pa == "a":
      user_cards.append(deal_card())
      user_score=calculate_score(user_cards)
      print(user_cards)
      print(f"This is your score: {user_score}")
    if user_score > 21:
      is_game_over=True
    if pa == "p":
      is_game_over=True
  
  
  while computer_score < 17 and user_score !=0 and computer_score!=0:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
    
  compare(user_score,computer_score)
  restart=play_game()
