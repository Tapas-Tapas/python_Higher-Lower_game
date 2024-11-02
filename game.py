from art import art
from art import logo
import random
import data
print(art)
score=0
game_over=False
while not game_over:
    a=random.choice(data.cricket_players)
    b=random.choice(data.football_players)
  
    print(f"Cricket_player: {a["name"]} is a {a["description"]} from {a["country"]}")
    print(logo) 
    print(f"Football_player: {b["name"]} is a {b["description"]} from {b["country"]}")
    compare=input("Who has more followers? Type 'A' for cricket player and 'B' for football player: ").lower()
    if compare=="a":
        if a["followers"]>b["followers"]:
            score+=1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            
            game_over=True
    elif compare=="b":
            if b["followers"]>a["followers"]:
                score+=1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_over=True
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over=True