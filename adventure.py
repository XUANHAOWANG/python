

import time
import random



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
    player_life = 200
    player_attack = random.randint(10,25)
    enemy_life = 200
    enemy_attack = random.randint(10,25)  
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print("enemy_attack:"+str(player_life))
        print("player_attack:"+str(enemy_life))
        time.sleep(0.9)
    if(player_life > 0 and enemy_life <= 0):
        print('player win')
    else:
        print('enemy win')
        bre()
   

        
        #brave
def bre():
    print("you died ")
    
        
  

#jungle
def jungle():
 path=input("which way you go/1:deep jungle/2:seaside")
 if(path=="1"):
     print("You are going to deep jungle")
     
 if(path=="2"):
     print("You are going to seaside")      

#castle
def castle():
 road=input("chosen your road/1:market/2:palace")
 if(road=="1"):
     print("You are going to market")
 if(road=="2"):
     print("You are going to palace")            


direction=input("chosen direction/1:go to jungle/2:go to castle")
  
if(direction=="1"):
    print("go to jungle, you found a enemy")
    fight()
    jungle()
if(direction=="2"):
    print("go to castle")   
    castle() 
