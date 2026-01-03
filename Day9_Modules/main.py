
from user_manager import add_user,find_user

users = []

add_user(users,{"name":"Amit","email":"amit@gmail.com"})

print(find_user(users,"amit@gmail.com"))