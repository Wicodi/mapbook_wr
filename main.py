users = [
    {"name": "Wiktor", "Location": "Kutno", "posts": 500},
    {"name": "Mikołaj", "Location": "Przasnysz", "posts": 100},
    {"name": "Krzysztof", "Location": "Poznań", "posts": 300},
    {"name": "Bartosz", "Location": "Ostrołęka", "posts": 800},

]



def get_user_info(users_data: list)->None:
    for user in users:
        print(f"Twój znajomy   {user['name']}, z miejscowości: {user['Location']} opublikował {user['posts']} postów")


get_user_info(users)