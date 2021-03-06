import random
# Get Guess
def get_guess():
    return list(input("What is your guess"))
# Generate Computer Code
def generate_code():
    digits = [str(num) for num in range(10)]

# Shuffle the digits
    random.shuffle(digits)
# Then grab the first three
    return digits[:3]

# Generate the clues

def generate_clues(code,user_guess):

    if user_guess==code:
        return "Code Cracked!"

    clues =  []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

    if clues == []:
        return ["Nope"]
    else:
        return clues

# Run Game logic

print("Welcome to the Game")

secret_code = generate_code()

clue_report = []

while clue_report != "Code Cracked!":
   guess = get_guess()
   clue_report = generate_clues(guess,secret_code)
   print("here is the result")
   for clue in clue_report:
       print(clue)
