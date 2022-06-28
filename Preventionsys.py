from openpyxl import load_workbook
import PySimpleGUI as sg
from datetime import datetime

def mainfunc():
    sg.theme('DarkAmber')

    layout = [[sg.Text('First Name'), sg.Push(), sg.Input(key='FIRST_NAME')],
              [sg.Text('Contact'), sg.Push(), sg.Input(key='CONTACT')],
              [sg.Text('Email id'), sg.Push(), sg.Input(key='EMAIL_ID')],
              [sg.Text('Alcohol Level'), sg.Push(), sg.Input(key='ALCOHOL_LEVEL')],
              [sg.Text('Amount Of Sleep'), sg.Push(), sg.Input(key='AMOUNT_OF_SLEEP')],
              [sg.Button('Submit'), sg.Button('Close'), sg.Button('Results')]
              ]

    # 'window=sg.window('Data Entry',layout,element_justification='center')'
    window = sg.Window('Data Entry', layout, element_justification='center')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':
            break
        if event == 'Submit':
            try:
                wb = load_workbook('D:\\2ndyear\\Semister-2\\DataScience\\Cpdtaset.xlsx')
                sheet = wb['Sheet1']
                ID = len(sheet['ID'])
                time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                data = [ID, values['FIRST_NAME'], values['CONTACT'], values['EMAIL_ID'], values['ALCOHOL_LEVEL'],
                        values['AMOUNT_OF_SLEEP']]
                sheet.append(data)
                wb.save('D:\\2ndyear\\Semister-2\\DataScience\\Cpdtaset.xlsx')
                window['FIRST_NAME'].update(value='')
                window['CONTACT'].update(value='')
                window['EMAIL_ID'].update(value='')
                window['ALCOHOL_LEVEL'].update(value='')
                window['AMOUNT_OF_SLEEP'].update(value='')
                window['FIRST_NAME'].set_focus()
                sg.popup('Success', 'Data Saved')
            except PermissionError:
                sg.popup('Sorry', 'File is being used by another user')
        if event == "Results":
            try:
                from model1 import predict
                a = float(values['ALCOHOL_LEVEL'])
                s = float(values['AMOUNT_OF_SLEEP'])
                predict(a, s)
            except ValueError as a:
                print(a)
                sg.popup('Sorry!!!Please Try Again')

    window.close()
