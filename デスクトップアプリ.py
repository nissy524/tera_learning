import PySimpleGUI as sg

layout= [[sg.Text('名前: '),sg.InputText(key='-NAME-')],
         [sg.Text('住所: '),sg.InputText(key='-ADDRESS-')],
         [sg.Button('実行',key='-SUBMIT-')]]

window = sg.Window('てらんぼ',layout,size=(300,150))

while True:
    event, values=window.read()
    if event == '-SUBMIT-':
        print(values['-NAME-'])
        print(values['-ADDRESS-'])
    if event == sg.WIN_CLOSED:
        break

        