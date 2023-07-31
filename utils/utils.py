import json
from datetime import date




def unpacking_data():
    with open("operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def filtered_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_date(data):
    data = date.fromisoformat(data[:10])
    return data.strftime("%d.%m.%Y")


def get_from_or_to(data):
    data = data.split()
    if len(''.join(data[-1])) == 20:
        return f"{''.join(data[0:-1])} {data[-1][0:4]} {data[-1][4:6]}** **** {data[-1][-4:]}"

    else:
        return f"{''.join(data[0:-1])} **{data[-1][2:6]}"


def get_list_of_operations(data):
    list = []
    for row in data:
        date_of_operation = get_date(row["date"])
        description = row["description"]
        if "from" in row:
            open_from = get_from_or_to(row["from"])
        else:
            open_from = ''
        to = get_from_or_to(row["to"])
        operation_amount = row["operationAmount"]["amount"]
        operation_cyrrency = row["operationAmount"]["currency"]["name"]
        list.append(f"{date_of_operation} {description} \n{open_from} "
                              f"{to} \n{operation_amount} {operation_cyrrency}")
    return list