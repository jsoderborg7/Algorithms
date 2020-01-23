#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  # Ok, so we need to loop through the amounts of ingredients currently present to see how many batches we can make
  
# number of batches of available ingredients
  store = []
# loop through recipe key/value pairs
  for item, needed in recipe.items():
# check that keys are present in ingredients 
    if item not in ingredients:
      return 0
# calculate number of batches
    min_amount = ingredients[item] // needed
# if not enough ingredients, exit
    if min_amount == 0:
      return 0
# if enough, save
    if min_amount > 0:
      store.append(min_amount)
  return min(store)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 64, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))