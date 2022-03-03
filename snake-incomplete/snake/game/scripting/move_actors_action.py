
from game.scripting.action import Action


# Todo: Implement MoveActorsAction class here!


# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
class MoveActorsAction(Action):

    def execute(self, cast, script):
        # 2) loop through the actors

        for actor in cast.get_all_actors():
            # 3) call the move_next() method on each actor
            actor.move_next()
