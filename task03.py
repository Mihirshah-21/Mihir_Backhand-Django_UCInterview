menu = {
    "Mojito": 4.5,
    "Martini": 4.8,
    "Negroni": 4.2
}
# Print all cocktails with their ratings.
print(menu) 

# Check if Negroni is on the menu. If yes, return rating, if not, return a default message "Sorry! We don't serve this.".
if "Negroni" in menu: 
    print(menu["Negroni"])  
else : 
    print("Sorry! We don't serve this.")


# Check if LIIT is on the menu. If yes, return rating, if not, return a default message "Sorry! We don't serve this.".
if "LIIT" in menu:
    print(menu["LIIT"])
else:
    print("Sorry! We don't serve this.")

# Add a new drink: "Pina Colada" with a rating of 4.6.
menu.update({"Pina Colada":4.6,}) 
print(menu)

# Sort the cocktails from highest to lowest rated and print them in order.
sorted_menu = dict(sorted(menu.items( ), key=lambda item: item[1], reverse=True))
print(sorted_menu)