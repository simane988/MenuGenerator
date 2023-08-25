import csv


def generate_menu(menu_dict: dict):
    convert_name_to_id(menu_dict)


def convert_name_to_id(menu_dict: dict, name_to_id: dict):
    for i in menu_dict:
        menu_dict[i] = name_to_id[menu_dict[i]]

    return menu_dict


def export_menu(menu_dict: dict):

    # Read tmp_data from csv file
    with open(".tmp/tmp_menu.csv", 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(['mealtime', 'dish_id'])
        for key in menu_dict:
            csv_writer.writerow([key, menu_dict[key]])
