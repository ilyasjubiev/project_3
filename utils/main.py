from utils import filtered_data, unpacking_data, get_last_values, get_list_of_operations


def main():
    COUNT_LAST_VALUES = 5

    data = unpacking_data()

    data = filtered_data(data)
    data = get_last_values(data, count_last_values=COUNT_LAST_VALUES)
    data = get_list_of_operations(data)


    print("INFO: Вывод транзакций...")
    for row in data:
        print(row, end='\n\n')


if __name__ == '__main__':
    main()






