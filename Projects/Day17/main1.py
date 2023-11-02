class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "srinivas")
user_2 = User("002", "sowmya")

user_1.follow(user_2)

print(f"{user_1.user_name} followers and following are ", user_1.followers, user_1.following)

print(f"{user_2.user_name} followers and following are ", user_2.followers, user_2.following)

##############Methods##
