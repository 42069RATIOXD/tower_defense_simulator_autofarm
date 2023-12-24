from Config import *

Towers_placed = 0
def Place_tower_1():

    global Towers_placed
    number_1_press()
    wait(0.02)
    number_1_unpress()
    wait(0.02)
    Click_at_random_thing_on_the_screen()
    wait(0.9)
    Placed_the_tower = Click_on_an_image('Tower Defense Simulator Stats Icon.png')
    if Placed_the_tower == True:
        Towers_placed = Towers_placed + 1
        print(Placed_the_tower)
        print("Placed a tower")
    wait(0.02)
    q_press()
    wait(0.02)
    q_unpress()
    wait(0.02)
    return Towers_placed

def Place_tower_1_with_upgrades():

    global Towers_placed
    number_1_press()
    wait(0.02)
    number_1_unpress()
    wait(0.02)
    Click_at_random_thing_on_the_screen()
    wait(1.2)
    Placed_the_tower = Click_on_an_image_specialized_for_upgrading('Tower Defense Simulator Stats Icon.png')
    if Placed_the_tower == True:
        Towers_placed = Towers_placed + 1
        print(Placed_the_tower)
        print("Placed a tower")
    wait(0.02)
    q_press()
    wait(0.02)
    q_unpress()
    wait(0.02)
    return Towers_placed

def Place_tower_1_with_upgrades_custom_militant():
    
    global Towers_placed
    number_1_press()
    wait(0.02)
    number_1_unpress()
    wait(0.02)
    Click_at_random_thing_on_the_screen()
    wait(1.6)
    Placed_the_tower = Click_on_an_image_specialized_for_upgrading_custom_militant('Tower Defense Simulator Stats Icon.png')
    if Placed_the_tower == True:
        Towers_placed = Towers_placed + 1
        print(Placed_the_tower)
        print("Placed a tower")
    wait(0.02)
    q_press()
    wait(0.02)
    q_unpress()
    wait(0.02)
    return Towers_placed

def Place_tower_2():

    global Towers_placed
    number_2_press()
    wait(0.02)
    number_2_unpress()
    wait(0.02)
    Click_at_random_thing_on_the_screen()
    wait(0.9)
    Placed_the_tower = Click_on_an_image('Tower Defense Simulator Stats Icon.png')
    if Placed_the_tower == True:
        Towers_placed = Towers_placed + 1
        print(Placed_the_tower)
        print("Placed a tower")
    wait(0.02)
    q_press()
    wait(0.02)
    q_unpress()
    wait(0.02)
    return Towers_placed

def Place_tower_2_with_upgrades():
    
    global Towers_placed
    number_2_press()
    wait(0.02)
    number_2_unpress()
    wait(0.02)
    Click_at_random_thing_on_the_screen()
    wait(1.2)
    Placed_the_tower = Click_on_an_image_specialized_for_upgrading('Tower Defense Simulator Stats Icon.png')
    if Placed_the_tower == True:
        Towers_placed = Towers_placed + 1
        print(Placed_the_tower)
        print("Placed a tower")
    wait(0.02)
    q_press()
    wait(0.02)
    q_unpress()
    wait(0.02)
    return Towers_placed