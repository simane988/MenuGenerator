import PySimpleGUI as sg
from dish_parser import get_dish_data
from generate_menu import *


def main_gui():
    sg.theme("DarkGrey9")

    dish_data = get_dish_data()
    dish_list = tuple([i[1] for i in dish_data])
    name_to_id = {i[1]: i[0] for i in dish_data}
    name_to_id[''] = -1

    padding = (10, 10)
    col01 = [[sg.Text('', pad=padding)], [sg.Text('Breakfast', pad=padding)],
             [sg.Text('Lunch', pad=padding)], [sg.Text('Dinner', pad=padding)]]

    col1 = [[sg.Text('Monday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='mon_b', enable_events=True)],
            [sg.Combo(dish_list, pad=padding, key='mon_l')], [sg.Combo(dish_list, pad=padding, key='mon_d')]]

    col2 = [[sg.Text('Tuesday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='tue_b')],
            [sg.Combo(dish_list, pad=padding, key='tue_l')], [sg.Combo(dish_list, pad=padding, key='tue_d')]]

    col3 = [[sg.Text('Wednesday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='wed_b')],
            [sg.Combo(dish_list, pad=padding, key='wed_l')], [sg.Combo(dish_list, pad=padding, key='wed_d')]]

    col4 = [[sg.Text('Thursday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='thu_b')],
            [sg.Combo(dish_list, pad=padding, key='thu_l')], [sg.Combo(dish_list, pad=padding, key='thu_d')]]

    col02 = [[sg.Text('', pad=padding)], [sg.Text('Breakfast', pad=padding)],
             [sg.Text('Lunch', pad=padding)], [sg.Text('Dinner', pad=padding)]]

    col5 = [[sg.Text('Friday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='fri_b')],
            [sg.Combo(dish_list, pad=padding, key='fri_l')], [sg.Combo(dish_list, pad=padding, key='fri_d')]]

    col6 = [[sg.Text('Saturday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='sat_b')],
            [sg.Combo(dish_list, pad=padding, key='sat_l')], [sg.Combo(dish_list, pad=padding, key='sat_d')]]

    col7 = [[sg.Text('Sunday', pad=padding)], [sg.Combo(dish_list, pad=padding, key='sun_b')],
            [sg.Combo(dish_list, pad=padding, key='sun_l')], [sg.Combo(dish_list, pad=padding, key='sun_d')]]

    col8 = [[sg.Text('', pad=padding)], [sg.Button('Done')], [sg.Text('', pad=padding)], [sg.Text('', pad=padding)]]

    layout = [[sg.Column(col01), sg.Column(col1), sg.Column(col2), sg.Column(col3), sg.Column(col4)],
              [sg.Column(col02), sg.Column(col5), sg.Column(col6), sg.Column(col7), sg.Column(col8)]]

    window = sg.Window('Menu Generator', layout)

    while True:  # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == "Done":
            print(convert_name_to_id(values, name_to_id))


if __name__ == '__main__':
    main_gui()
