#A random number
import random
num = random.randint(10,20)

#Ask users to guess
while True:

  guess = int(input("Guess a num ranging from 10 to 20:"))

  if guess == num:
    print("Congratulations!")
    break
  else:
    print("Wrong.Try again.")
