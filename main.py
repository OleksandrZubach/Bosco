# def get_user_input():
#     while True:
#         name = input('Enter name --> ')
#         if len(name) > 0 and len(name) <= 16:
#             print('good')
#             break
#         else:
#             print('bad')
#     # while True:
#     moon = int(input('Enter moon --> '))
#         # if moon > 0 and moon <= 12:
#         #     print('very good')
#         #     break
#         # else:
#         #     print('very bad')
#     while True:
#         year = int(input('Enter year --> '))
#         if year >= 5 and year <= 120:
#             print('amazing')
#             break
#         else:
#             print('oops')
#     return name, moon, year
#
# def valide_month():
#     moon = moon
#     print(moon)
#     try:
#         if moon >= 0 and moon <= 12:
#             print('very good')
#         else:
#             print('very bad')
#     except ValueError:
#         print('Невірне значення')
#
#
#
#
#
# print('fsdfsdfsd')
#
# if __name__ == '__main__':
#     get_user_input()
#     valide_month()



def get_user_input():
    while True:
        name = input("Введіть ім'я: ")
        if valide_name(name):
            break
        else:
            # print("Некоректне ім'я. Будь ласка, спробуйте щераз")
            continue
    while True:
        year = int(input("Введіть рік народження (від 5 до 120 років): "))
        if validate_year(year):
            break
        else:
            print("Некоректний рік. Будь ласка, спробуйте ще раз.")

    while True:
        month = int(input("Введіть місяць народження (від 1 до 12): "))
        if validate_month(month):
            break
        else:
            print("Некоректний місяць. Будь ласка, спробуйте ще раз.")

    return name, year, month

def valide_name(name):
    while True:
        name = name
        if 0 < len(name) <=16:
            break
        else:
            print('Невірне значення')

def validate_year(year):
    try:
        while True:
            year = int(year)
            if 5 <= year <= 120:
                return year
            else:
                print('Введено погане значення')
    except ValueError:
        print("Введено не число")

def validate_month(month):
    try:
        while True:
            month = int(month)
            if 1 <= month <= 12:
                return  month
            else:
                print('Введено невірне значення')
    except ValueError:
        print("Введено не число")




def create_test_file(name, year, month):
    with open("test_file.txt", "w") as file:
        file.write(name + "\n")
        file.write(str(year) + "\n")
        file.write(str(month) + "\n")


def main():
    name, year, month = get_user_input()
    create_test_file(name, year, month)
    print("Дані успішно записані у файл 'test_file.txt'.")


if __name__ == "__main__":
    main()