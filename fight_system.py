import time
import random

# <--------------- Basic Functions --------------->





def coin_flip():
    return random.choice(['heads', 'tails'])


def die_roll():
    return random.randint(1, 6)


def time_print(string):
    test_speed = .5
    play_speed = 2
    print(string)
    time.sleep(test_speed)


def time_print_loop(lst):
    for element in lst:
        time_print(element)


def time_print_img(lst):
    test_speed = .2
    play_speed = .5
    for element in lst:
        print(element)
        time.sleep(test_speed)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return option1
        if option2 in response:
            return option2
        else:
            time_print("I don't understand.")

def continue_on():
    input("Press (enter) to continue.\n")


# <--------------- Fight System --------------->


def intro_fight():
    time_print('You are both still, waiting for the right time to make your'
               ' move, and then...\n')


def choose_stats(game_data):
    opt1 = {
        'boss_hp': 18,
        'player_hp': 20,
        'boss_name': 'Elijah'
        }
    opt2 = {
        'boss_hp': 20,
        'player_hp': 18,
        'boss_name': 'Clover'
        }
    if game_data['bag'] == '*Primal Command*':
        game_data.update(opt1)
    else:
        game_data.update(opt2)
    return game_data


def play_again():
    time_print("Would you like to play again?")
    replay = valid_input("(1) Yes\n(2) No\n", "1", "2")
    if replay == "1":
        play()
    elif replay == "2":
        time_print("Ok, thanks for playing!")
        lst = [
            "",
            " ,----.                                 ,-----. ",
            "'  .-./    ,--,--.,--,--,--. ,---.     '  .-.  ',--.  ,--.,---. ,--.--. ",
            "|  | .---.' ,-.  ||        || .-. :    |  | |  | \  `'  /| .-. :|  .--' ",
            "'  '--'  |\ '-'  ||  |  |  |\   --.    '  '-'  '  \    / \   --.|  | ",
            " `------'  `--`--'`--`--`--' `----'     `-----'    `--'   `----'`--' ",
            ""
            ]
        time_print_img(lst)


# <----- Fight Flow ----->


def pick_who_attacks(game_data):
    result = coin_flip()
    if result == 'heads':
        player_turn(game_data)
    elif result == 'tails':
        boss_turn(game_data)


# <-------------------- Boss Functions -------------------->


def dont_run(game_data):
    lst = [
        "I will not give up!",
        "I'm not done yet!",
        "That won't stop me!",
        "I can do this!",
        "I'm not afraid!"
        ]
    time_print(f'''({game_data['player_name']}) "{random.choice(lst)}"\n''')
    pick_who_attacks(game_data)


def run(game_data):
    lst = [
        f"{game_data['player_name']} runs from {game_data['boss_name']}.",
        "You live to fight another day.",
        f"{game_data['player_name']} returns to town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


def clover_attack_shout(boss_name):
    lst = [
        f"{boss_name} thrust her hands out toward you and shouts"
        " *Primal Command*!, as a torrent of earth, hail, and flames"
        " crash into you.",
        f"{boss_name} shouts *Primal Command*! as a mass of stones,"
        " embers, and icy shards tornado around you, stiking you from every side.",
        f"{boss_name} shouts *Primal Command*! and blast you with a"
        " tempest infused with firey ash, molten rock, and blistering steam."
        ]
    time_print(random.choice(lst))


def clover_attacks(game_data):
    dmg = die_roll() + die_roll()
    game_data['player_hp'] -= dmg
    clover_attack_shout(game_data['boss_name'])
    lst = [
        "",
        f"{game_data['boss_name']} hits you for {dmg} damage.",
        f"your health is now at {game_data['player_hp']}",
        ""
        ]
    time_print_loop(lst)


def elijah_attack_shout(boss_name):
    lst = [
        f"{boss_name} shouts *Banishing Light*! as a massive beam"
        " of light strikes you from the sky.",
        f"Dark clouds part as {boss_name} shouts *Banishing Light*!"
        " and a column of light blasts you from above.",
        f"{boss_name} chops his hand downward and shouts *Banishing"
        " Light*! as a pillar of light collides with you."
        ]
    time_print(random.choice(lst))


def elijah_attacks(game_data):
    dmg = (die_roll() * 2) + 1
    game_data['player_hp'] -= dmg
    elijah_attack_shout(game_data['boss_name'])
    lst = [
        "",
        f"{game_data['boss_name']} hits you for {dmg} damage.",
        f"your health is now at {game_data['player_hp']}",
        ""
        ]
    time_print_loop(lst)


def boss_turn(game_data):
    if game_data['boss_name'] == 'Clover':
        clover_attacks(game_data)
    else:
        elijah_attacks(game_data)
    if game_data['player_hp'] > 0:
        answer = valid_input('Continue fighting or run away?\n(1) Fight\n(2)'
                             ' Run\n', '1', '2')
        if answer == "1":
            dont_run(game_data)
        elif answer == "2":
            run(game_data)
    else:
        time_print('You have died!')
        play_again()


# <-------------------- Player Functions -------------------->


def player_attack_shout(player_name, boss_name, special_item):
    lst = [
        f"{player_name} bolts toward {boss_name}, shouting"
        f" {special_item}!, and rams {boss_name} with a punishing strike.",
        f"With outstretched arms and palms aimed at {boss_name},"
        f" {player_name} shouts {special_item}! and hammers"
        f" {boss_name} with a powerful blow.",
        f"Shouting {special_item}!, {player_name} releases a migthy"
        f" force that smashes {boss_name}."
        ]
    time_print(random.choice(lst))


def player_attack(game_data):
    if game_data['boss_name'] == 'Clover':
        dmg = (die_roll() * 2) + 1
    else:
        dmg = die_roll() + die_roll()
    game_data['boss_hp'] -= dmg
    player_attack_shout(game_data['player_name'], game_data['boss_name'], game_data['bag'])
    lst = [
        "",
        f"You hit {game_data['boss_name']} for {dmg} damage points.",
        f"{game_data['boss_name']}'s health is now at {game_data['boss_hp']}",
        ""
        ]
    time_print_loop(lst)
    continue_on()


def boss_taunt(boss_name):
    taunts = [
        "Not bad!",
        "Just a scratch!",
        "You're going to pay for that!",
        "That made me angry!",
        "That won't happen again!"
        ]
    time_print(f'''({boss_name}) "{random.choice(taunts)}"\n''')


def winner_endings(boss_name, special_item):
    time_print('You have Won!')
    if boss_name == 'Elijah':
        lst = [
            "Keeping your promise to Clover, you made the world safe from"
            " Elijah and his menacing.",
            "A new journey is in front of you.",
            f"Good people might need your assistance and the power"
            f" of {special_item}.",
            "You leave the narrow valley, never to return."
            ]
        time_print_loop(lst)
    elif boss_name == 'Clover':
        lst = [
            "You have completed the task given to you by Elijah and"
            " dispatched Clover.",
            "Attainment of *Primal Command* doubles your power and desire"
            " for more.",
            "You return to Elijah and plot with him to find more prey.",
            "You two leave the narrow valley, never to return."
            ]
        time_print_loop(lst)


def player_turn(game_data):
    player_attack(game_data)
    if game_data['boss_hp'] > 0:
        boss_taunt(game_data['boss_name'])
        pick_who_attacks(game_data)
    else:
        winner_endings(game_data['boss_name'], game_data['bag'])
        play_again()


# <----- Fight ----->

game_data = {
        #'bag': '*Primal Command*',
        'bag': '*Banishing Light*',
        'player_name': 'Brian',

        }


def fight(game_data):
    intro_fight()
    pick_who_attacks(choose_stats(game_data))

fight(game_data)