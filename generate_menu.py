def generate_menu(menu_dict: dict):
    convert_name_to_id(menu_dict)


def convert_name_to_id(menu_dict: dict, name_to_id: dict):
    for i in menu_dict:
        menu_dict[i] = name_to_id[menu_dict[i]]

    return menu_dict
