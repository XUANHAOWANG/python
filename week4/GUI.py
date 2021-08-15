import PySimpleGUI as sg
import sys

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Adventure game')],     
          [sg.Button('Start')]]
win1 = sg.Window('win1', layout)
win2=False
win3=False            
event,value=win1.read()
if event=="Start":
        layout = [[ sg.Text('Chose a way to ')],     
          
          [sg.Button('Jungle')],
          [sg.Button('Castle')]]  
win2 = sg.Window('win2', layout)
event,value=win2.read()
win1.close()
  
if event=="Jungle":
    layout = [[ sg.Text('You are in Jungle Chose a way to ')],     
           
            [sg.Button('Deep jungle')],
            [sg.Button('Seaside')]]   
    win3 = sg.Window('win3', layout)
    event,value=win3.read() 
    if event=="Deep jungle":
         layout = [[ sg.Text('you win ')]]   
         win2 = sg.Window('win2', layout)
         
        
    elif event=="Seaside":
        layout = [[ sg.Text('Your are attacked by enemy,you died')]]     
        win2 = sg.Window('win2', layout)
        

elif event=="Castle":
    layout = [[ sg.Text('You are in Castle Chose a way to ')],         
            [sg.Button('Market')],
            [sg.Button('Your house')]]   
    win3 = sg.Window('win3', layout)
    event,value=win3.read()
        

 



    


    