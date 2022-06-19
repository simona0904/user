from user import User

users = [
    User("Cordos", "Simona", "456789", "abs.dfg@ya.com", True),
    User("Mates", "Bogdan", "123456", "aaa.dfg@ya.com", True),
    User("Cordos", "Ciprian", "789456", "bbb.dfg@ya.com", True),
]

users[1].deactivate()

# print surname si daca e activ sau nu pt fiecare user

for user in users:
    print(user.surname)
    print(user.activ)

users[2].email = "asd.zxc@ya.com"   
print(user.email) 




    



