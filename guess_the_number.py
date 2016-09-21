import random
import sys

class NumberGuessing:

    def __init__(self):
        # This is a constructor in Python
        # Initialize all your object variables here
        self.assigned_number = float(random.randint(0,10000))
        self.tries = 1
        self.max_tries = 10

    def can_try(self):
        if self.tries >= self.max_tries:
            return False
        else:
            return True

    def check_guess(self, number):
        # This is a method. The `self` object gives it access to object variables

        absolute_error = abs(self.assigned_number - float(number))

        percentage_error = float(absolute_error / self.assigned_number) * 100

        if percentage_error == 0:
            print "You found it. You Sherlock", self.assigned_number
            return True
        else:
            print "You are %s percent away from the correct number. %s tries remaining" % (percentage_error, self.max_tries - self.tries)
            return False


n = NumberGuessing()

while True:
    try:
        user_input = int(raw_input("Give me a guess(0-10000): "))
    except KeyboardInterrupt:
        print "You pressed Ctrl+c"
        break
    except:
        print "Your input is invalid. give me a number"
        continue

    if n.can_try():
        if n.check_guess(user_input):
            break
        n.tries += 1
    else:
        print "You are out of luck"
        break
