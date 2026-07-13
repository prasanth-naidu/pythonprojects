import random
pick_num = random.randint(1,100)
while True:
    guess = int(input("pick a num:"))
    if guess == pick_num:
        print("you cracked it!")
    elif guess < pick_num
        print("too low")
    else:
        print("too high")