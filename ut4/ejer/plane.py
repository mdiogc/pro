class Plane:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
  
    def kamikaze(self):
        probability_percentage = 1.1
        max_passengers = probability_percentage * self.capacity
        if len(self.passengers) > self.capacity:
            msg = "There is a strange passenger."
            if len(self.passengers) > max_passengers:
                msg = "There's a high probability of the plane exploding!"
            else:
                msg = "The plane avoids disaster."
        else:
            msg = "No strange passengers detected. Safe flight!"

        print(msg)
