class Car:

    def __init__(self, name, color, top_speed=60):
        self.name = name
        self.color = color
        self.top_speed = top_speed
        self.current_speed = 0

    def accelerate(self):
        if self.current_speed > self.top_speed:
            print "You need to slow down"
        else:
            self.current_speed = self.current_speed + 15
            print "You are now travelling at", self.current_speed, "Kmph"
