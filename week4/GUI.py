import PySimpleGUI as sg


# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1')],     
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Start')]]
win1 = sg.Window('Adventure game', layout)
win2=False
win3=False
while True:
    ev1, vals1 = win1.read(timeout=100)

    if ev1 == 'Start'  and not win2:
        win2 = True
        win1.Hide()
        layout2 = [[sg.Text('chose a way to go to')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Jungle')],
                   [sg.Button('Castle')]]
        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read(timeout=100)
            if ev2 == 'Jungle':
                win2.close()
                win1.UnHide()
                break
            if ev2 == 'Castle':
                win2.close()
                win3 =True
                win1.UnHide()
    while win3==True:
        ev3, vals3 = win3.read(timeout=100) 
        layout3=[[sg.Text('you are in castle')],[sg.Button('Exist')]]   
        win3=sg.Window('Window 3', layout3)
        if ev3=='Exist':
            break
              
        
             
    
    

