
import time
import random
import sys

#fight
def fight():  
    print("start fight with enemy")
    time.sleep(1)
    print("fight start in 3 seconds")
    time.sleep(1)
    print("fight start in 2 seconds")
    time.sleep(1)
    print("fight start in 1 second")
    time.sleep(1)
    enemy_life = 200
    player_life = 200
    while player_life > 0 and enemy_life > 0:      
        player_attack = random.randint(10,25)     
        enemy_attack = random.randint(10,25) 
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print("enemy_life:"+str(enemy_life)+"-"+str(player_attack))
        print("player_life:"+str(player_life)+"-"+str(enemy_attack))
        time.sleep(0.9)
    if(player_life > 0 and enemy_life <= 0):
        print('player win')
    else:     
        bre()   
        #brave
def bre() :
          
 print("you died,Game over ")
 sys.exit()
   
def seaside():
    fight()
  
#jungle
def jungle():
 path=input("which way you go/1:deep jungle/2:seaside")
 if(path=="1"):
     print("You are going to deep jungle")
     
 if(path=="2"):
     print("You are going to seaside")
     seaside()      

def market():
    print("your are going to start a gamble game")
    time.sleep(1)
    print("start in 3 seconds")
    time.sleep(1)
    print("start in 2 seconds")
    time.sleep(1)
    print("start in 1 second")
    time.sleep(1)

    your_point=random.randint(1,6)
    opponent_point=random.randint(1,6)  
    print("opponent point is ："+str(opponent_point)+"---your point is ："+str(your_point))
    if(opponent_point>your_point):
        print("opponent win")
    else:
         print("you win")   
#castle
def castle():
 road=input("chosen your road/1:market/2:palace")
 if(road=="1"):
     print("You are going to market")
     market()

 if(road=="2"):
     print("You are going to palace")     
#game start here
direction=input("chosen direction/1:go to jungle/2:go to castle")
if(direction=="1"):
    print("go to jungle, you found a enemy")
    fight()
    jungle()
if(direction=="2"):
    print("go to castle")   
    castle() 


