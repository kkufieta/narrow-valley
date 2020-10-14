import time
import random

#<------------------------------------------------------------ Basic Functions ------------------------------------------------------------>    

def coin_flip():
	return random.choice(['heads', 'tails'])

def die_roll():
	return random.randint(1, 6)

def time_print(string):
    print(string)
    time.sleep(2)

def time_print_loop(lst):
    for element in lst:
        time_print(element)

def time_print_img(lst):
    for element in lst:
        print(element)
        time.sleep(.5)

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
    input("(Enter) to continue.\n")

#<------------------------------------------------------------ Fight System ------------------------------------------------------------>    

def intro_fight():    
    time_print('You are both still, waiting for the right time to make your move, and then...\n')


def choose_stats(items):
    opt1 = {
        'boss_hp': 15, 
        'player_hp': 15,
        'boss_name': 'Elijah'
        }
    opt2 = {
        'boss_hp': 15, 
        'player_hp': 15, 
        'boss_name': 'Clover',
        }
    if items['key'] == '*Primal Command*':
        items.update(opt1)
    else:
        items.update(opt2)
    return items

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

#<----- Fight Flow ----->

def pick_who_attacks(items):    
    result = coin_flip()
    if result == 'heads':
        player_turn(items)
    elif result == 'tails':
        boss_turn(items)

#<-------------------------------- Boss Functions -------------------------------->

def dont_run(items):
    lst = [
        "I will not give up!",
        "I'm not done yet!",
        "That won't stop me!",
        "I can do this!",
        "I'm not afraid!"
        ]
    time_print(f'''({items['player_name']}) "{random.choice(lst)}"\n''')
    pick_who_attacks(items)

def run(items):
    lst = [
        f"{items['player_name']} runs from {items['boss_name']}.", 
        "You live to fight another day and return to town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

def clover_attack_shout(items):
    lst = [
        f"{items['boss_name']} thrust her hands out tward you and shouts *Primal Command*!, as a torrent of earth, hail, and flames crash into you.",
        f"{items['boss_name']} shouts *Primal Command*! as a mass of stones, embers, and icy shards tornado around you, stricking you from every side.",
        f"{items['boss_name']} shouts *Primal Command*! and blast you with a tempest infused with firey ash, molten rock, and blistering steam."   
        ]
    time_print(random.choice(lst))

def clover_attacks(items):
    dmg = die_roll() + die_roll() 
    items['player_hp'] -= dmg
    clover_attack_shout(items)
    lst = [
        "",
        f"{items['boss_name']} hits you for {dmg} damage.", 
        f"your health is now at {items['player_hp']}",
        ""
        ]
    time_print_loop(lst)

def elijah_attack_shout(items):
    lst = [
        f"{items['boss_name']} shouts *Banishing Light*! as a massive beam of light stricks you from the sky.",
        f"Dark clouds start to break as {items['boss_name']} shouts *Banishing Light*! and a column of light blast you from above.",
        f"{items['boss_name']} chops his hand downward and shouts *Banishing Light*! as a pillar of light collides with you."
        ]
    time_print(random.choice(lst))

def elijah_attacks(items):
    dmg = die_roll() * 2 
    items['player_hp'] -= dmg
    elijah_attack_shout(items)
    lst = [
        "",
        f"{items['boss_name']} hits you for {dmg} damage.", 
        f"your health is now at {items['player_hp']}",
        ""
        ]
    time_print_loop(lst)

def boss_turn(items):    
    if items['boss_name'] == 'Clover':
        clover_attacks(items)
    else:
        elijah_attacks(items)
    if items['player_hp'] > 0:
        answer = valid_input('Continue fighting or run away?\n(1) Fight\n(2) Run\n', '1', '2')
        if answer == "1":
            dont_run(items)
        elif answer == "2":
            run(items)
    else:
        time_print('You have died!')
        play_again()
        
#<-------------------------------- Player Functions -------------------------------->

def player_attack_shout(items):
    lst = [
        f"{items['player_name']} bolts toward {items['boss_name']}, shouting {items['key']}!, as he rams {items['boss_name']} with a punishing strike.",
        f"With outstretched arms and palms aimed at {items['boss_name']}, {items['player_name']} shouts {items['key']}! and hammers {items['boss_name']} with a powerful blow.",
        f"Shouting {items['key']}!, {items['player_name']} releases a mighy force that smashes {items['boss_name']}."
        ]
    time_print(random.choice(lst))

def player_attack(items):
    if items['boss_name'] == 'Clover':
        dmg = die_roll() * 2
    else:
        dmg = die_roll() + die_roll() 
    items['boss_hp'] -= dmg
    player_attack_shout(items)
    lst = [
        "",
        f"You hit {items['boss_name']} for {dmg} damage points.",
        f"{items['boss_name']}'s health is now at {items['boss_hp']}",
        ""
        ]
    time_print_loop(lst)
    continue_on()

def boss_taunt(items):
    taunts = [
        "Not bad!",
        "Just a scratch!",
        "You're going to pay for that!",
        "That made me angry!",
        "That won't happen again!"
        ]
    time_print(f'''({items['boss_name']}) "{random.choice(taunts)}"\n''')

def winner_endings(items):
    time_print('You have Won!')
    if items['boss_name'] == 'Elijah':
        lst = [
            "Keeping your promise to Clover, you made the world safe from Elijah and his menacing.",
            "A new journey is in front of you.",
            f"Good people might need your assistance and the power of {items['key']}.",
            "You leave the narrow valley, never to return."
            ]
        time_print_loop(lst)
    elif items['boss_name'] == 'Clover':
        lst = [
            "You have completed the task given to you by Elijah and dispatched Clover.",
            "Attainment of *Primal Command* doubles your power and desire for more.",
            "You return to Elijah and plot with him to find more prey.",
            "You two leave the narrow valley, never to return."
            ]
        time_print_loop(lst)

def player_turn(items):
    player_attack(items)
    if items['boss_hp'] > 0:
        boss_taunt(items)
        pick_who_attacks(items)
    else:
        winner_endings(items)
        play_again()
            
        
        
#<----- Fight ----->

def fight(items):
    intro_fight()
    pick_who_attacks(choose_stats(items))

#<------------------------------------------------------------ Story ------------------------------------------------------------>

def title():
    lst = [
        "         ,--.",                                                                                                                           
        "       ,--.'|                                                                                       ,--,    ,--,",                        
        "   ,--,:  : |                                                                    ,---.            ,--.'|  ,--.'|",                        
        ",`--.'`|  ' :             __  ,-.  __  ,-.   ,---.           .---.              /__./|            |  | :  |  | :",                        
        "|   :  :  | |           ,' ,'/ /|,' ,'/ /|  '   ,'\         /. ./|         ,---.;  ; |            :  : '  :  : '",                        
        ":   |   \ | :  ,--.--.  '  | |' |'  | |' | /   /   |     .-'-. ' |        /___/ \  | |   ,--.--.  |  ' |  |  ' |      ,---.       .--,",  
        "|   : '  '; | /       \ |  |   ,'|  |   ,'.   ; ,. :    /___/ \: |        \   ;  \ ' |  /       \ '  | |  '  | |     /     \    /_ ./|",  
        "'   ' ;.    ;.--.  .-. |'  :  /  '  :  /  '   | |: : .-'.. '   ' .         \   \  \: | .--.  .-. ||  | :  |  | :    /    /  |, ' , ' :",  
        "|   | | \   | \__\/: . .|  | '   |  | '   '   | .; :/___/ \:     '          ;   \  ' .  \__\/: . .'  : |__'  : |__ .    ' / /___/ \: |",  
        "'   : |  ; .' ,' .--.; |;  : |   ;  : |   |   :    |.   \  ' .\  |           \   \   '  ,' .--.; ||  | '.'|  | '.'|'   ;   /|.  \  ' |",  
        "|   | '`--'  /  /  ,.  ||  , ;   |  , ;    \   \  /  \   \   ' \ |            \   `  ; /  /  ,.  |;  :    ;  :    ;'   |  / | \  ;   :",  
        "'   : |     ;  :   .'   \---'     ---'      `----'    \   \  |--'              :   \ |;  :   .'   \  ,   /|  ,   / |   :    |  \  \  ;",  
        ";   |.'     |  ,     .-./                              \   \ |                  '---' |  ,     .-./---`-'  ---`-'   \   \  /    :  \  \ ", 
        "'---'        `--`---'                                   '---'                          `--`---'                      `----'      \  ' ;", 
        "                                                                                                                                  `--`", 
                                                                                                                                    
        ]
    time_print_img(lst)

def get_name(items):
    items['player_name'] = input("To start enter your name\n")
    return items

def intro_story():
    lst = [
        "A brave warrior wonders the world in search of great power.",
        "their journey leads them to two sacred mountains divided by a village in a narrow valley.",
        ]
    time_print_loop(lst)
    lst = [
        "        __      /\                ",
        "       /  \    /  \_               /\ __         ",
        "      /    \  /\ '  \            _/  /  \     ",
        "     /\/\  /\/ :' __ \_      _ /   ^/_   `--.",
        "    /    \/  \  _/  \-'\    /   ^ _   \_ ^ .'\  ",
        "  /\  .-   `. \/     \ /''' `._ _/ \  ^ `_/   \_",
        " /  `-.__ `   / .-'.--\ ''' / ^  `--./ .-'  `- ^",
        "/        `.  / /       `.''' .-' ^    '-._ `._  `-",
        "                          ''' "
        ]
    time_print_img(lst)        
    lst = ["At the peak of each holy mountain a great master resides.",
        "One has conquered the forces of nature.",
        "The other manipulates spiritual energy.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        "           )            _     / \ ",
        "   /\    ( _   _._     / \   /^  \ ",
        "\ /  \    |_|-'_~_`-._/ ^ \ /  ^^ \ ",
        " \ /\/\_.-'-_~_-~_-~-_`-._^/  ^    \ ",
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
        "After a much needed rest at the village inn, our hero sets out.",
        ""
        ]
    time_print_loop(lst)
def get_location(items):
    lst = [
        f"What do you wan't to do {items['player_name']}?",
        "(1) Traverse the wooded mountain to the east.",
        "(2) Hike the snow covered mountain to the west."
        ]
    time_print_loop(lst)
    number = input("(3) Check bag.\n")
    return number

def check_bag(items):
    time_print(f"You have {items['key']} in you bag.\n")
    town(items)

#<----- Story Flow ----->

def town(items):
    choice = get_location(items)
    if choice == '1':
        clover(items)
    elif choice == '2':
        elijah(items)
    elif choice == '3':
        check_bag(items)
    else:
        town(items)

#<-------------------------------- Clover Functions -------------------------------->
def print_clover_house():
    lst = [
            "                                   /  \   .      ~         /\         `", 
            "  ~      /\      .            /\  /    \                  /`-\ ",
            "        /  \       `   /\    /^ \/  ^   \      /\  *     /  ^ \  .",
            "   .   / ^  \         / ^\  /  ^/  ^  )  \    /^ \      /  ^ ^ \ ",
            "      /`     \     ` /  ^ \/^ ^/^   (     \  /  ^ \    /      ^ \ ",
            "     /    ^   \~    / ^   /  ^/ ^ ^ ) ) ^  \/  ^^  \  / ^      `_\ ",
            "    /^  ^   `  \   / ^ ^   ^ / ^  (  ( ^   / ^   ^  \/`   ^       \ ",     
            "   /     ^ ^    \ /  ^ ^ ^^ / ^  (____) ^ /       ^ /     ^ ^   ^  \ ",
            "  /`   ^ ^  ^    \    ^  ^  ______|__|_____^ ^     / ^-    ^      ^ \ ",
            " / `'     ^     `-\     ^  /_______________\ ^ ^  / ^    ``     `-   \ ",
            "/     ^  ^^   ^   ^\^     /_________________\  ^ /  ^  ^^     ^       \ ", 
            "  -^ ^  ^ ^^-     ^ \^  ^  ||||||   |||__|||    /`-  ^  ^ ^^^   ^^-    \ ",       
            "        | |                ||||||I  |||__|||              | |    ",
            "||||||| [ ] |||||||||||||| ||||||___|||||||| |||||||||||| [ ] |||||||||| ", 
            '""""""""""""""""""""""""""""""""===="""""""""""""""""""""""""""""""""""""" ',
            "    |||||||||||||||||||||||||||=====|||||||||||||||||||||||||||||||| "   
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
        "     \_____/ ",      
        ]
    time_print_img(lst)

def clover_offer(items):
    print_clover_house()
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out to greet you.",
        "She peers curiously into you, sensing your kind heart...",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Clover) "{items['player_name']}, I am the master you seek."''',
        '''(Clover) "Train under me and unearth the secrets only I and Mother Nature know."''',
        "",
        "Will you accept her offer?"
        ]
    time_print_loop(lst)

def clover_not_home(items):
    lst = [
        "Clover isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

def clover_fight(items):
    print_clover_house()
    lst = [
        "Clover, brown-haired and slender, with bright, dark eyes, comes out to greet you.",
        f"She notices {items['key']} in your possession and understands why you have come.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        '''(Clover) "I will not be intimidated by one of Elijah's thugs!"''', 
        "Clover twirls her hands in the air, forming a bright green aura around herself.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    fight(items)

def clover_training(items):
    lst = [
        "For the next year you apprentice yourself to Clover, cultivating your skills.",
        "You pickup that a man named Elijah has been trying to steal Clover's power for many years.",
        "You promise Clover that you will bring an end to Elijah's reign of terror.",
        "Clover is touched by your commitment.",
        ""
        ]
    time_print_loop(lst)
    continue_on()           
    lst = [
        "To conclude your final day of training, Clover requests that you meet her infront of her house.",
        f'''(Clover) "{items['player_name']}, everything that you have endured was to prepare you for this."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    print_primal_command()
    lst = [
        '''(Clover) "*Primal Command* is my greatest weapon and now it is yours."''',
        f'''(Clover) "Remember your promise and good luck on your travels {items['player_name']}."''',
        ""
        ]
    time_print_loop(lst)
    items['key'] = '*Primal Command*'
    continue_on()
    lst = [
        "You recieve *Primal Command!*",
        "",
        "With the training from Clover and the power of *Primal Command*, you leave and head into town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

def clover_turned_down(items):
    lst = [
        '''(Clover) "I hope you will reconsider my offer." ''',
        "You leave the small house and return to town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

# <----- Clover Flow ----->

def clover(items):
    time_print("You find yourself in front of a small wooden house surrounded by tall grass and massive pine trees.")
    if items['key'] == '*Primal Command*':
        clover_not_home(items)
    elif items['key'] == '*Banishing Light*':
        clover_fight(items)
    else:
        clover_offer(items)
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            clover_training(items)
        elif answer == "2":
            clover_turned_down(items)

#<-------------------------------- Elijah Functions -------------------------------->

def print_elijah_house():
    lst = [
                
        "         .           .       (    )       *                *",
        "    *                          )  )",
        "        .                     (  (              .      /\ ",
        "                           .   (_)                    /  \  /\ ",
        "      *       *     ___________[_]___________      /\/    \/  \ ",
        "           /\      /\   *       ______    *  \    /   /\/\  /\/\ ",
        "          /  \    //_\          \    /\       \  /\/\/    \/    \ ",
        "   /\    / /\/\  //___\       *  \__/  \  .    \/       *",
        "  /  \  /\/*   \//_____\          \ |[]|        \ ",
        " /\/\/\/       //_______\          \|__|         \           .",
        "/   __ \      /XXXXXXXXXX\                        \       __",
        "   /  \ \    /_I_I___I__I_\________________________\     /  \ ",
        "  { () }       I_I   I__I_________[]_|_[]_________I     ( () )",
        "   (  )  /\    I_II  I__I_________[]_|_[]_________I      (  )",
        "    []  (  )   I I___I  I         XXXXXXX    /\   I       []",
        " ~~~[] ~~[] ~~~~~____~~~~~~~~~~~~~~~~~~~~~~~{  }~~~~~~~~~~[] ~~~~~",
        "          ~~~~~~_____~~~~~~~~~~      ~~~~~~~~[] ~~~~~~~~~"
        ]
    time_print_img(lst)

def print_banishing_light():
    lst = [
        "         ( ",    
        "   )    )\(   . ",
        "  (( `.((_))  )) ",
        "( ),\`.'    `-',' ",
        " `.)    /\    (,') ",
        " ,',   (  )   '._,) ",
        "((  )   ''   (`--' ",
        " `'( ) _--_,-.\ ' ",
        "  ' /,' \( )) `') ",
        "    (    `\( ",
        "           ) ",
        ""
        ]
    time_print_img(lst)

def elijah_offer(items):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes out to greet you.",
        "He sizes you up, feeling your desire for power...",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Elijah) "{items['player_name']}, I am the master you seek."''',
        '''(Elijah) "Take my guidence and uncover the limitless potential of the spirit relm."''',
        "",
        "Will you accept his offer?"
        ]
    time_print_loop(lst)

def elijah_not_home(items):
    lst = [
        "Elijah isn't home right now.",
        "There doesn't seem to be much to do here.",
        "You head back into town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

def elijah_fight(items):
    print_elijah_house()
    lst = [
        "Elijah, tall with powerful shoulders, and fierce blue eyes, comes out to greet you.",
        f"He smiles at you and begins to glow bright red as he notices you possess {items['key']}.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    lst = [
        f'''(Elijah) "I crave the power of {items['key']} and i will crush you to obtain it!"''', 
        "Elijah gets into a fighting stance.",
        ""
        ]
    time_print_loop(lst)
    continue_on()
    fight(items)

def elijah_training(items):
    lst = [
        "For the next year you memorize every mystical technique offerered to you by Elijah.",
        "Elijah shares his disire to increase his capabilities by defeating other masters and taking their power.",
        "He wants you to assist him and share the bounty, both of you becomming allpowerful.",
        "Elijah feels that with you, his dreams can be realized.",
        ""
        ]
    time_print_loop(lst)
    continue_on()    
    lst = [    
        "To conclude your final day of training, Elijah requests that you meet him infront of his house.",
        f'''(Elijah) "{items['player_name']}, everything that you have encountered has prepare you for this."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    print_banishing_light()
    lst = [
        '''(Elijah) "*Banishing Light* is my greatest technique and now it is yours."''',
        f'''(Elijah) "{items['player_name']}, I want you to defeat a master named Clover to the east and take her power.''',
        '''(Elijah) "Leave now and only return when you have completed your mission."''',
        ""
        ]
    time_print_loop(lst)
    continue_on()
    items['key'] = '*Banishing Light*'
    lst = [
        "You recieve *Banishing Light*",
        "",
        "With the training from Elijah and the power of *Banishing Light*, you leave and head into town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

def elijah_turned_down(items):
    lst = [
        '''(Elijah) - "I hope you will reconsider my offer." ''',
        "You leave the sizable log cabin and return to town.",
        ""
        ]
    time_print_loop(lst)
    town(items)

# <----- Elijah Flow ----->

def elijah(items):
    time_print("You find yourself in front of a sizable log cabin surrounded by odd stone sculpturs, both covered in snow.")
    if items['key'] == '*Banishing Light*':
        elijah_not_home(items)
    elif items['key'] == '*Primal Command*':
        elijah_fight(items)
    else:
        elijah_offer(items)
        answer = valid_input("(1) Yes\n(2) No\n", "1", "2")
        if answer == "1":
            elijah_training(items)
        elif answer == "2":
            elijah_turned_down(items)

#<----- Game Play / Items ----->

def play():
    items = {
    'key':'*Some old map*', 
    'player_name':''
    }
    title()
    get_name(items)
    intro_story()
    town(items)

#<----- Play ----->

play()

