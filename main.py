import random

num = int(input("Enter the maximum number: "))

n = random.randint(1, num)
guess = int(input("Enter your guess: "))

while n != "guess":
  if guess < n:
     print("guess is low")
     guess = int(input("Enter your guess: ")
  elif guess > n:
    print("guess is high")
    guess = int(input("Enter your guess: ")
  else:
    print("You guessed it!")
    break
