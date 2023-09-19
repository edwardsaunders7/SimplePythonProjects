order_list = [("tom", 0.87),
              ("sug", 2.09),
              ("ws", 0.29),
              ("juc", 1.89),
              ("fo", 2.29)]

# This dictionary gives the full name of each product code.
names = {"tom": "Tomatoes",
         "sug": "Sugar",
         "ws": "Washing Sponges",
         "juc": "Juice",
         "fo": "Foil"}

budget = 10.00
running_total = 0
receipt = []

for item in order_list:
    receipt.append(names[item[0]])
    cost = item[1]
    print(receipt)
    print(f"New item cost: £{cost}")

    if running_total + cost > budget:
      print(f"You cannot afford this item: {names[item[0]]}")
      break
    else:
      running_total = running_total + cost
      print(f"\nTotal cost: £{running_total}\n")
      

money_left = budget - running_total

print(f"You have £{money_left} left to spend")

