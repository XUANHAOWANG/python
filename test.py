import PySimpleGUI as sg
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

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Adventure game'),],      
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Start')]]

win1 = sg.Window('Adventure game ', layout)
win2_active=False
win3_active=False
while True:
    event, value = win1.read(timeout=100)
    if event is None:
        break
    if event == 'Start'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('chose a way to go to')],
        [sg.Button('Jungle')],       # note must create a layout from scratch every time. No reuse
        [sg.Button('castle')]]
#step2
win2 = sg.Window('Your are in start point', layout2)
while True:
    event, value = win2.read()
    if event is None or event == 'Jungle':
        win3_active=True#step        
        win2.UnHide()
            # sg.Popup(fight())
        layout3=[[sg.Text('You found a monster')],
        [sg.Button('Jungle')],       # note must create a layout from scratch every time. No reuse
        [sg.Button('castle')]] 
    win3=sg.Window('',layout3)
            


