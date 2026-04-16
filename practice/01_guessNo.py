import random

n = random.randint(1, 100)
attempts = 1
# a = int(input("Guess the Number between 1 and 100 🤔 : "))

# After (With Walrus):
# the not-equal operator (!=) has a higher priority than the walrus operator (:=)
while (a := int(input("Guess the Number 🤔 : "))) != n:
    if a > n:
        print("❌ Wrong no.! Please guess lower")
    elif a < n:
        print("❌ Wrong no.! Please guess higher number")
    # a = int(input("Guess the Number 🤔 : "))
    attempts += 1
    if attempts > 15:
        print("Sorry!😥 You have not guessed the correct no within 15 attempts")
        break
else:
    print(f"🎉 Guessed the correct number {a} in {attempts} attempts")
