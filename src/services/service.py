import database

Prompt = """
-----landlord menu------
0. Exit application
1. Insert new user
2. Insert new unit
3. Retrieve all users
4. Retrieve all units that belong to a specific user
"""
class BasicMenu():
    def prompt(self):
        conn = database.connect()
        database.create_users_table(conn)
        database.create_units_table(conn)
        while True:
            selected = input(Prompt)
            if selected == '0':
                break
            elif selected == '1':
                username = input('Insert username: ')
                password = input('Select password: ')
                database.create_user(conn, username, password)
            elif selected == '2':
                username = input('Insert username: ')
                address = input('Insert unit address: ')
                location = input('Insert unit location: ')
                square_meters = float(input('Insert unit size in square meters: '))
                asking_price = float(input('Insert unit asking price: '))
                purchase_price = float(input('Insert unit asking price: '))
                database.create_unit(conn, username, address, location, square_meters, asking_price, purchase_price)
            elif selected == '3':
                all_users = database.get_all_users(conn)
                for user in all_users:
                    print(user)
            elif selected == '4':
                selected_username = input('Select user(name) whose units you wish to see: ')
                selected_units = database.get_all_units_by_username(conn, selected_username)
                for unit in selected_units:
                    print(unit)
            else:
                print('Unknown input, please select again')
        return "Menu closed"


basic_menu = BasicMenu()
basic_menu.prompt()