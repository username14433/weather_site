import random
def create_daypart_rain_chance():
    parts_of_the_day = ['morning', 'noon', 'evening']
    rain_chance = random.randint(0, 100)
    part_of_the_day = random.choice(parts_of_the_day)
    return {'rain_chance': rain_chance, 'part_of_the_day': part_of_the_day}
