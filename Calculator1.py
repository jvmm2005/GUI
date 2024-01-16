import PySimpleGUI as sg

# Define the layout of the calculator
layout = [
    [sg.Text('Enter two numbers:')],
    [sg.InputText(key='num1'), sg.Text('+'), sg.InputText(key='num2')],
    [sg.Button('Add'), sg.Button('Exit')],
    [sg.Text(size=(20, 1), key='result')]
]

# Create the window
window = sg.Window('Basic Calculator', layout)

# Event loop to handle button clicks
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Add':
        try:
            num1 = float(values['num1'])
            num2 = float(values['num2'])
            result = num1 + num2
            window['result'].update(f"Result: {result}")
        except ValueError:
            window['result'].update('Invalid input. Enter numbers.')

# Close the window
window.close()