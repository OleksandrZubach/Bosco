def get_user_input():
    while True:
        name = input('Enter name --> ')
        if len(name) > 0 and len(name) <= 16:
            print('good')
            break
        else:
            print('bad')
    # while True:
    moon = int(input('Enter moon --> '))
        # if moon > 0 and moon <= 12:
        #     print('very good')
        #     break
        # else:
        #     print('very bad')
    while True:
        year = int(input('Enter year --> '))
        if year >= 5 and year <= 120:
            print('amazing')
            break
        else:
            print('oops')
    return name, moon, year

def valide_month(moon):
    try:
        if moon >= 0 and moon <= 12:
            print('very good')
        else:
            print('very bad')
    except ValueError:
        print('Невірне значення')







if __name__ == '__main__':
    get_user_input()
    valide_month('moon')
