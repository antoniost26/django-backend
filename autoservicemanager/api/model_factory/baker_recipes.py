from model_bakery.recipe import Recipe
from api.models import Car
from api.car_brands import CAR_BRANDS
from itertools import cycle
from random import shuffle

aq_yr = list(range(1900, 2021))
shuffle(aq_yr)
shuffle(CAR_BRANDS)
car_recipe = Recipe(
    Car,
    model=cycle(CAR_BRANDS),
    an_achizitie=cycle(aq_yr),
)
