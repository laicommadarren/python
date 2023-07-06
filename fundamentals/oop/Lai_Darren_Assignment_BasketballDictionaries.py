players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
"""
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team
"""

class Player:
    def __init__(self, player_dictionary):
        self.name = player_dictionary["name"]
        self.age = player_dictionary["age"]
        self.position = player_dictionary["position"]
        self.team = player_dictionary["team"]

    def __repr__(self):
        return "Player: {}, {} years old, position: {}, team: {}".format(self.name, self.age, self.position, self.team)
    
    @classmethod
    def get_team(cls, team_list):
        player_objects = []
        for dict in team_list:
            player_objects.append(cls(dict)) # cls is the instance with the given dictionary
            return player_objects
# Challenge 2: Create instances using individual player dictionaries.
# Given these variables, create Player instances for each of the following dictionaries. Be sure to instantiate these outside the class definition, in the outer scope.

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}

player_kevin = Player(kevin)
print(player_kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
# Finally, given the example list of players at the top of this module (the one with many players) write a for loop that will populate an empty list with Player objects from the original list of dictionaries.

# ... (class definition and large list of players here)

new_team = []
for player_dictionary in players:
    player = Player(player_dictionary)
    new_team.append(player)

print(new_team)


# Write your for loop here to populate the new_team variable with Player objects.
    
# NINJA BONUS: Add a get_team(cls, team_list) @class method
# Add an @class method called get_team(cls, team_list) that, given a list of dictionaries populates and returns a new list of Player objects. Be sure to test your method!