#!/usr/bin/python

def recipe_batches(recipe, ingredients):
  values = []
  for i in recipe:
        if i not in ingredients:
              return 0
        else:
            values.append(ingredients[i] // recipe[i])

  smallest = values[0]
  for i in range(len(values)):
      if values[i] < smallest:
          smallest = values[i]
          
  return smallest
    

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))