import random


while True:
    upper_numb = (input("Please type the upper bound number. "))
    if upper_numb.isdigit():
        print("Let's start the guessing game!!")
        upper_numb = int(upper_numb)
        break
    else:
        print("Please enter a valid number!")

random_numb = random.randint(1, int(upper_numb))
user_guess = int(input(f"Please guess a number between 1 and {upper_numb}: "))
attempt_taken = 1


while user_guess != random_numb:
  
  if user_guess > random_numb:
    print("You need to guess a lower number.")  
    attempt_taken +=1
    user_guess = int(input(f"Please guess a number between 1 and {upper_numb}: "))
  elif user_guess < random_numb:
    print("You need to guess a higher number.")
    attempt_taken +=1
    user_guess = int(input(f"Please guess a number between 1 and {upper_numb}: "))

print(f"You have guess the correct number in {attempt_taken} attempt!")
  
# Since you oened that can of worms, you should ensure every user entry is valid. Goob Job going above an beyond on the project.
