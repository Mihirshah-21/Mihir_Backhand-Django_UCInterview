def make_cocktail(name,ingredients):
   print(f"Making {name}")
   for p in range(len(ingredients)):
    print(f"Step {p+1}: Add {ingredients[p]}")
   print("Enjoy your drink!")
   
make_cocktail("Mojito", ["rum", "lime", "mint"])