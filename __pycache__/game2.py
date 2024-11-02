from art import art
from data import data
import random
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"




account_a = random.choice(data)
score=0
game_over = False
while not game_over:
    account_b = random.choice(data) 
    if account_a == account_b:
        account_b = random.choice(data)
    else:
        check = False
   
    account_b = random.choice(data)
    print(format_data(account_a))
    print("VS")
    print(format_data(account_b))
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["followers"]
    b_follower_count = account_b["followers"]
    is_correct=check_answer(guess, a_follower_count, b_follower_count)
    
    if is_correct:
        score+=1
        print(f"You're right! Current score: {score}.")
        account_a=account_b
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        exit()
        game_over=True
