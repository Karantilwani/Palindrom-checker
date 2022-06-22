print("Hi There!, We're going to play Palindrome Game\n")
print("In this game you have to enter the word which will be exact same when you reverse it (Like DAD or MOM)\n","So Lets begin!!")

chance = 0

while chance < 3:
    word = input("Enter a word: ")
    r_word = word[::-1]
    if word == r_word:
        print("Congrats!! You Won")
        exit("Thanks for playing!!")
    else:
        print("Sorry you've lost\n")
        print("Wanna try again?")
        replay = input("Enter Yes or No: ")
        while replay != ("Yes" or "No"):
            if replay == "Yes":
                break
            if replay == "No":
                exit("Thanks for playing!!")
            else:
                print("Sorry wrong input!")
                replay = input("Please enter again: ")
    chance += 1