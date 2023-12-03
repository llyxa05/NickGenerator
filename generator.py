import random
import string
import sys

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def generate_nicknames(count):
    for _ in range(count):
        length = random.randint(4, 15)
        print(random_string(length))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("NickGen: python3 generator.py 10")
    else:
        count = int(sys.argv[1])
        generate_nicknames(count)
