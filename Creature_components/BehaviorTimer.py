
class BehaviorContext:
    def __init__(self, timers=None):
        if not timers:
            self.timers = {"find_food": 1,
                           "wait": 1,
                           "mitoz": 1
                       }
        else:
            self.timers = timers