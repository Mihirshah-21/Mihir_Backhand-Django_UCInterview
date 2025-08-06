import datetime

class Bartender:
  def __init__(self, name, joining_month, favorite_cocktail):
    # complete the constructor
    self.name = name 
    self.joining_month = joining_month
    self.favorite_cocktail = favorite_cocktail
    self.joining_month= datetime.datetime.strptime(joining_month, "%B").month
  def work_duration(self):
    # calculate how many full months since joining
    current_month= datetime.datetime.now().month
    duration = current_month - self.joining_month
    if duration < 0:
        duration += 12
    return duration

  def introduce(self):
    # return the formatted string
    print(f"Hello, my name is {self.name}. I have been working here for {self.work_duration()} months. My favorite cocktail is {self.favorite_cocktail}.")


b = Bartender("Aarushi", "December", "Cosmopolitan")
b.introduce()