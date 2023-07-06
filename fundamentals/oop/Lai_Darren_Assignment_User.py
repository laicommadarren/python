class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # following are default attributes
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("first name:", self.first_name)
        print("last name:", self.last_name)
        print("email:", self.email)
        print("age:", self.age)
    def enroll(self):
        if self.is_rewards_member == True:
            print ("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True
    def spend_points(self, amount):
        if amount >= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print ("You do not have enough points to redeem.")

user_darren = User("Darren", "Lai", "test@test.com", 30)
print(user_darren.display_info())
print(user_darren.enroll())

user_mom = User("Honglin", "Lai", "mom@test.com", 62)
user_sis = User("Melissa", "Lai", "melissa@test.com", 23)

print(user_mom.spend_points(50))
print(user_sis.enroll())
print(user_sis.spend_points(80))
print (user_darren.display_info(), user_mom.display_info(), user_sis.display_info())
