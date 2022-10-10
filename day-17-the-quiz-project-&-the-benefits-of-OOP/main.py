class User:
    def __init__(self, name, follower_count, description, country):
        self.name = name
        self.followers = follower_count
        self.descr = description
        self.country = country


user_1 = User('Instagram', 346, 'Social media platform', 'United States')

print(f'{user_1.name}, a {user_1.descr}, from {user_1.country}')
