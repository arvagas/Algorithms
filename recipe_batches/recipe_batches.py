#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    batch_amts = []

    for i in recipe:
        if i not in ingredients or recipe[i] > ingredients[i]:
            return 0
        else:
            batch_amts.append(int(ingredients[i]/recipe[i]))
        
    return min(batch_amts)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))