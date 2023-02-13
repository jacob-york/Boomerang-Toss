from imports import *

def add_sound(function):
    """niche use only with kbchoice"""
    def inner(prompt, choices, clear_scrn=False, sound="None"):
        return_value = function(prompt, choices, clear_scrn)
        if sound != "None":
            audio.play(sound)
        return return_value
            
    return inner


kbinput = add_sound(kbinput)


def randomness():
    return random.randint(1,200)


def make_props(game_map):
    props = []
    prop_skins = ("._", "_.", "_ ", " _", "..", ".,", ",.", ",_", "  ")
    for x in range(PROP_CNT):
        props.append(Entity(random.choice(prop_skins), C(game_map.rwall, game_map.floor)))
    return props


def make_enemies(game_map):
    enemy_range = list(range(2, 24))
    enemies = []
    for x in range(settings[ENEMY_CNT][ACTIVE]):  # settings is a large 4D list for storing data
        y_pos = random.choice(enemy_range)
        enemies.append(Enemy(C(game_map.rwall, y_pos)))
        if settings[ENEMY_CNT][ACTIVE] <= 22:  # ***
            enemy_range.pop(enemy_range.index(y_pos))
    return enemies

def save(window, player, boomerang, props, enemies, background):
    with open("saves\\Save.bin", "wb") as save_file:
        for item in (window, player, boomerang, props, enemies, background):
            pickle.dump(item, save_file)


def load():
    with open("saves\\Save.bin", "rb") as save_file:
        window = pickle.load(save_file)
        player = pickle.load(save_file)
        boomerang = pickle.load(save_file)
        props = pickle.load(save_file)
        enemies = pickle.load(save_file)
        background = pickle.load(save_file)
    return window, player, boomerang, props, enemies, background  # this is the arbitrary order in which things are saved and loaded


def new_game():
    window = GameMap(MAP_HEIGHT, MAP_WIDTH, "  ")  # Each graphic/map coord is 2 chars long. This gives it a squarer look. Plus, you have more room for ascii art with 2 chars.
    player = Player(C(5, 4))
    boomerang = Boomerang(C(6, player.pos.y))

    # create enemies and props
    props = make_props(window)  # <-ground irregularities that help sell the illusion of forward movement.
    enemies = make_enemies(window)
    background = []
    return window, player, boomerang, props, enemies, background


def set_fps(fps):
    time.sleep(1/fps)


def get_simple_menu(menu_name):
    """reads {menu_name}.txt from file simple and returns it as a string."""
    with open("menus\\simple\\" + menu_name + ".txt", "r") as menu:
        return menu.read()


def get_static(menu_name):
    """menu_name's static as a string."""
    with open("menus\\complex\\" + menu_name + "\\Static.txt", "r") as static:
        return static.read()


def get_options(menu_name):
    """reads menu_name's Options.txt and returns a list of strings split by \n."""
    with open("menus\\complex\\" + menu_name + "\\Options.txt", "r") as options:
        return options.read().split("\n")


def complex_menu_input(menu_name, display="default"):
    options = get_options(menu_name)
    hl = 0
    choice_made = False
    while not choice_made:
        if display == "default":
            prompt = get_static(menu_name)
        else:
            prompt = display
        for option in range(len(options)):
            if hl == option:
                prompt = prompt.replace("|" + str(option) + "~", colors.paint(options[option], "negative"))
            else:
                prompt = prompt.replace("|" + str(option) + "~", options[option])

        keypress = kbinput(prompt, (k["w"], k["s"], k["<SPACE>"], k["<ENTER>"]))

        if keypress == k["w"]:
            audio.play(audio.menu_sound)
            if hl > 0:
                hl -= 1
            elif hl <= 0:
                hl = (len(options) - 1)
        elif keypress == k["s"]:
            audio.play(audio.menu_sound)
            if hl < (len(options) - 1):
                hl += 1
            elif hl >= (len(options) - 1):
                hl = 0
        
        if keypress == k["<SPACE>"] or keypress == k["<ENTER>"]:
            audio.play(audio.select)
            clear()
            choice_made = True

    return options[hl]


def settings_static(dynamic, saved):
    menu = ""
    menu += colors.paint("use <W>/<S> to highlight a setting, <E>/<D> to scale it.", "dark green") + "\n"
    menu += BOARDER + "\n"
    menu += dynamic + "\n"
    menu += BOARDER + "\n"
    menu += get_simple_menu("settings") + "\n"
    if not saved:
        menu += "\nyou have unsaved changes"
    elif saved:
        menu += "\n"
    menu += "\n"*49
    # menu += "\n"*30
    return menu
###########



def update_display(game_map, ent_list):
    game_map.refresh_self()
    for ent in ent_list:
        game_map.update_ent_pos(ent)
    print(game_map, end="", flush=True)


@catch_unexpected
def main():

    random.seed()

    new_game_called = False
    step = MAIN
    while step < QUIT:
        if step == MAIN:
            # TODO: re-implement "Personal Best"
            '''
            score_loc = (main_menu.index("best: ") + len("best: "))
            prev_score = int(main_menu[score_loc:(score_loc + 2)])
            '''
            menu_choice = complex_menu_input("main_menu")

            if menu_choice == "NEW GAME":
                window, player, boomerang, props, enemies, background = new_game()
                if not new_game_called:
                    new_game_called = True
                step = GAME
            elif menu_choice == "RESUME":
                if new_game_called:
                    step = GAME
                elif not new_game_called:
                    try:
                        window, player, boomerang, props, enemies, background = load()
                        step = GAME
                    except FileNotFoundError:
                        msg = "No save files found."
                        step = BACK
                # TODO: this is not very intuitive on the user end
            elif menu_choice == "HOW TO PLAY":
                msg = '''You'll have 60 seconds to earn a score of 5000 or more. If the timer runs out, you lose the game.\n
To earn points, use a high jump <SPACE> and a low jump <W> to position your player for boomerang throws.\n
When the boomerang hits a target, it will ricochet off of that target at an angle, letting you hit multiple targets with one throw!\n
To bounce the boomerange up, fire with <E>. To bounce it down, fire with <D>.\n
Single hits earn 50 [default] points, and any preceding hit with the same boomerang will earn double that.\n
Press <ESC> while playing to pause and unpause.'''
                step = BACK
            elif menu_choice == "SETTINGS":
                step = SETTINGS

            elif menu_choice == "EXIT":
                step = EXT_MENU
                
        elif step == SETTINGS:
            clear()
            # settings needs a unique input system, so the code in complex_menu_input() can't be re-used
            hl = 0
            saved = True
            custom = [settings[each_setting][ACTIVE] for each_setting in range(len(settings))]
            while step == SETTINGS:
                # draw the dynamic for settings
                settings_dynamic = "\n"
                for setting in range(len(settings)):
                    settings_dynamic += "\t"
                    if hl == setting:
                        settings_dynamic += colors.paint(f"{settings[setting][NAME]}: {custom[setting]}",
                                                         "negative")
                    else:
                        settings_dynamic += f"{settings[setting][NAME]}: {custom[setting]}"
                    settings_dynamic += "\n"
                settings_dynamic += "\n"

                keypress = kbinput(settings_static(settings_dynamic, saved),
                                   (k["w"], k["s"], k["e"], k["d"], k["r"], k["<SPACE>"], k["<ENTER>"], k["<ESC>"]),
                                   clear_scrn=False)

                if keypress == k["w"]:
                    audio.play(audio.settings_move)
                    if hl > 0:
                        hl -= 1
                    elif hl <= 0:
                        hl = (len(custom) - 1)
                elif keypress == k["s"]:
                    audio.play(audio.settings_move)
                    if hl < (len(custom) - 1):
                        hl += 1
                    elif hl >= (len(custom) - 1):
                        hl = 0
                    
                if keypress == k["e"]:
                    if custom[hl] < settings[hl][RANGE][MAX]:
                        if isinstance(custom[hl], float):
                            custom[hl] += .1
                        elif isinstance(custom[hl], int):
                            custom[hl] += 1
                        if saved:
                            saved = False
                    elif custom[hl] >= settings[hl][RANGE][MAX]:
                        audio.play(audio.negative)
                elif keypress == k["d"]:
                    if custom[hl] > settings[hl][RANGE][MIN]:
                        if isinstance(custom[hl], float):
                            custom[hl] -= .1
                        elif isinstance(custom[hl], int):
                            custom[hl] -= 1
                        if saved:
                            saved = False
                    elif custom[hl] <= settings[hl][RANGE][MIN]:
                        audio.play(audio.negative)

                if keypress == k["<SPACE>"] or keypress == k["<ENTER>"]:
                    audio.play(audio.select)

                    for each_setting in range(len(settings)):
                        settings[each_setting][ACTIVE] = custom[each_setting]

                    # I have ascended Python syntax
                    settings_str = "\n".join([
                        ",".join([
                            (
                                (
                                    "/".join([str(val) for val in datapoint])
                                ) if isinstance(datapoint, list) else str(datapoint)
                             ) for datapoint in setting
                        ]) for setting in settings
                    ])

                    with open("saves\\settings_data.cfg", "w") as settings_txt:
                        settings_txt.write(settings_str)
                    saved = True

                if keypress == k["r"] and custom[hl] != settings[hl][DEFAULT]:
                    audio.play(audio.menu_sound)
                    custom[hl] = settings[hl][DEFAULT]
                    if saved:
                        saved = False
                        
                if keypress == k["<ESC>"]:
                    audio.play(audio.select)
                    step = MAIN
                # TODO: Rounding Errors (ffs Python pls let me use decimals)
                
        elif step == BACK:
            clear()
            try:
                print(msg)
            except NameError:
                pass
            ans = kbinput(get_simple_menu("back"), (k["<SPACE>"], k["<ENTER>"], k["<ESC>"]), clear_scrn=True, sound=audio.select)
            step = MAIN
            # TODO: step should direct the user BACK to the previous menu step, as the name entails, not just send them to MAIN
                
        elif step == GAME:
            clock = 0
            while step == GAME:
                clock += 1
                if clock % settings[TICK_SPD][ACTIVE] == 0:
                    window.timer += 1

                if window.timer >= 60:
                    step = LOSE
                    continue
                if window.score >= 5000:
                    step = WIN
                    continue

                set_fps(settings[TICK_SPD][ACTIVE])
                key = randomness()

                # randomly "generated" background entities
                for prop in props:
                    if prop not in background and key == (props.index(prop) + 51):
                        prop.add(background)
                for enemy in enemies:
                    if enemy not in background and key == (enemies.index(enemy) + 1):
                        enemy.add(background)

                # respond to user keyboard interactions
                if msvcrt.kbhit():
                    keypress = ord(msvcrt.getwch())
                    if keypress == k["<SPACE>"] and player.touching_floor(window) and player.up_force == 0:
                        player.jump(BIG_JUMP)
                    if keypress == (k["w"] or k["W"]) and player.touching_floor(window) and player.up_force == 0:
                        player.jump(SMALL_JUMP)

                    if keypress == (k["e"] or k["E"]) and not boomerang.visible:
                        boomerang.aim_up = True
                        boomerang.pos.y = player.pos.y
                        boomerang.visible = True
                    if keypress == (k["d"] or k["D"]) and not boomerang.visible:
                        boomerang.aim_up = False
                        boomerang.pos.y = player.pos.y
                        boomerang.visible = True
                        
                    if keypress == k["<ESC>"]:
                        audio.play(audio.select)
                        clear()
                        update_display(window, background + [player, boomerang])
                        pausing_choice = complex_menu_input("pause", str(window) + "\n" + get_static("pause"))
                        if pausing_choice == "NEW GAME":
                            window, player, boomerang, props, enemies, background = new_game()
                            if not new_game_called:
                                new_game_called = True
                        elif pausing_choice == "SAVE AND EXIT":
                            msg = "Your game has been saved."
                            save(window, player, boomerang, props, enemies, background)
                            step = BACK
                        elif pausing_choice == "MAIN MENU":
                            step = MAIN
                            continue

                for ent in background:
                    
                    # move background
                    if not ent.touching_lwall(window):
                        ent.motion()
                    elif ent.touching_lwall(window):
                        ent.remove(background)
                        
                    # when an entity and a laser collide
                    if isinstance(ent, Enemy):
                        if ent.touching(boomerang):
                            ent.remove(background)
                            Effect("><", C(ent.pos.x, ent.pos.y), 1000).add(background)
                            audio.play(audio.hit_sound)
                            if boomerang.hit:
                                window.score += settings[KILL_POINTS][ACTIVE] * 2
                                if boomerang.down:
                                    boomerang.down = False
                                    boomerang.up = True
                                elif boomerang.up:
                                    boomerang.down = True
                                    boomerang.up = False
                            elif not boomerang.hit:
                                window.score += settings[KILL_POINTS][ACTIVE]
                                boomerang.hit = True
                                if boomerang.aim_up:
                                    boomerang.up = True
                                    boomerang.aim_up = None
                                elif not boomerang.aim_up:
                                    boomerang.down = True
                                    boomerang.aim_up = None

                # move player and laser
                player.motion(window)
                boomerang.motion(window, player)

                update_display(window, background + [player, boomerang])

        # win vs lose result screens
        elif step == WIN:
            clear()
            update_display(window, background + [player, boomerang])

            '''
            # update high score on main menu (a bit of a lazy implement but why not?)
            if prev_score > window.timer:
                main_menu = main_menu.replace(f"personal best: {prev_score} seconds", f"personal best: {window.timer} seconds")
                with open("menus\\main_menu.txt", "w") as mm_file:
                    mm_file.truncate()
                    mm_file.write(main_menu)
            '''

            print("\n")
            won_choice = complex_menu_input("you_win", str(window) + "\n" + get_static("you_win"))
            if won_choice == "PLAY AGAIN":
                window, player, boomerang, props, enemies, background = new_game()
                if not new_game_called:
                    new_game_called = True
                step = GAME
            elif won_choice == "MAIN MENU":
                step = MAIN

        elif step == LOSE:
            clear()
            update_display(window, background + [player, boomerang])
            print("\n")
            lost_choice = complex_menu_input("you_lose", str(window) + "\n" + get_static("you_lose"))
            if lost_choice == "PLAY AGAIN":
                window, player, boomerang, props, enemies, background = new_game()
                if not new_game_called:
                    new_game_called = True
                step = GAME
            elif lost_choice == "MAIN MENU":
                step = MAIN

        elif step == EXT_MENU:
            exit_choice = complex_menu_input("exit")
            if exit_choice == "MAIN MENU":
                step = MAIN
            elif exit_choice == "EXIT":
                step = QUIT


if __name__ == "__main__":
    main()
