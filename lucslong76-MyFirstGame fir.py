print("Hello player!!! Welcome to my first game. What is your name player?")
name = input("What is your name? ")

print("Hello", name, "I hope you enjoy my game!!!")

print("Now let us start with a question", name,"what is your age?")
age = int(input("What is you age? "))
print("Wow", name, "you are", age, "years old.")

health = 20

print("You begin the game with", health, "health")

if age >= 18:
  print("First off", name,"you ae old enough to play this game, congrats!")

  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Then Let's play.")

    left_or_right = input("Ok, good choice", name, "...your first decision is to go Left or Right. Which do you choose (left/right)? ")
    if left_or_right == "left":
        ans = input("Okay, follow the path to the woods...Do you enter the woods or go around (enter/around)? ")

        if ans == "enter":
          print("You enter the woods and continue the path. You find a sword in a stump.")

          pull_sword_from_stump = input("Do you pull sword from stump? ").lower()
          if pull_sword_from_stump == "yes":
            print("You pull the sword from the tree stump. You now have a sword...great succces!")

          else:
              print("You did not pull the sword from the stump. You are ambushed by a group of Nomes, you lose 10 health, along with your underwear and dignity.....SHAME.")
              health -= 10

          ans = input("You sheath your sword and look down the path and see a cottage and a airplane. Which do you walk to (cottage/airplane)? ")
          if ans == "cottage":
            print("You walk to the cottage and knock on the door. Do you open the door? ")

            open_the_door = input("Do you open the door? ").lower()
            if open_the_door == "yes":
              print("You grab and twist the door knob, opening the door. You walk in and see that it is empty. You claim the cottage as your new home. Congrats on being a new homeowner. You live a long and happy life in your new home. YOU WIN!!!!")

            else:
                print("You do not open the door and internally combust. You lose 10 health.")
                health -= 10

                if health <= 0:
                  print("You have zero health, you lose the game...game over.")
                else:
                    print("You have survived! As a bonus you win.")
          
          else:
              print("You walk towards the airplane. As you get close to the airplane you grab the keys in the cockpit. An alarm goes off and the airplane was really a robot and twists your body into a pretzel. You lose 10 health.")
              health -= 10

              if health <= 0:
                  print("You have zero health. You died and lost the game. What a loser.")
              else:
                  print("You survived, have a token that grants you an automatic win, hooray!")

          
        elif ans == "around":
            print("You try to go around the woods, but realize it never ends. You get lost and encounter a dragon on your journey. You are then eaten and die. YOU LOSE!")
       
    else:
        print("You immediaty turn to your right and trip on a rock. You split your head open. You lay gazing at the sky and think I should've gone left. You die, GAME OVER!!!")

  else:
      print("Oh, I see. Well I guess you can kick rocks")
    
else:
  print("Sorry", name, "you are not old enough to play, come back when you are older youngblood.")
