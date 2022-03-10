from game.scripting.action import Action


class MoveActorsAction(Action):

    def execute(self, cast, script):
        # 2) loop through the actors

        for actor in cast.get_all_actors():
            # 3) call the move_next() method on each actor
            actor.move_next()
