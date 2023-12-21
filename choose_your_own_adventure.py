import random

random_number = random.randint(0, 11)


def start_adventure():
    name = input("Type in your name: ")
    print("Welcome", name, "to this adventure!")

    while True:
        answer = input("You are on a dirt road that is scary on the left and nice on the right, it has come to an end and you can either turn left or right: ").lower()

        if answer == "left":
            return encounter_river()
        elif answer == "right":
            return encounter_horse()
        else:
            print("Not a valid option.")

def encounter_river():
    while True:
        answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk around and 'swim' to swim across: ").lower()

        if answer == "swim":
            print("You encounter a hippo and it eats you. You lose!")
            return False
        elif answer == "walk":
            print("You walk for many miles and encounter a thief who kills you.")
            return False
        else:
            print("Not a valid option.")

def encounter_horse():
    while True:
        answer = input("You come to a long dirt road and find a horse tied to a tree. Choose 'travel' to travel or 'go back': ").lower()

        if answer == "travel":
            return encounter_stranger()
        elif answer == "go back":
            print("You go back to the start and find a stranger that kills you. You lose.")
            return False
        else:
            print("Not a valid option.")

def encounter_stranger():
    while True:
        answer = input("You travel down the long road and at the end of the road you find a stranger. Do you talk to them (Yes/No)? ").lower()
      
        if answer == "yes":
            print("You talk to the stranger and he gives you the chalice of wishes. You win!")
            return True
        elif answer == "no":
            print("The stranger kills you. You lose.")
            return False
        else:
            print("Not a valid option.")

# Start the game
start_adventure()
