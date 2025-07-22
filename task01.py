def suggest_drink(weather):
    if weather == "hot":
        return "Try a Mojito!"
    elif weather == "cold":
        return "Go for a Hot Toddy!"
    elif weather == "rainy":
        return "How about a Dark 'n' Stormy?"
    else:
        return "Just have some water!"

print(suggest_drink("hot"))
