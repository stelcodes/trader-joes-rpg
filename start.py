import random
from datetime import datetime

#date/time info
now = datetime.now()
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
current_month = str(month_names[now.month - 1])
current_day = str(now.day)

#manager name generator
possible_names = ["Cedar", "Lavar", "Celik", "Zhenna", "Ivy", "Krysta", "Moonbeam", "Donna", "Sasha"]
def random_name():
    global possible_names
    chosen_name = random.choice(possible_names)
    possible_names.remove(chosen_name)
    return chosen_name

#food name generator
possible_foods = [["organic valencia peanut butter", "peanut butter"], ["ginger snap cookies", "cookie"], ["organic olive oil popcorn", "popcorn"], ["mochi ice cream balls", "ice cream"]] #[specific item, singular generic description]
chosen_food = random.choice(possible_foods)
def new_food():
    global possible_foods
    global chosen_food
    possible_foods.remove(chosen_food)
    chosen_food = random.choice(possible_foods)
    return

#class for all characters, including user
class Character:
    love = 0
    purpose = ""
    movie = ""
    age = 21
    def __init__(self, name):
        self.name = name
        self.love = 0
    def speak(self, message):
        print(self.name.upper() + ":")
        print(message + "\n")
        input()
    def ask(self, question):
        print(self.name.upper() + ":")
        print(question + "\n")
    def decide_speech(self, speech1, speech2):
        announce("decision!!")
        print("\"" + speech1 + "\" (1)\nOR\n\"" + speech2 + "\" (2)")
        line_break()
        self.decision = demand_decision()
        line_break()
    def decide_action(self, action1, action2):
        announce("decision!!")
        print("" + action1 + " (1)\nOR\n" + action2 + " (2)")
        line_break()
        self.decision = demand_decision()
        line_break()
    def love_update(self, n):
        self.love = self.love + n
        if (self.love > 10):
            self.love = 10
        elif (self.love < 1):
            self.love = 1
        announce("Your love meter is " + str(self.love) + " out of 10.")






#narration tools
def day_start():
    global day
    try:
        day += 1
    except:
        day = 1

def announce(announcement):
    print("** "+ announcement.upper() + " **")
    print("")
    input()

def get_fired():
    announce("YOU GOT FIRED.")
    end_screen()

#screen tools
def line_break():
    print("")

def refresh_screen():
    global day
    print("\033c")
    print(
    '''
     _______  ______    _______  ______   _______  ______          ___  _______  _______  __   _______
    |       ||    _ |  |   _   ||      | |       ||    _ |        |   ||       ||       ||  | |       |
    |_     _||   | ||  |  |_|  ||  _    ||    ___||   | ||        |   ||   _   ||    ___||__| |  _____|
      |   |  |   |_||_ |       || | |   ||   |___ |   |_||_       |   ||  | |  ||   |___      | |_____
      |   |  |    __  ||       || |_|   ||    ___||    __  |   ___|   ||  |_|  ||    ___|     |_____  |
      |   |  |   |  | ||   _   ||       ||   |___ |   |  | |  |       ||       ||   |___       _____| |
      |___|  |___|  |_||__| |__||______| |_______||___|  |_|  |_______||_______||_______|     |_______|

                                                 | {} |
      '''.format(sub_header()))
      #modular typeface

def sub_header():
    if day == 0:
        return "GAME OVER"
    else:
        return "DAY " + str(day)

def end_screen():
    global day
    day = 0
    refresh_screen()
    print(
    """
                           _______  __   __  _______  __    _  ___   _  _______
                          |       ||  | |  ||   _   ||  |  | ||   | | ||       |
                          |_     _||  |_|  ||  |_|  ||   |_| ||   |_| ||  _____|
                            |   |  |       ||       ||       ||      _|| |_____
                            |   |  |       ||       ||  _    ||     |_ |_____  |
                            |   |  |   _   ||   _   || | |   ||    _  | _____| |
                            |___|  |__| |__||__| |__||_|  |__||___| |_||_______|
                                         _______  _______  ______
                                        |       ||       ||    _ |
                                        |    ___||   _   ||   | ||
                                        |   |___ |  | |  ||   |_||_
                                        |    ___||  |_|  ||    __  |
                                        |   |    |       ||   |  | |
                                        |___|    |_______||___|  |_|
                           _______  ___      _______  __   __  ___   __    _  _______
                          |       ||   |    |   _   ||  | |  ||   | |  |  | ||       |
                          |    _  ||   |    |  |_|  ||  |_|  ||   | |   |_| ||    ___|
                          |   |_| ||   |    |       ||       ||   | |       ||   | __
                          |    ___||   |___ |       ||_     _||   | |  _    ||   ||  |
                          |   |    |       ||   _   |  |   |  |   | | | |   ||   |_| |
                          |___|    |_______||__| |__|  |___|  |___| |_|  |__||_______|


                                           Designed by Stel Abrego
                                         https://github.com/stelcodes

    """
    )
    quit()


#type safety functions
def demand_input():
    answer = input("> ")
    if answer == "":
        print("Try Again")
        answer = demand_input()
    return answer

def demand_int():
    answer = input("> ")
    try:
        answer = int(float(answer))
    except ValueError:
        print("Try Again")
        answer = demand_int()
    if answer < 10:
        print("Try Again")
        answer = demand_int()
    return int(float(answer))

def demand_decision():
    answer = input("> ")
    if (answer != "1") and (answer != "2"):
        print("Try Again")
        answer = demand_decision()
    return int(float(answer))




#set initial values
manager = Character(random_name())
coworker1 = Character(random_name())
coworker2 = Character(random_name())
user = Character("")

#begin simulation
day_start()
refresh_screen()
announce("Today, you begin working at Trader Joe's. Meet your new manager, " + manager.name + ".")
user.love_update(1)

#interview
manager.ask("What is your name?")
user.name = demand_input().title()
line_break()

manager.ask("Alright... What are you here to do?")
user.purpose = demand_input().lower()
line_break()

manager.ask("Fair enough.\nNow, what is your favorite movie genre?")
user.movie = demand_input().lower()
line_break()
manager.ask("Great! So you are " + user.name + " who is here to " + user.purpose + " and you like watching " + user.movie + " movies. Welcome to Trader Joe's. You'll fit right in.\nLooks like your first day will be " + current_month + " " + current_day + ".\nOh by the way, how old are you?")
user.age = demand_int()
line_break()

#manager's age reaction
if (user.age < 21):
    manager.speak("Whoa! I saw you sampling the Charles Shaw Zinfandel. That's highly illegal. You are fired, my young friend. I have no choice.")
    get_fired()
elif (user.age >= 21 and user.age < 30):
    manager.speak("Hey, I just turned 32 and I miss those days when I could eat as many organic brownies as I wanted. Sometimes you have to make sacrifices. You should come to one of our staff parties.")
    user.love_update(2)
else:
    manager.speak("You must be filled with wisdom with all those years under your belt.")
    user.love_update(1)

#segway
refresh_screen()
manager.speak("Ok, " + user.name + ". Let's meet your new teammates.")
announce("You and " + manager.name + " walk over to the wine aisles.")

#meet coworker1
coworker1.speak("Hi, my name is " + coworker1.name + ". My favorite ice cream is moosetracks and I use they/them. Nice to meet you.")
user.decide_speech("I love moosetracks too!", "I really don't like moosetracks but we can still be friends I guess.")

#coworker1 first impression
if user.decision == 1:
    coworker1.speak("Really? Moosetracks is kind of *my* thing around here. You better not step on my toes.")
    user.love_update(-2)
elif user.decision == 2:
    coworker1.speak("Haha, I like your attitude. I think we will be friends after all.")
    user.love_update(2)

#segway
manager.speak(coworker1.name + " is one of our resident wine experts, so don't be afraid to ask questions.")
refresh_screen()
coworker1.speak("Yeah! Don't be shy. I love talking about wine. I like drinking it even more!")
manager.speak("Haha... Don't we all. Alright, let's head into the back and I can show you where the inventory is done.")
announce("You and " + manager.name + " walk through the wine aisle, past the sample center, and through the big swinging doors on the back wall.")

#Meet coworker2
refresh_screen()
coworker2.speak("Oh my god!! A new friend!!")
user.decide_action("Embrace incoming ambush hug", "Go for the knuckle touch")

#coworker2 first impression
if user.decision == 1:
    announce("You and " + coworker2.name + " share a quick hug.")
    coworker2.speak("The sweet warmth of friendship!")
    user.love_update(1)
elif user.decision == 2:
    coworker2.speak("OW!!")
    coworker2.speak("*BREATHES HEAVILY*")
    coworker2.speak("You friggin' punched me in the chest, what was that??")
    manager.speak("Oh my god " + coworker2.name + ", are you alright?")
    coworker2.speak("I'll be fine but I think I need the rest of the day off to recover.")
    user.love_update(-3)

#shift activities
refresh_screen()
manager.speak("What an exciting first day! Anyway, let's get you started with stocking, " + user.name + ". Ooo look, it's a box of our " + chosen_food[0] + "! Yum yum.")
announce(manager.name + " shows you how to stock the shelves for an hour or so, and eventually you're able to do it yourself. Another hour goes by and " + manager.name + ", your manager, returns.")
manager.ask("I think that's enough for today, " + user.name + ". How do you think you did?")
self_eval = demand_input()
line_break()

#judgement
if user.love < 2:
    manager.speak("That's interesting.")
    announce("there is a long, awkward silence")
    manager.speak(user.name + ", I've got to keep it 100 with you. You are the slowest " + chosen_food[1] + " stocker I have ever trained. You only emptied one box in an hour,\nand you even put them on the wrong shelf. I'm not sure you're going to be a good fit here. \nWhy don't you just go home and not bother coming in tomorrow.")
    get_fired()
else:
    manager.speak("I think you did a great job. The " + chosen_food[1] + " section looks beautiful. \nYou're a friendly person, and I'm glad you're our new team member. See you tomorrow!")
    announce("day 1 completed")

#day 2
refresh_screen()


end_screen()
