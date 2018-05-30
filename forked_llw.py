# uncomment the following line to use Option B
dictionary_health = {'Sanaa': 145, 'Bidziil': 125, 'Ishita': 135 , 'Hao': 130 , 'Adela': 140 , 'The Bionic Man': 150}
        
dictionary_sig_moves = {'Spinning Crane Leg Kick': 15, 'Lunar Assault': 25, 'Sleeper Headlock': 20, 'Elevated Elbow Smash': 15, 'Firework Neckbreacker': 25, 'Bionic Elbow Drop': 15}

dictionary_fin_moves = {'Praying Mantis': 20, 'Supernova Body Bomb': 25, 'Octopus Grip': 20, 'Flying Chokeslam': 15, 'Two Handed Gut Buster': 15, 'Shooting Star Spinning Kick': 25}

dictionary_gen_moves = {'Dropkick': 10, 'DDT': 5, 'Sharpshooter': 25, 'Moonsault': 20}

dictionary_weapons = {'Thumbtacks': 20, 'Steel Folding Chair': 10, 'Table': 10, 'Ladder': 25, 'Trash Can': 15, 'Barbed Wire Baseball Bat': 25, 'Handcuffs': 5, 'Kendo Sticks': 15,
                      'Sledgehammer': 20}


class Wrestler:
    """This is the beginning of a class for the wrestler"""

    def __init__(self, name, mass, sig_moves, fin_moves):
        # self.health = 120  # add a comment to this line to use option B
        # remove the comment from the following line to use option B
        self.health = dictionary_health[name]
        self.name = name
        self.mass = mass
        self.sig_moves = sig_moves
        self.fin_moves = fin_moves
        print("Your player name is: " + self.name + " and your health is at: " + str(self.health))


class Moves:
    """This is the beginning of a class for moves"""

    def __init__(self, name):
        self.gen_moves = gen_moves

class Weapons:
    """This is the beginning of a class for weapons"""

    def __init__(self, name):
        self.weapons = weapons

class Matches:
    """This is the beginning of a class for matches"""

    def __init__(self, name):
        self.stipulations = stipulations

class Payperviews:
    """This is the beginning of a class for the payperview"""

    def __init__(self, name):
        self.payperviews = payperviews

class Championships:
    """This is the beginning of a class for the championships"""

    def __init__(self, name):
        self.championships = championships 

def checkInput(someInput):
    print(str(len(someInput.strip())))
    return someInput

print("Hello")


wrestlers = {'Sanaa', 'Bidziil', 'Ishita', 'Hao', 'Adela', 'The Bionic Man'}
mass = {'Sanaa': 201, 'Bidziil': 190, 'Ishita': 205 , 'Hao': 182 , 'Adela': 180 , 'The Bionic Man': 290 }
sig_moves = {'Sanaa': "Spinning Crane Leg Kick", 'Bidziil': "Lunar Assault" , 'Ishita': "Sleeper Headlock" , 'Hao': "Elevated Elbow Smash", 'Adela': "Firework Neckbreaker", 'The Bionic Man': "Bionic Elbow Drop"}
fin_moves = {'Sanaa': "Praying Mantis", 'Bidziil': "Supernova Body Bomb" , 'Ishita': "Octopus Grip", 'Hao': "Flying Chokeslame", 'Adela': "Two-Handed Gut Buster", 'The Bionic Man': "Shooting Star Spinning Kick"}

print("\n\n")
print(wrestlers)
print("\n\n")
print(mass)
print("\n\n")
print(sig_moves)
print("\n\n")
print(fin_moves)
print("\n\n")

user_names = ["Sanaa", "Bidziil", "Ishita", "Hao", "Adela", "The Bionic Man"]
print(user_names)
user_response = ''
user_name = ''    

def validate(un, un_list):
    global user_name
    count = 0
    for list_item in un_list:
        if list_item.lower().strip() == un.lower().strip():
            del un_list[count]
            user_name = list_item
            return False
        count += 1
    return True

while validate(user_response, user_names):
    user_response = input("What champion name would you like to use? ")

champion = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(champion.mass)


while validate(user_response, user_names):
    user_response = input("What challenger name would you like to use? ")

challenger = Wrestler(user_name, mass[user_name], sig_moves[user_name], fin_moves[user_name])
print(challenger.mass)

gen_moves = ['Dropkick', 'DDT', 'Sharpshooter', 'Moonsault']
print("\n\n")
print(gen_moves)

genMove_names = ["Dropkick", "DDT","Sharpshooter", "Moonsault"]
user_response = ''
genMove_name = ''    

while validate(user_response, gen_moves):
    user_response = input("What generic move would your champion like to use? ")

while validate(user_response, gen_moves):
    user_response = input("What generic move would your challenger like to use? ")

print("the generic move name is: " + user_response + " -- " + genMove_name)
print(genMove_names)

weapons = {'Thumbtacks', 'Steel Folding Chair', 'Table', 'Ladder', 'Trash Can', 'Barbed Wire Baseball Bat', 'Handcuffs', 'Kendo Sticks', 'Sledgehammer'}
print("\n\n")
print(weapons)

weapons_names = ["Thumbtacks", "Steel Folding Chair","Table", "Ladder", "Trash Can", "Barbed Wire Baseball Bat", "Handcuffs", "Kendo Sticks", "Sledgehammer"]
user_response = ''
weapon_name = ''    

while validate(user_response, weapons_names):
    user_response = input("What weapon would your champion like to use? ")

while validate(user_response, weapons_names):
    user_response = input("What weapon would your challenger like to use? ")

print("the weapons name is: " + user_response + " -- " + weapon_name)
print(weapons_names)

stipulations = {'I Quit Match', 'Ladder Match', 'Pinfall Match', 'Submission Match', 'Pinfall Anywhere Match', 'Time Limit Match'}
print("\n\n")
print(stipulations)


stipulations_names = ["I Quit Match", "Ladder Match","Pinfall Match", "Submission Match", "Pinfall Anywhere Match", "Time Limit Match"]
user_response = ''
stipulation_name = ''    

while validate(user_response, stipulations_names):
    user_response = input("What stipulation would you like to have? ")

print("the stipulation name is: " + user_response + " -- " + stipulation_name)
print(stipulations_names)


payperviews = {'Lethal Ladders', 'Lethal World', 'Lethal Empire', 'Lethal Tournament', 'Heavyweight Tournement', 'Lightweight Tournement', 'Lethal Cage', 'Nothing Left to Lose'}
print("\n\n")
print(payperviews)

payperviews_names = ["Lethal Ladders", "Lethal World","Lethal Empire", "Lethal Tournament", "Heavyweight Tournement", "Lightweight Tournement", "Lethal Cage", "Nothing Left to Lose"]
user_response = ''
payperview_name = ''    

while validate(user_response, payperviews_names):
    user_response = input("What payperview would you like to fight at? ")

print("the payperview name is: " + user_response + " -- " + payperview_name)
print(payperviews_names)


championships = ['Lightweight Championship', 'Intercontinental Championship', 'Heavyweight Championship', 'Lethal Championship', 'Universal Championship', 'Ultimate Championship']
print("\n\n")
print(championships)

championships_names = ['Lightweight Championship', 'Intercontinental Championship', 'Heavyweight Championship', 'Lethal Championship', 'Universal Championship', 'Ultimate Championship']
user_response = ''

while validate(user_response, championships_names):
    user_response = input("What championship would you like to fight for?")

print("the championships name is: " + user_response + " -- ")

print(championships_names)

run = True

while run:
    ans = input("\n say something: ")
    print("your answer was: " + ans)

    if ans == 'quit':
        run = False

if champion.health == challenger.health:
    print("you have faught to a draw, congratulations")
elif(champion.health > challenger.health):
    print("Congratulations {}, you have vanquished {}!".format(champion.name, challenger.name))
else:
    print("Valiant effort {}, but {} has prevailed!".format(champion.name, challenger.name))

print("Goodbye!")
