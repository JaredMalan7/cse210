from game.shared.color import Color
from game.shared.point import Point
from game.casting.actor import Actor


class Gem(Actor):
    """
    Gem: 
    Replace Artifact with Rock(Actor) and Gem(Actor) and Player(Actor) # Make 3 inheriting classes.
    Gem: inherits actor. have point value attribute. have a getter for point value.
    (Player: inherit actor. have point score. have getter and setter for point score.)
    (Rock: inherits actor. have point value attribute. have a getter for point value.)
    Give rocks and gems velocity. # Do when called in __main__.py 

    Attributes for Gem:
        _point_value(int): Point value which Gem has.
     """

    # def __init__(self):
    #     self._text = ""
    #     self._font_size = 15
    #     self._color = Color(255, 255, 255)
    #     self._position = Point(0, 0)
    #     self._velocity = Point(0, 0)

    def __init__(self):
        super().__init__()
        self._point_value = 0

    def get_point(self):
        # gets the point value of the gem
        return self._point_value
