name = input("Type in your name: ")
print("welcome",  name, "to this adventure!")

answer  = input(" you are on a dirt road  that is scary on the left and nice on the rihgt , it has come to an end and you can either turn left or right? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim cross? type walk to walk around and swim to swim accross:  ")

    if answer == "swim":
        print(" you encounter a hippo and it eats you")

    elif answer == "walk":
        print("you walk for many miles and encounter a theif who kills you")
    else:
        print("not a valid option you lose ")
elif answer == "right":
    answer = input(" you come to a long dirt road and find a horse tied to a tree. travel/go back? : ")

    if answer == "travel":
        answer = input(" you travel down the long road and at the end of the road you find a stranger. do you talk to them  Yes/No? ")
      
        if answer == "Yes":
            print("you talk to the stranger and he give you the challice of wishes and you win ")
        elif answer == "No":
            print("the stranger kills you you lose ")
        else:
            print("not a valid option you lose ") 

    elif answer == "go back":
        print("you go back to the start and find a stranger that kills you, you lose .")
    else:
        print("not a valid option you lose ")
else:
    print("not a valid option. you lose")
