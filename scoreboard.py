from constants import MAX_SCORE

class Scoreboard():
    def __init__(self):
        self.__score = 0

    def update_score(self, amount):
        if amount <= 0:
            print("Cannot add negative or 0 score.")
        elif self.__score + amount > MAX_SCORE:
            print(f"Max score is {MAX_SCORE}")
        else:
            self.__score += amount

    def get_score(self):
        return self.__score
