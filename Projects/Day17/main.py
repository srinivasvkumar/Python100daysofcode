class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name


user_1 = User("001", "srinivas")

print(user_1.user_name, user_1.id)


##############
