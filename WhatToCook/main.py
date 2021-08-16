import csv

"""
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
"""

def ask_save_recipe():
    recipe_name = input("Name of Recipe: ")
    with open("recipes.csv", "a+") as recipes:
        writer = csv.writer(recipes, delimiter = ",")
        writer.writerow([recipe_name])

    while True:
        decision = input("Do you want to add an ingredient? (y) yes or (n) no: ").lower()
        if decision == "y":
            ingredient = input("Input the ingredient: ")
            amount = input("Input the amount (in kilograms): ")
            with open("recipes.csv", "a+") as recipes:
                writer = csv.writer(recipes, delimiter = ",")
                writer.writerow([ingredient , amount])
        elif decision == "n":
            with open("recipes.csv", "a+") as recipes:
                writer = csv.writer(recipes, delimiter = ",")
                writer.writerow([" "])
            print("New recipe added!")
            break
    return

def main():
    print("Hello World!")
    print("[The purpose of the program is written here.]")
    print("What to do? \n(1) Choose What To Cook \n(2) Add Ingredients \n(3) Add Recipe")
    decision = input()
    
    if decision == "1":
        pass
    elif decision == "2":
        pass
    elif decision == "3":
        ask_save_recipe()
    else:
        print("That is something I can't process...")

if __name__ == "__main__":
    main()
