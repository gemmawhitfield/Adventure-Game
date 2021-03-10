print("Welcome to Gemma's 'Choose Your Own Adventure' game!")
name = input("What is your name? ")
age = int(input("How old are you? "))

health = 10

if age >= 18:
    print("Congratulations " + name + ". You are old enough to play this game!")

    wants_to_play = input("Do you want to play? (Type 'yes' or 'no'): ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health points.")
        print("Okay " + name + " - let's play!")

        left_or_right = input("First choice... left or right? (Type left/right): ")
        if left_or_right == "left":
            ans = input("Nice, you walk down Bearwood Road and reach the Kings Head. Do you go in or around? (Type 'in' or 'around'): ")

            if ans == "around":
                print("You went around and walked to town.")
            elif ans == "in":
                print("You went inside The Kings Head and were spotted by the Bearwood chatterbox. You were talking for so long that you lost 5 health points. You left and walked to town.")
                health -= 5

            ans = input("You notice another pub and a canal. Which one do you go to (pub/canal)? ")
            if ans == "pub":
                print("You go to a pub on Broad Street and are greeted by one of the regulars... you accidentally knock his drink over and have a fight. You lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...goodbye.")
                else:
                    print("You survived! Congratulations, you win!")

            else:
                print("You fell in the canal and lost...")


        else:
            print("You fell down a manhole and lost...")

    else:
        print("Maybe next time...")
else:
    print("You are not old enough to play...")
