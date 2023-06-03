import random
import string

def random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#generate 100 lines
for _ in range(100):
    length = random.randint(4, 15)
    print(random_string(length))
