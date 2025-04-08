users = [
    {"name": "Wiktor", "Location": "Kutno", "posts": 500},
    {"name": "Mikołaj", "Location": "Przasnysz", "posts": 100},
    {"name": "Krzysztof", "Location": "Poznań", "posts": 300},
    {"name": "Bartosz", "Location": "Ostrołęka", "posts": 800},

]

for user in users:
    print(f"Twój znajomy   {user['name']},z {user['location']} opublikował {user['posts']} postów")
