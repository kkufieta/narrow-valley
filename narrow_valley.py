import time
import random
import sys

# <--------------- Basic Functions --------------->
PLAY_SPEED_TEXT = 2
PLAY_SPEED_IMAGE = 0.5


def coin_flip():
    return random.choice(['heads', 'tails'])


def die_roll():
    return random.randint(1, 6)


def time_print(string):
    print(string)
    time.sleep(PLAY_SPEED_TEXT)


def time_print_loop(lst):
    for element in lst:
        time_print(element)


def time_print_img(lst):
    for element in lst:
        print(element)
        time.sleep(PLAY_SPEED_IMAGE)


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
            "'  .-./    ,--,--.,--,--,--. ,---.   "
            "  '  .-.  ',--.  ,--.,---. ,--.--. ",
            "|  | .---.' ,-.  ||        || .-. :  "
            "  |  | |  | \\  `'  /| .-. :|  .--' ",
            "'  '--'  |\\ '-'  ||  |  |  |\\   --.  "
            "  '  '-'  '  \\    / \\   --.|  | ",
            " `------'  `--`--'`--`--`--' `----'  "
            "   `-----'    `--'   `----'`--' ",
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
        " embers, and icy shards tornado around you, stiking you"
        " from every side.",
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
    player_attack_shout(game_data['player_name'],
                        game_data['boss_name'], game_data['bag'])
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
            "You leave the narrow valley, never to return.",
            ""
            ]
        time_print_loop(lst)
    elif boss_name == 'Clover':
        lst = [
            "You have completed the task given to you by Elijah and"
            " dispatched Clover.",
            "Attainment of *Primal Command* doubles your power and desire"
            " for more.",
            "You return to Elijah and plot with him to find more prey.",
            "You two leave the narrow valley, never to return.",
            ""
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


def fight(game_data):
    intro_fight()
    pick_who_attacks(choose_stats(game_data))


# <--------------- Story --------------->


def title():  # Says Narrow Valley in ascii
    lst = [
        "         ,--.",
        "       ,--.'|                                                     "
        "                                  ,--,    ,--,",
        "   ,--,:  : |                                                     "
        "               ,---.            ,--.'|  ,--.'|",
        ",`--.'`|  ' :             __  ,-.  __  ,-.   ,---.           .---. "
        "             /__./|            |  | :  |  | :",
        "|   :  :  | |           ,' ,'/ /|,' ,'/ /|  '   ,'\\         /. ./| "
        "        ,---.;  ; |            :  : '  :  : '",
        ":   |   \\ | :  ,--.--.  '  | |' |'  | |' | /   /   |     .-'-. ' | "
        "       /___/ \\  | |   ,--.--.  |  ' |  |  ' |      ,---.       .--,",
        "|   : '  '; | /       \\ |  |   ,'|  |   ,'.   ; ,. :    /___/ \\: | "
        "       \\   ;  \\ ' |  /       \\ '  | |  '  | |     /     \\  "
        "  /_ ./|",
        "'   ' ;.    ;.--.  .-. |'  :  /  '  :  /  '   | |: : .-'.. '   ' . "
        "        \\   \\  \\: | .--.  .-. ||  | :  |  | :  "
        "  /    /  |, ' , ' :",
        "|   | | \\   | \\__\\/: . .|  | '   |  | '   ' "
        "  | .; :/___/ \\:     ' "
        "         ;   \\  ' .  \\__\\/: . .'  : |__'  : |__ . "
        "   ' / /___/ \\: |",
        "'   : |  ; .' ,' .--.; |;  : |   ;  : |   | "
        "  :    |.   \\  ' .\\  | "
        "          \\   \\   '  ,' .--.; ||  | '.'|  | '.'|' "
        "  ;   /|.  \\  ' |",
        "|   | '`--'  /  /  ,.  ||  , ;   |  , ;  "
        "  \\   \\  /  \\   \\   ' \\ | "
        "           \\   `  ; /  /  ,.  |;  :    ;  :  "
        "  ;'   |  / | \\  ;   :",
        "'   : |     ;  :   .'   \\---'     ---'      `----'    \\   \\  |--' "
        "             :   \\ |;  :   .'   \\  ,   /|  , "
        "  / |   :    |  \\  \\  ;",
        ";   |.'     |  ,     .-./    "
        "                          \\   \\ |      "
        "            '---' |  ,     .-./---`-'  ---`-' "
        "  \\   \\  /    :  \\  \\ ",
        "'---'        `--`---'                                   '---'      "
        "                    `--`---'            "
        "          `----'      \\  ' ;",
        "                                                                    "
        "                                                              `--`",

        ]
    time_print_img(lst)


def get_name(game_data):
    game_data['player_name'] = input("To start enter your name\n")
    return game_data


def intro_story():
    lst = [
        "A brave warrior wanders the world in search of great power.",
        "Their journey leads them to two sacred mountains divided by a"
        " village in a narrow valley.",
        ]
    time_print_loop(lst)
    lst = [
        "        __      /\\                ",
        "       /  \\    /  \\_                /\\__   ",
        "      /    \\  /\\ /  \\            _/  /  \\     ",
        "     /\\/\\  /\\/ :' __ \\_      _ /   ^/_   `--.",
        "    /    \\/  \\  _/  \\-'\\    /   ^ _   \\_ ^ .'\\  ",
        "  /\\  .-   `. \\/     \\ /''' `._ _/ \\  ^ `_/   \\_",
        " /  `-.__ `   / .-'.--\\ ''' / ^  `--./ .-'  `- ^",
        "/        `.  / /       `.''' .-' ^    '-._ `._  `-",
        "                          ''' "
        ]
    time_print_img(lst)
    lst = [
        "At the peak of each holy mountain a great master resides.",
        "One has conquered the forces of nature.",
        "The other manipulates spiritual energy.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        "           )            _     / \\ ",
        "   /\\    ( _   _._     / \\   /^  \\ ",
        "\\ /  \\    |_|-'_~_`-._/ ^ \\ /  ^^ \\ ",
        " \\ /\\/\\_.-'-_~_-~_-~-_`-._^/  ^    \\ ",
        "   _.-'_~-_~-_-~-_~_~-_~-_`-._   ^ ",
        "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "    |  [ ]   [ ]  [ ]   [ ] |",
        "    |   ___     __    ___   |   ",
        "    |  [___]   | .|  [___]  |  <inn>",
        "    |________  |__|  _______|    |",
        "^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^|^^ ",
        "          ^^^^^ === ^^^^^^      ^^^   "
        ]
    time_print_img(lst)
    lst = [
        "After a much-needed rest at the village inn, our hero sets out.",
        ""
        ]
    time_print_loop(lst)


def get_location(player_name):
    lst = [
        f"What do you want to do {player_name}?",
        "(1) Traverse the wooded mountain to the east.",
        "(2) Hike the snow-covered mountain to the west."
        ]
    time_print_loop(lst)
    number = input("(3) Check bag.\n")
    return number


def check_bag(game_data):
    time_print(f"You have {game_data['bag']} in your bag.\n")
    town(game_data)


# <----- Story Flow ----->


def town(game_data):
    choice = get_location(game_data['player_name'])
    if choice == '1':
        clover(game_data)
    elif choice == '2':
        elijah(game_data)
    elif choice == '3':
        check_bag(game_data)
    else:
        town(game_data)


# <-------------------- Clover Functions -------------------->


def print_clover_house():
    lst = [
            "                                 "
            "  /  \\   .      ~         /\\         `",
            "  ~      /\\      .            /\\ "
            " /    \\                  /`-\\ ",
            "        /  \\       `   /\\  "
            "  /^ \\/  ^   \\      /\\  *     /  ^ \\  .",
            "   .   / ^  \\         / ^\\ "
            " /  ^/  ^  )  \\    /^ \\      /  ^ ^ \\ ",
            "      /`     \\     ` /  ^ \\/^ ^/^   (  "
            "   \\  /  ^ \\    /      ^ \\ ",
            "     /    ^   \\~    / ^   /  ^/ ^ ^ ) ) ^ "
            " \\/  ^^  \\  / ^      `_\\ ",
            "    /^  ^   `  \\   / ^ ^   ^ / ^  (  ( ^  "
            " / ^   ^  \\/`   ^       \\ ",
            "   /     ^ ^    \\ /  ^ ^ ^^ / ^  (____) ^ / "
            "      ^ /     ^ ^   ^  \\ ",
            "  /`   ^ ^  ^    \\    ^  ^  ______|__|_____^ ^ "
            "    / ^-    ^      ^ \\ ",
            " / `'     ^     `-\\     ^  /_______________\\ ^ ^ "
            " / ^    ``     `-   \\ ",
            "/     ^  ^^   ^   ^\\^     /_________________\\  ^ / "
            " ^  ^^     ^       \\ ",
            "  -^ ^  ^ ^^-     ^ \\^  ^  ||||||   |||__|||    /`-  ^  ^ ^^^ "
            "  ^^-    \\ ",
            "        | |                ||||||I  |||__|||             "
            " | |    ",
            "||||||| [ ] |||||||||||||| ||||||___|||||||| |||||||||||| [ ]"
            " |||||||||| ",
            '""""""""""""""""""""""""""""""""===="""""""""""""""""""""""""'
            '""""""""""""" ',
            "    |||||||||||||||||||||||||||=====|||||||||||||||||||||||||"
            "||||||| "
            ]
    time_print_img(lst)


def print_primal_command():
    lst = [
        "       ... ",
        "    :::;(;::: ",
        " .::;.) );:::::. ",
        ":::;`(,' (,;::::: ",
        ":::;;) .-. (';::: ",
        ":::;( ( * )'):;:: ",
        "'::;`),'-' (;::' ",
        "  ':(____),_)::' ",
        "    |_______| ",
        "     \\_____/ ",
        ]
    time_print_img(lst)


def clover_offer(player_name):
    print_clover_house()
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out"
        " to greet you.",
        "She peers curiously into you, sensing your kind heart...",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Clover) "{player_name}, I am the master you seek."''',
        '''(Clover) "Train under me and unearth the secrets only I and'''
        ''' Mother Nature know."''',
        "",
        "Will you accept her offer?"
        ]
    time_print_loop(lst)


def clover_not_home(game_data):
    lst = [
        "Clover isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


def clover_fight(game_data):
    print_clover_house()
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out"
        " to greet you.",
        f"She notices {game_data['bag']} in your possession and"
        " understands why"
        " you have come.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        '''(Clover) "I will not be intimidated by one of Elijah's'''
        ''' thugs!"''',
        "Clover twirls her hands in the air, forming a bright green aura"
        " around herself.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    fight(game_data)


def clover_training(game_data):
    lst = [
        "For the next year, you apprentice yourself to Clover, cultivating"
        " your skills.",
        "You pick up that a man named Elijah has been trying to steal Clover's"
        " power for many years.",
        "You promise Clover that you will bring an end to Elijah's reign of"
        " terror.",
        "Clover is touched by your commitment.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        "To conclude your final day of training, Clover requests that you"
        " meet her in front of her house.",
        f'''(Clover) "{game_data['player_name']}, everything that you have'''
        ''' endured was to prepare you for this."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    print_primal_command()
    lst = [
        '''(Clover) "*Primal Command* is my greatest weapon and now it is'''
        ''' yours."''',
        '''(Clover) "Remember your promise and good luck on your travels'''
        f''' {game_data['player_name']}."''',
        ""
        ]
    time_print_loop(lst)
    game_data['bag'] = '*Primal Command*'
    continue_on()
    lst = [
        "You receive *Primal Command!*",
        "",
        "With the training from Clover and the power of *Primal Command*, you"
        " leave and head into town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


def clover_turned_down(game_data):
    lst = [
        '''(Clover) "I hope you will reconsider my offer."''',
        "You leave the small house and return to town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


# <----- Clover Flow ----->


def clover(game_data):
    time_print("You find yourself in front of a small wooden house surrounded"
               " by tall grass and massive pine trees.")
    if game_data['bag'] == '*Primal Command*':
        clover_not_home(game_data)
    elif game_data['bag'] == '*Banishing Light*':
        clover_fight(game_data)
    else:
        clover_offer(game_data['player_name'])
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            clover_training(game_data)
        elif answer == "2":
            clover_turned_down(game_data)


# <-------------------- Elijah Functions -------------------->


def print_elijah_house():
    lst = [

        "         .           .       (    )       *                *",
        "    *                          )  )",
        "        .                     (  (              .      /\\ ",
        "                           .   (_)                    /  \\  /\\ ",
        "      *       *     ___________[_]___________      /\\/    \\/  \\ ",
        "           /\\      /\\   *       ______    *  \\  "
        "  /   /\\/\\  /\\/\\ ",
        "          /  \\    //_\\          \\    /\\       \\ "
        " /\\/\\/    \\/    \\ ",
        "   /\\    / /\\/\\  //___\\       *  \\__/  \\  .  "
        "  \\/       *",
        "  /  \\  /\\/*   \\//_____\\          \\ |[]|        \\ ",
        " /\\/\\/\\/       //_______\\          \\|__|         \\  "
        "         .",
        "/   __ \\      /XXXXXXXXXX\\                        \\       __",
        "   /  \\ \\    /_I_I___I__I_\\________________________\\     /  \\ ",
        "  { () }       I_I   I__I_________[]_|_[]_________I     ( () )",
        "   (  )  /\\    I_II  I__I_________[]_|_[]_________I      (  )",
        "    []  (  )   I I___I  I         XXXXXXX    /\\   I       []",
        " ~~~[] ~~[] ~~~~~____~~~~~~~~~~~~~~~~~~~~~~~{  }~~~~~~~~~~[] ~~~~~",
        "          ~~~~~~_____~~~~~~~~~~~~~~~~~~~~~~~~[] ~~~~~~~~~"
        ]
    time_print_img(lst)


def print_banishing_light():
    lst = [
        "         ( ",
        "   )    )\\(   . ",
        "  (( `.((_))  )) ",
        "( ),\\`.'    `-',' ",
        " `.)    /\\    (,') ",
        " ,',   (  )   '._,) ",
        "((  )   ''   (`--' ",
        " `'( ) _--_,-.\\ ' ",
        "  ' /,' \\( )) `') ",
        "    (    `\\( ",
        "           ) ",
        ""
        ]
    time_print_img(lst)


def elijah_offer(player_name):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes"
        " out to greet you.",
        "He sizes you up, feeling your desire for power...",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Elijah) "{player_name}, I am the master you seek."''',
        '''(Elijah) "Take my guidance and uncover the limitless potential'''
        ''' of the spirit realm."''',
        "",
        "Will you accept his offer?"
        ]
    time_print_loop(lst)


def elijah_not_home(game_data):
    lst = [
        "Elijah isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


def elijah_fight(game_data):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes"
        " out to greet you.",
        "He smiles at you and begins to form a bright red aura around"
        " himself as he notices you"
        f" possess {game_data['bag']}.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Elijah) "I crave the power of {game_data['bag']} '''
        '''and I will crush you to obtain it!"''',
        "Elijah gets into a fighting stance.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    fight(game_data)


def elijah_training(game_data):
    lst = [
        "For the next year, you memorize every mystical technique offered to"
        " you by Elijah.",
        "Elijah shares his desire to increase his capabilities by defeating"
        " other masters and taking their power.",
        "He wants you to assist him and share the bounty, both of you becoming"
        " all-powerful.",
        "Elijah feels that with you, his dreams can be realized.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        "To conclude your final day of training, Elijah requests that you meet"
        " him in front of his house.",
        f'''(Elijah) "{game_data['player_name']}, everything that you have'''
        ''' encountered has prepared you for this."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    print_banishing_light()
    lst = [
        '''(Elijah) "*Banishing Light* is my greatest technique and now it '''
        '''is yours."''',
        f'''(Elijah) "{game_data['player_name']}, I want you to'''
        ''' defeat a master'''
        ''' named Clover to the east and take her power.''',
        '''(Elijah) "Leave now and only return when you have completed your'''
        ''' mission."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    game_data['bag'] = '*Banishing Light*'
    lst = [
        "You receive *Banishing Light*",
        "",
        "With the training from Elijah and the power of *Banishing Light*, you"
        " leave and head into town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


def elijah_turned_down(game_data):
    lst = [
        '''(Elijah) "I hope you will reconsider my offer." ''',
        "You leave the sizable log cabin and return to town.",
        ""
        ]
    time_print_loop(lst)
    town(game_data)


# <----- Elijah Flow ----->


def elijah(game_data):
    time_print("You find yourself in front of a sizable log cabin surrounded"
               " by odd stone sculptures, both covered in snow.")
    if game_data['bag'] == '*Banishing Light*':
        elijah_not_home(game_data)
    elif game_data['bag'] == '*Primal Command*':
        elijah_fight(game_data)
    else:
        elijah_offer(game_data['player_name'])
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            elijah_training(game_data)
        elif answer == "2":
            elijah_turned_down(game_data)


# <----- Game Play / game_data ----->


# game_data holds important stats for the game.


def play():
    game_data = {
        'bag': 'dust and a few crumbs',
        'player_name': None,
        'boss_hp': None,
        'player_hp': None,
        'boss_name': None
        }
    title()
    get_name(game_data)
    intro_story()
    town(game_data)


# <----- Play ----->


if __name__ == '__main__':
    if len(sys.argv) > 1:
        PLAY_SPEED_TEXT = float(sys.argv[1])
        PLAY_SPEED_IMAGE = float(sys.argv[1]) * 0.25
    play()
