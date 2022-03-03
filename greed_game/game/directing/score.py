class Score:

    """ Keeps track for the value score and updating  and showing 

        attributes:
        Score: Set the value how the game start
        Substract:  every time hits a rock substract 50 points
        add: Evry time hits a gems add 50 points
        Methods:
           update_points
           show_score
            """

    def __init__(self):
        self.__score = 600
        self.__substract = 50
        self.__add = 50

    def update_points(self, operation):
        if operation == '+':
            self.__score = self.__score + self.__add
        elif operation == '-':
            print("discounting")
            self.__score = self.__score - self.__substract
        else:
            self.__score = 0

    def show_score(self):
        score_message = "Score: " + str(self.__score)
        return score_message
