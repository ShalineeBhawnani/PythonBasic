num = int(input("Enter a number: "))
def computer_guess(num):
    low = 1
    high = 100
    guess = 50
    if num not in range(0,101):
        print("Must be in range [1, 100]")
        return
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")
computer_guess(num)
