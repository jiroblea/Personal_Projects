#   Asks the user for recipes
def askRecipes():
    recipe_name = input("Name of the Recipe: ")
    print("Ingredients for the Recipe and corresponding amount: ")
    ingredients_num = int(input("How many ingredients will you input? "))
    with open("Recipes.txt", "w") as recipes:
        recipes.write(f"{recipe_name}\n")
    saveRecipe(ingredients_num)
    
# Save the inputted recipes to a file
def saveRecipe(ingredients_num):
    for i in range(0, ingredients_num):
        ingredient = input("Ingredient: ")
        ingredient_amount = input("Amount: ")
        with open("Recipes.txt", "a") as recipes:
            recipes.write(f"{ingredient}: {ingredient_amount}\n")


askRecipes()