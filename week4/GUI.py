import PySimpleGUI as sg


# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1')],     
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Start')]]
win1 = sg.Window('Adventure game', layout)
win2_active=False
win3_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)

    if ev1 == 'Start'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('chose a way to go to')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Jungle')],
                   [sg.Button('Castle')]]
        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read(timeout=100)
            if ev2  == 'Jungle':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
            if ev2 == 'Castle':
                win2.close()
                win3_active =True
                win1.UnHide()
    while True:
        ev3, vals3 = win3.read(timeout=100)        
        layout3=[[sg.Text('you win')]] 
        win3=sg.Window('Window 3', layout3)       
    
    

