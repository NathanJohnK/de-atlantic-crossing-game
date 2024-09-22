class Ship:
     def __init__(self, name, hit_points, armor, max_speed, position):
          self.name = name
          self.hit_points = hit_points
          self.armour = armor
          self.max_speed = max_speed
          self.position = position
     
     #adding in ship movement
     # Need to add sth in about the danger zone.
     # danger zone defined as being within 1000 metres of enemy


          
     def move(self, direction):
          if self.position == 0-0:
               print ("Prepare to move off")
          x, y = self.position
          if direction == "up":
               y += self.max_speed
          if direction == "down":
               y -= self.max_speed
          if direction == "left":
               x -= self.max_speed
          if direction == "right":
               x += self.max_speed
          
          self.position = (x, y)
          print(f"{self.name} moves {direction} to {self.position}")
              