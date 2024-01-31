import PySimpleGUI as sg
import DetectionModule

sg.change_look_and_feel('GreenTan')
layout = [
    [sg.Text("Welcome To Expression Finder")],
    [sg.Text("Please press Q to exit out of frame")],
    [sg.Text("Enter the pathway for the video file", )],
    [sg.InputText(key='__file__')],
    [
        sg.Button("Proceed", key='cont'),
        sg.Button("Quit"),
        sg.Button("Use camera")
    ],
]

window = sg.Window("EXPRESSION AI EMOTION FINDER", layout)

while True:
    event, values = window.read()
    if event == 'Quit':
        break
    elif event == 'cont':
        DetectionModule.DetectionModule(values["__file__"])
    elif event == "Use camera":
        DetectionModule.DetectionModule(None)

sg.popup("Thanks for your time happy coding")
