import random
import monsterDef

# Action Definitions


def attack(attacker, defender):
    '''attacker attempts an attack on defender'''
    accuracy_result = random.randint(1, 20) + attacker.accuracy
    print(accuracy_result, "to hit.")
    if(accuracy_result >= defender.armor):
        defender.hp = defender.hp - attacker.damage


def escape():
    '''player attempts escape'''
    pass


def inventory():
    '''player opens inventory'''
    pass


def get_action():
    '''Recieves and returns player's action'''
    while True:
        action_input = input().lower()
        if(action_input == "attack"):
            return action_input
        elif(action_input == "escape"):
            return action_input
        elif(action_input == "inventory"):
            return action_input
        else:
            print("Invalid Action. Try again.")


def player_turn():
    print("---Player Turn---")
    print("Enter Action:")
    player_action = get_action()

    if(player_action == "attack"):
        pass
    elif(player_action == "escape"):
        pass
    elif(player_action == "inventory"):
        pass
    else:
        print("Error! This shouldn't have happened >.<")


def initiative():
    '''determines who takes the first action in combat'''
    pass


print("Giant Rat hp", monsterDef.GiantRat.hp)
attack(monsterDef.Skeleton, monsterDef.GiantRat)
print("Giant Rat hp", monsterDef.GiantRat.hp)

# Combat Loop


def combat_loop(creature1, creature2):
    '''combat loop'''
    pass
