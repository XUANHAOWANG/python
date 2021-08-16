import PySimpleGUI as sg
import sys

# Design pattern 1 - First window does not remain active
title = 'adventure game'
def lay(layType):
    layout =[]
    if layType =='lay1':
     layout = [[ sg.Text('Adventure game')],     
          [sg.Button('Start')]]
    if layType =='lay2':
        layout= [[ sg.Text('Welcome to advenure game,Chose a way to ')], 
          [sg.Button('Jungle',key='Jungle')],
          [sg.Button('Castle',key='Castle')]]
    if layType =='lay3':
        layout = [[ sg.Text('You are in Jungle Chose a way to ')],     
            [sg.Button('Deep jungle')],
            [sg.Button('Seaside')]]  
    if layType =='lay4':
        layout = [[ sg.Text('you win ')]]   
    if layType =='lay5':
        layout = [[ sg.Text('Your are attacked by enemy,you died')]] 
    if layType =='lay6':
        layout = [[ sg.Text('You are in Castle Chose a way to ')],         
            [sg.Button('Market')],
            [sg.Button('Your house')]]  
    return layout




window=sg.Window(title,lay('lay1'))
event,value= window.read()

while True:
    if event == 'Start':
        window.close()
        window=sg.Window(title,lay('lay2'))
        event= window.read()
    if event=='Jungle':
        window.close()
        window=sg.Window(title,lay('lay3'))
        event= window.read()
    if event=='Deep jungle':
        window.close()
        window=sg.Window(title,lay('lay5'))
        event= window.read()
    if event=='Seaside':
        window.close()
        window=sg.Window(title,lay('lay4'))
        event= window.read()
        window.close()
    if event=='Castle':
        window.close()
        window=sg.Window(title,lay('lay6'))
        event= window.read()
        window.close()
         



     


 



    


    