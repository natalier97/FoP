# # Write a program that prompts the user for an 
# integer that the player will try to guess. 
# If the player's guess is higher than the target integer, 
# the program should display "too high". 
# If the user's guess is lower than the target integer, 
# the program should display "too low". 
# The program should use a loop that repeats until the user 
# correctly guesses the integer. Then the program should print how many guesses it took.  
# When you run your program it should match the following format:

# # Enter the integer for the player to guess.
# # -12
# # Enter your guess.
# # 100
# # Too high - try again:
# # 50
# # Too high - try again:
# # -2000
# # Too low - try again:
# # -12
# # You guessed it in 4 tries.

# # If the user guesses the integer in 1 try, then your program should print "You guessed it in 1 try."

correct_integer = int(input('Enter the integer for the player to guess:'))
guess = int(input('enter your guess'))
count = 0

if correct_integer == guess:
    print('you guessed in 1 try')
while guess != correct_integer:
    if guess < correct_integer:
        print('too low-try again')
        guess = int(input('enter your guess again'))
        count += 1
    elif guess > correct_integer:
        print('too high, try again')
        guess = int(input('enter your guess again'))
        count += 1
if guess == correct_integer:
    count += 1
    print(f'you guessed in {count} tries')