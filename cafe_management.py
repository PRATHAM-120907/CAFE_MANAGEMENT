menu = {
    "Pizza": 120,
    "Pasta": 90,
    "Burger": 60,
    "Coffee": 100,
    "Ramen": 500,
    "Fried chicken": 400,
}

print("WELCOME TO OUR CAFE!!")
print("")

print("Pizza: 120\nPasta: 90\nBurger: 60\nCoffee: 100\nRamen: 500\nFried chicken: 400")

order_total = 0
order_count = 0

while order_count < 2:
    item = input("PLEASE ENTER THE NAME OF THE DISH TO ORDER: ")
    if item in menu:
        order_total += menu[item]
        order_count += 1
        print(f"YOUR {item} HAS BEEN ADDED TO YOUR ORDER")
    else:
        print(f"{item} IS NOT AVAILABLE IN MENU")

print(f"YOUR TOTAL BILL TO PAY IS: {order_total}")
