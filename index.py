# Calling the Random library
import random

# ALl Variable that needs to define
mainWords = ("a", "o", "u", "e", "i")
startWords = ("sch", "ch", "ph", "sh", "th", "sp", "st", "ss")
others = ("q", "w", "r", "t", "y", "i", "p", "s", "d", "f", "g",
          "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m")
numbers = (1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 0)

# The Password words length
PASSWORD_LENGTH = 10


# --- ALL TYPES OF GENERATIONS ---
# input: none, output: a Word starts with "Main words"
def genWord():
    temp = ""
    word = random.choice(mainWords)
    temp += word
    sec_word = random.choice(random.choice((startWords, others)))
    temp += sec_word
    return temp

# input: none, output: a Word starts with "Start words"
def genWord2():
    temp = ""
    word = random.choice(startWords)
    temp += word
    sec_word = random.choice(mainWords)
    temp += sec_word
    return temp

# input: none, output: a Number
def genNumber():
    temp = ""
    for x in range(0, 3):
        temp += str(random.choice(numbers))
    return temp

# Randomizing and generate words
# input: none, output: a generated word. It might be (Number, Word)
def generatingNewWord():
    random1 = random.choice((1, 2, 3))
    if random1 == 1:
        return genWord()
    elif random1 == 2:
        return genWord2()
    elif random1 == 3:
        return genNumber()

# Main function that loops the generate words function
# input: none, output: a string of password
def main():
    res = ""
    for x in range(PASSWORD_LENGTH - (PASSWORD_LENGTH // 2), PASSWORD_LENGTH):
        res += generatingNewWord()
    print(res)

# Calling the main function
main()