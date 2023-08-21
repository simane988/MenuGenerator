import csv
import os.path


def get_dish_data(csv_file='dishes.csv') -> tuple:
    tmp_data = []

    if not os.path.isfile(csv_file):
        print(f"File {csv_file} dose not exist!")
        exit(1)

    # Read tmp_data from csv file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            tmp_data.append(row)

    tmp_data = tmp_data[3:]  # First three lines are trash

    # Make data look beautiful
    dish_data = []
    dish_cursor = 0
    dish_id = 0
    while dish_cursor < len(tmp_data):
        dish_name = tmp_data[dish_cursor][0]
        dish_total_cost = tmp_data[dish_cursor][3]
        dish_portions = tmp_data[dish_cursor][4]
        dish_portion_cost = tmp_data[dish_cursor][5]
        dish_products = [(tmp_data[dish_cursor][1], tmp_data[dish_cursor][2])]
        dish_cursor += 1
        while dish_cursor < len(tmp_data) and tmp_data[dish_cursor][0] == '':
            dish_products.append((tmp_data[dish_cursor][1], tmp_data[dish_cursor][2]))
            dish_cursor += 1

        dish_data.append((dish_id, dish_name, tuple(dish_products), dish_total_cost, dish_portions, dish_portion_cost))
        dish_id += 1

    return tuple(dish_data)


if __name__ == "__main__":
    print(get_dish_data())
