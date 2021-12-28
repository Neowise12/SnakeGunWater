import random
def game(x,y):
    
    if(x==y):
        print( "tie computer choosed  "+y)
    elif x=="s" and y=="w" :
        print( "YOU IS THE WINNER computer choosed   "+y)
    elif x=="w" and y=="s" :
        print( "YOU IS THE LOOSER computer choosed   "+y)
    elif x=="g" and y=="s" :
        print( "YOU IS THE WINNER computer choosed   "+y)  
    elif x=="s" and y=="g" :
        print( "YOU IS THE LOOSER computer choosed   "+y)   
    elif x=="g" and y=="w" :
        print( "YOU IS THE LOOSER computer choosed   "+y)            
    elif x=="w" and y=="g" :
        print( "YOU IS THE WINNER computer choosed   "+y)
    

randomno = random.randint(1, 3)
computer="choose s or g or w"
if randomno==1:
    computer="s"
elif randomno==2:
    computer="w"  
elif randomno==3:
    computer="g"      
you=input("what you want snake(s),water(w),gun(g)?")    
game(you, computer)



####### HARRY'S ANSWER  #####
# import random

# # Snake Water Gun or Rock Paper Scissors
# def gameWin(comp, you):
#     # If two values are equal, declare a tie!
#     if comp == you:
#         return None

#     # Check for all possibilities when computer chose s
#     elif comp == 's':
#         if you=='w':
#             return False
#         elif you=='g':
#             return True
    
#     # Check for all possibilities when computer chose w
#     elif comp == 'w':
#         if you=='g':
#             return False
#         elif you=='s':
#             return True
    
#     # Check for all possibilities when computer chose g
#     elif comp == 'g':
#         if you=='s':
#             return False
#         elif you=='w':
#             return True

# print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
# randNo = random.randint(1, 3) 
# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp = 'w'
# elif randNo == 3:
#     comp = 'g'

# you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
# a = gameWin(comp, you)

# print(f"Computer chose {comp}")
# print(f"You chose {you}")

# if a == None:
#     print("The game is a tie!")
# elif a:
#     print("You Win!")
# else:
#     print("You Lose!")