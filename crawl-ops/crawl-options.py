import subprocess
import os

settings = {}

def save_options():
    string = ""
    for key in settings:
        string += "{}={}\n".format(key, settings[key])
    file = open("../crawl-ref/settings/init.txt", 'w')
    file.write(string)
    file.close()
    print("Options saved successfully!")

def change_options():
    while True:
        print("\nChoose a category:\n1: Starting Screen\nX: Go back to main menu")
        selection = input().strip()
        if selection == '1':
            starting_screen_options()
        elif selection == 'x' or selection == 'X':
            return
        else:
            print("Invalid selection! Please try again.")

def starting_screen_options():
    while True:
        print("\nSelect an option:\n1: name\n2: type\n3: restart_after_game\n4: game_seed\nX: Go back")
        selection = input().strip()
        if selection == '1':
            change_name()
        elif selection == '2':
            change_type()
        elif selection == '3':
            change_restart_after_game()
        elif selection == '4':
            change_game_seed()
        elif selection == 'x' or selection == 'X':
            return
        else:
            print("Invalid selection! Please try again.")

def change_name():
    print("\nOption: name\nDefault: \nDesc: If set, that's the name all your Crawl characters will get. Setting this will bypass the main menu by default; see `name_bypasses_menu`.")
    print("Submit nothing to go back.")
    print("Submit an option: ")
    op = input().strip()
    if op == '':
        return
    settings['name'] = op

def change_type():
    print("\nOption: name\nDefault: normal\nDesc: Choose a game type. Valid values are \"normal\", \"seeded\", \"tutorial\", \"arena\", \"sprint\", \"descent\", and \"hints\". If explicitly set (not just left to the default), this sets the default game type at the main menu. If the main menu is bypassed (e.g. by setting `name`), this option can be used to determine the game type.")
    print("Submit nothing to go back.")
    while True:
        print("Submit an option: ")
        op = input().strip()
        if op == '':
            return
        if op not in ["normal", "seeded", "tutorial", "arena", "sprint", "descent", "hints"]:
            print("Invalid submission! Try again.")
            continue
        settings['type'] = op
        break
    
def change_restart_after_game():
    print("\nOption: name\nDefault: normal\nDesc: When set to true, at the game end, crawl will return to the main menu. If set to maybe, crawl will return to the main menu only if the startup options don't bypass the main menu, otherwise it will exit. If set to false, it will exit unconditionally. This option is set to true for local tiles builds by default, and maybe by default for other builds. This option is ignored for online games.")
    print("Submit nothing to go back.")
    while True:
        print("Submit an option: ")
        op = input().strip()
        if op == '':
            return
        if op not in ["true", "maybe", "false"]:
            print("Invalid submission! Try again.")
            continue
        settings['restart_after_game'] = op
        break
    
def change_game_seed():
    print("\nOption: name\nDefault: \nDesc: A number indicating the seed to initialize the random number generator from. Within certain limits, the same seed will deterministically lead to the same dungeon. If set to \"none\" or 0, the seed will be chosen randomly. This can also be set directly via the command line with \"-seed\", which will override any rc file setting. This value is an unsigned 64 bit integer.")
    print("Submit nothing to go back.")
    while True:
        print("Submit an option: ")
        op = input().strip()
        if op == '':
            return
        if not op.isnumeric():
            print("Invalid submission! Must be a number. Try again.")
            continue
        settings['game_seed'] = op
        break

def run_game():
    process = subprocess.Popen(['../crawl-ref/source/crawl'], stdout=subprocess.PIPE)
    process.wait()

print("Welcome to the Dungeon Crawl: Stone Soup Options Editor Prototype!")
print("This is a prototype for implementing a configurable options menu into DC:SS.")

while(True):
    print("\nMake a selection:\n1: Change options\n2: Save options\n3: Run game\nX: Quit")
    selection = input().strip()
    if selection == '1':
        change_options()
    elif selection == '2':
        save_options()
    elif selection == '3':
        run_game()
    elif selection == 'x' or selection == 'X':
        break
    else:
        print("Invalid selection! Please try again.")
