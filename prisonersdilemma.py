#prisoner's dilemma

import random

print("You and your friend are presented with two envelopes that have $100 each. ")
print("Each round, you and your friend have the opportunity to either split or steal. ")
print("If both of you choose to split, you each recieve $100. If one of you splits ")
print("and the other steals, then the person who steals recieves $200. But if both ")
print("of you steal, you each recieve nothing. Good luck!")


x=0
y=0

while True:
    user_action = input("Choose either SPLIT or STEAL." )
    possible_actions = ["SPLIT", "STEAL"]
    computer_action = random.choice(possible_actions)

    if user_action == "SPLIT":
        if computer_action == "STEAL":
            y=y+200
            print("You have chosen to split, but your friend has betrayed you. ")
            print("Your total is now $",x,". Your friend's total is $",y,"." )
        else:
            x=x+100
            y=y+100
            print("You have both selected to split! Your total is $",x,". Your friend's total is now $",y,"." )
    elif user_action == "STEAL":
        if computer_action == "SPLIT":
            x=x+200
            print("Your friend has chosen to split, but you have betrayed them. ")
            print("Your total is now $",x,". Your friend's total is now $",y,"." )
        else:
            print("You have both selected to steal and now get nothing! Your total is now",x,". Your friend's total is",y,"." )
  

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        if x > y:
            print("Game over!" )
            print("Congrats! You made $",x,"whiile your friend only made $",y,"." )
        elif x == y:
            print("Game over!" )
            print("It's a tie!")
        else:
            print("Game over!" )
            print("Your friend made $",y," while you only made $",x,". Better luck next time :/" )
        break    
       
 
        
                     

        
